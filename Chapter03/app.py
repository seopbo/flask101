import os
from flask import Flask

# Flask 클래스를 instantiate해서 app 변수로 가리킨다.
# app 변수가 Flask 웹 어플리케이션
# app 변수에 API의 설정과 엔드포인트들을 추가하여 API를 완성한다.
app = Flask(__name__)


# route 데코레이터를 사용하여 엔드포인트를 웹 어플리케이션에 등록한다.
# Flask가 알아서 HTTP response로 변환하여, HTTP request를 보낸 client에게 전송함.
@app.route("/ping", methods=["GET"])
def ping():
    return "pong"


if __name__ == "__main__":
    # debug=True는 디버그 모드를 활성화시킴.
    # 디버그 모드가 활성화된 상태에서는 코드가 수정되었을 때, Flask 어플리케이션이 직접 자동으로 재시작되어, 수정된 코드를 반영한다.
    # app.run(debug=True)
    os.system("./run_server.sh")

