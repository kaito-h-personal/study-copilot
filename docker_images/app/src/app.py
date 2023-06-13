import json

from flask import Flask, jsonify, request

import pymysql

app = Flask(__name__)


@app.route("/")
def index():
    # pymysqlを使用してDBからデータを取得して表示する
    connection = pymysql.connect(
        host="db",
        port=3306,
        user="dbuser",
        password="pasuwaado",
        database="db",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )
    with connection.cursor() as cursor:
        # cursor.executeのINSERT文のサンプルコード作成
        cursor.execute("INSERT INTO `product` (`id`, `name`) VALUES (1, 'test')")
        cursor.execute("SELECT * FROM `product`")
        result = cursor.fetchall()

    print("test print")
    print(result)

    # resultのdictをstringに変換して表示する
    result = str(result) + '\ntest'
    return result


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
    p = request.form['password']
    return jsonify({"id": 3, "password": p})
