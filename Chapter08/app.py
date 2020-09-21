import os
import bcrypt
import jwt

from functools import wraps
from flask import Flask, jsonify, current_app, request, Response, g
from flask_cors import CORS
from flask.json import JSONEncoder
from datetime   import datetime, timedelta
from sqlalchemy import create_engine, text


# dict의 key에 대한 value가 set일 때, list로 변경, 그 이외에는 원래의 동작대로
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return JSONEncoder.default(self, obj)


def get_user(user_id):
    user = current_app.database.execute(text("""
    SELECT id, name, email, profile FROM users WHERE id =:user_id
    """), {"user_id": user_id}).fetchone()
    return dict(id=user["id"], name=user["name"], email=user["email"], profile=user["profile"])


def insert_user(user):
    return current_app.database.execute(text("""
    INSERT INTO users (name, email, profile, hashed_password) VALUES (:name, :email, :profile, :password)
    """), user).lastrowid


def insert_tweet(user_tweet):
    current_app.database.execute(text("""
    INSERT INTO tweets (user_id, tweet) VALUES (:id, :tweet)
    """), user_tweet).rowcount


def get_timeline(user_id):
    timeline = current_app.database.execute(text("""
    SELECT t.user_id, t.tweet FROM tweets t
    LEFT JOIN users_follow_list ufl ON ufl.user_id = :user_id
    WHERE t.user_id = :user_id
    OR t.user_id = ufl.follow_user_id
    """), {"user_id": user_id}).fetchall()

    return [{"user_id": tweet["user_id"], "tweet": tweet["tweet"]} for tweet in timeline]


def get_user_id_and_password(email):
    row = current_app.database.execute(text("""    
        SELECT
            id,
            hashed_password
        FROM users
        WHERE email = :email
    """), {'email' : email}).fetchone()

    return {
        'id'              : row['id'],
        'hashed_password' : row['hashed_password']
    } if row else None


def insert_follow(user_follow):
    current_app.database.execute(text("""
    INSERT INTO users_follow_list (user_id, follow_user_id) VALUES (:id, :follow)
    """), user_follow)


def insert_unfollow(user_unfollow):
    current_app.database.execute(text("""
    DELETE FROM users_follow_list
    WHERE user_id = :id
    AND follow_user_id = :unfollow
    """), user_unfollow)


#########################################################
#       Decorators
#########################################################
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        access_token = request.headers.get('Authorization')
        if access_token is not None:
            try:
                payload = jwt.decode(access_token, current_app.config['JWT_SECRET_KEY'], 'HS256')
            except jwt.InvalidTokenError:
                 payload = None

            if payload is None:
                return Response(status=401)

            user_id = payload['user_id']
            g.user_id = user_id
            g.user = get_user(user_id) if user_id else None
        else:
            return Response(status=401)
        return f(*args, **kwargs)
    return decorated_function


# Flask가 create_app이라는 이름의 함수를 자동으로 factory 함수로 인식, Flask 실행함.
# test_config이라는 parameter는 unit test를 실행시킬 때, 테스트용 데이터베이스의 설정 정보를 적용하기 위함.
def create_app(test_config=None):
    app = Flask(__name__)

    CORS(app)

    if not test_config:
        app.config.from_pyfile("config.py")
    else:
        app.config.update(test_config)

    database = create_engine(app.config["DB_URL"], encoding="utf-8", max_overflow=0)  # 데이터베이스와 연결
    app.database = database  # Flask instance의 attribute로 가리킴
    app.config["JWT_SECRET_KEY"] = "boseop"

    @app.route("/ping", methods=["GET"])
    def ping():
        return "pong"

    @app.route("/sign-up", methods=["POST"])
    def sign_up():
        new_user = request.json
        new_user["password"] = bcrypt.hashpw(password=new_user["password"].encode("utf-8"),
                                             salt=bcrypt.gensalt())
        new_user_id = insert_user(new_user)
        new_user = get_user(new_user_id)
        return jsonify(new_user)

    @app.route("/login", methods=["POST"])
    def login():
        credential = request.json
        email = credential["email"]
        password = credential["password"]
        user_credential = get_user_id_and_password(email)

        if user_credential and bcrypt.checkpw(password=password.encode("utf-8"),
                                              hashed_password=user_credential["hashed_password"].encode("utf-8")):
            user_id = user_credential["id"]
            payload = {
                "user_id": user_id,
                "exp": datetime.utcnow() + timedelta(seconds = 60 * 60 * 24)
            }
            token = jwt.encode(payload=payload,
                               key=app.config["JWT_SECRET_KEY"],
                               algorithm="HS256")
            return jsonify({
                "access_token": token.decode("utf-8")
            })
        else:
            return "", 401

    @app.route("/tweet", methods=["POST"])
    @login_required
    def tweet():
        user_tweet = request.json
        user_tweet['id'] = g.user_id
        tweet = user_tweet["tweet"]

        if len(tweet) > 300:
            return "300자를 초과했습니다", 400

        insert_tweet(user_tweet)

        return "", 200

    @app.route("/timeline/<int:user_id>", methods=["GET"])
    def timeline(user_id):
        return jsonify(dict(user_id=user_id, timeline=get_timeline(user_id)))

    @app.route("/timeline", methods=["GET"])
    @login_required
    def user_timeline():
        user_id = g.user_id

        return jsonify({
            "user_id": user_id,
            "timeline": get_timeline(user_id)
        })

    @app.route("/follow", methods=["POST"])
    @login_required
    def follow():
        payload = request.json
        payload['id'] = g.user_id
        insert_follow(payload)
        return "", 200

    @app.route("/unfollow", methods=["POST"])
    @login_required
    def unfollow():
        payload = request.json
        payload['id'] = g.user_id

        insert_unfollow(payload)
        return "", 200

    return app  # Flask instance를 return


if __name__ == "__main__":
    os.system("./run_server.sh")
