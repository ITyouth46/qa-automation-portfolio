import pytest
import requests

# 1. Наша фикстура теперь называется api_url
@pytest.fixture
def api_url():
    return "https://jsonplaceholder.typicode.com"

# 2. В скобках мы запрашиваем именно api_url
def test_todo_status(api_url):
    response = requests.get(f"{api_url}/todos/1")
    assert response.status_code == 200

# 3. Здесь в скобках тоже api_url
@pytest.mark.parametrize("todo_id", [9999, 8888, 7777])
def test_non_existent_todo(api_url, todo_id):
    response = requests.get(f"{api_url}/todos/{todo_id}")
    assert response.status_code == 404