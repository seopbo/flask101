from flask import Flask

app = Flask(__name__) # Flask 웹 어플리케이션

# app 변수에 API의 설정과 엔드포인트들을 추가한다.
## route decorator를 활용하여 엔드포인트를 등록한다. (이 경우 엔드포인트에 ping function을 등록함)
@app.route("/ping", methods=["GET"])
def ping():
    return "pong"
