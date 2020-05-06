import os
from flask import Flask, jsonify, request  # 1

app = Flask(__name__)
app.users = {}
app.id_count = 1


@app.route("/ping", methods=["GET"])
def ping():
    return "pong"


@app.route("/sign-up", methods=["POST"])  # 2
def sign_up():
    new_user = request.json  # 3
    new_user["id"] = app.id_count
    app.users[app.id_count] = new_user
    app.id_count += 1
    return jsonify(new_user)  # 4


if __name__ == "__main__":
    os.system("./run_server.sh")
