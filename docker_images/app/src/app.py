# 簡単なindexページの作成を行っています。
from flask import Flask

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
