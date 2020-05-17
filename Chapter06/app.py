import os
from flask import Flask, jsonify, request, current_app
from flask.json import JSONEncoder
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


# Flask가 create_app이라는 이름의 함수를 자동으로 factory 함수로 인식, Flask 실행함.
# test_config이라는 parameter는 unit test를 실행시킬 때, 테스트용 데이터베이스의 설정 정보를 적용하기 위함.
def create_app(test_config=None):
    app = Flask(__name__)

    if not test_config:
        app.config.from_pyfile("config.py")
    else:
        app.config.update(test_config)

    database = create_engine(app.config["DB_URL"], encoding="utf-8", max_overflow=0)  # 데이터베이스와 연결
    app.database = database  # Flask instance의 attribute로 가리킴

    @app.route("/ping", methods=["GET"])
    def ping():
        return ping

    @app.route("/sign-up", methods=["POST"])
    def sign_up():
        new_user = request.json
        new_user_id = insert_user(new_user)
        new_user = get_user(new_user_id)
        return jsonify(new_user)

    @app.route("/tweet", methods=["POST"])
    def tweet():
        user_tweet = request.json
        tweet = user_tweet["tweet"]

        if len(tweet) > 300:
            return "300자를 초과했습니다", 400

        insert_tweet(user_tweet)

        return "", 200

    @app.route("/timeline/<int:user_id>", methods=["GET"])
    def timeline(user_id):
        return jsonify(dict(user_id=user_id, timeline=get_timeline(user_id)))

    @app.route("/follow", methods=["POST"])
    def follow():
        payload = request.json
        insert_follow(payload)
        return "", 200

    @app.route("/unfollow", methods=["POST"])
    def unfollow():
        payload = request.json
        insert_unfollow(payload)
        return "", 200

    return app  # Flask instance를 return


if __name__ == "__main__":
    os.system("./run_server.sh")
