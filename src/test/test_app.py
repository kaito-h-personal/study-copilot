import pytest
import json

import app

# テストコードの先頭でフラスクアプリの設定を行う部分をフィクスチャ内に移動しました。
@pytest.fixture
def test_client():
    # テストコードの冗長な部分を削除し、共通の処理をフィクスチャ内で実行するようにしました。
    app.flask_app.config['TESTING'] = True
    return app.flask_app.test_client()

# test_client を共通のフィクスチャとして使用するように変更し、各テスト関数の引数として渡すようにしました。
def test_sample_page_post_json(test_client):
    # テスト用のデータを作成
    data = {"key": "value"}
    json_data = json.dumps(data)

    # POSTリクエストを送信
    response = test_client.post(
        "/sample_post_json",
        data=json_data,
        content_type="application/json"
    )

    # レスポンスを検証
    assert response.status_code == 200
    assert response.json == data

def test_product_get(test_client):
    # テスト用のデータを作成
    exp_data = [{"id": 1, "name": "test", "col": None}]
    json_data = json.dumps(exp_data)

    # "INSERT INTO `product` (`id`, `name`) VALUES (1, 'test')"を実行してmysqlにINSERTする
    with app.connection.cursor() as cursor:
        cursor.execute("INSERT INTO `product` (`id`, `name`) VALUES (1, 'test')")

    # GETリクエストを送信
    response = test_client.get(
        "/product",
        data=json_data,
        content_type="application/json"
    )

    # レスポンスを検証
    assert response.status_code == 200
    assert response.json == exp_data

def test_product_post(test_client):
    # テーブルをクリアする
    with app.connection.cursor() as cursor:
        cursor.execute("DELETE FROM `product` where id=1")
        # app.connection.commit() を追加して、データベースの変更を確定させるようにしました。
        app.connection.commit()

    # テスト用のデータを作成
    exp_data = [{"id": 1, "name": None, "col": "testmemo"}]
    json_data = json.dumps(exp_data)

    # POSTリクエストを送信
    response = test_client.post(
        "/product/1/testmemo",
        content_type="application/json"
    )

    # レスポンスを検証
    assert response.status_code == 200

    # mysqlのデータを検証 productテーブルの中身が1行でid=1, name=test, memo=testmemoになっていることを確認する
    with app.connection.cursor() as cursor:
        cursor.execute("SELECT * FROM `product` where id=1")
        result = cursor.fetchall()
        print(result)
    assert result == exp_data
