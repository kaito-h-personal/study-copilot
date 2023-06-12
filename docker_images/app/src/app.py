import json

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    return "index page is here!"


@app.route("/test")
def test_page():
    d = {"name": "test", "age": 20}
    # jsonifyを使うと、json形式で返してくれる
    return jsonify(d)


# jsonで受け取る
# 例: curl -X POST -H "Content-Type: application/json" -d '{"password": "test_password"}' http://localhost:5001/test_post_json
@app.route("/test_post_json", methods=["POST"])
def test_page_post_json():
    d = request.get_json()
    print(d)
    return jsonify(d)


# フォームで受け取る
# 例: curl -X POST -F "password=test_password" http://localhost:5001/test_post
@app.route("/test_post", methods=["POST"])
def test_page_post():
    # p = request.form.get('password')
    p = request.form['password']
    return jsonify({"id": 3, "password": p})
