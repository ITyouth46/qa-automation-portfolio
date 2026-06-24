import pytest
import requests

# Создаем фикстуру, которая возвращает базовый URL
@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"

# Передаем имя фикстуры прямо в аргументы теста! PyTest сам подставит туда значение
def test_todo_status(base_url):
    response = requests.get(f"{base_url}/todos/1")
    data = response.json()
    assert response.status_code == 200
    assert data["completed"] == False

@pytest.mark.parametrize("todo_id", [9999, 8888, 7777])
def test_non_existent_todo(base_url, todo_id):
    response = requests.get(f"{base_url}/todos/{todo_id}")
    assert response.status_code == 200