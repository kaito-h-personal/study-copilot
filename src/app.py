import json

from flask import Flask, jsonify, request

import pymysql

flask_app = Flask(__name__)
connection = pymysql.connect(
    host="db",
    port=3306,
    user="dbuser",
    password="pasuwaado",
    database="db",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)


@flask_app.route("/")
def index():
    # pymysqlを使用してDBからデータを取得して表示する
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


@flask_app.route("/sample")
def sample_page():
    d = {"name": "test", "age": 20}
    # jsonifyを使うと、json形式で返してくれる
    return jsonify(d)


# jsonで受け取る
# 例: curl -X POST -H "Content-Type: application/json" -d '{"password": "test_password"}' http://localhost:5001/test_post_json
@flask_app.route("/sample_post_json", methods=["POST"])
def sample_page_post_json():
    d = request.get_json()
    print(d)
    return jsonify(d)


# pymysqlでproductの中身を取得してjsonで返すGETメソッド
@flask_app.route("/product", methods=["GET"])
def product_get():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM `product`")
        result = cursor.fetchall()
    return jsonify(result)


# 引数でproductのidとmemo(テキスト)を受けとってpymysqlでproductのmemoにINSERTするPOSTメソッド
@flask_app.route("/product/<int:id>/<string:memo>", methods=["POST"])
def product_post(id, memo):
    with connection.cursor() as cursor:
        result = cursor.execute("INSERT INTO `product` (`id`, `col`) VALUES (%s, %s)", (id, memo))
        connection.commit()  # データベースの変更を確定する
    return jsonify(result)