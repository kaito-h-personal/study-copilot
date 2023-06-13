import pytest

import app


# test_page_post_jsonのテストコード
def test_test_page_post_json():
    with app.test_client() as c:
        response = c.post("/test_post_json", json={"password": "test_password"})
        assert response.status_code == 200
        assert response.json == {"password": "test_password"}
