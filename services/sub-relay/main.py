import os
from flask import Flask, request

project_root = os.path.dirname(__file__)
app = Flask(__name__)

if not os.getenv("AUTH_TOKEN"):
    raise Exception("AUTH_TOKEN not set")


@app.route("/<token>")
def retrieve(token):
    try:
        with open(f"{project_root}/data/{token}", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "No access", 400


@app.route("/update/<token>", methods=["POST"])
def save(token):
    if request.headers.get("Authorization") != f"Bearer {os.getenv('AUTH_TOKEN')}":
        return "Unauthorized", 401
    with open(f"{project_root}/data/{token}", "w") as f:
        f.write(request.data.decode("utf-8"))
    return "OK", 201
