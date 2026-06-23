import pytest
import requests

@pytest.mark.parametrize("limit, expected_status", [
    (10000, 201),
    (50000, 201),
    (50001, 400),
    (-400, 400),
    (0, 400)
])

def test_create_credit_card_success(limit, expected_status):

    url = ("https://jsonplaceholder.typicode.com/posts")
    
    payload = {
        "title": "Мой первый автотест",
        "body": "Работает!",
        "credit_limit": limit
    }
    
    response = requests.post(url, json=payload)
    
    assert response.status_code == expected_status
