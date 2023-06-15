import pytest
import json

import app

# sample_post_json()の単体テストコード
def test_sample_page_post_json():
    app.flask_app.config['TESTING'] = True
    client = app.flask_app.test_client()

    # テスト用のデータを作成
    data = {"key": "value"}
    json_data = json.dumps(data)

    # POSTリクエストを送信
    response = client.post(
        "/sample_post_json",
        data=json_data,
        content_type="application/json"
    )

    # レスポンスを検証
    assert response.status_code == 200
    assert response.json == data

# product_getの単体テストコード
def test_product_get():
    app.flask_app.config['TESTING'] = True
    client = app.flask_app.test_client()

    # テスト用のデータを作成
    exp_data = [{"id": 1, "name": "test", "col": None}]
    json_data = json.dumps(exp_data)

    # "INSERT INTO `product` (`id`, `name`) VALUES (1, 'test')"を実行してmysqlにINSERTする
    with app.connection.cursor() as cursor:
        cursor.execute("INSERT INTO `product` (`id`, `name`) VALUES (1, 'test')")

    # GETリクエストを送信
    response = client.get(
        "/product",
        data=json_data,
        content_type="application/json"
    )

    # レスポンスを検証
    assert response.status_code == 200
    assert response.json == exp_data