import requests

# Отправляем запрос
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
data = response.json()  # Вытащили JSON и превратили в словарь

# ПРОВЕРКА: берем именно status_code и сравниваем с числом 200
if response.status_code == 200 and data["completed"] == False:
    print("Тест пройден: Сервер ответил 200 OK")
else:
    print(f"Тест упал: Ошибка! Статус-код: {response.status_code}")

# Твоя отличная отладка данных:
print(f"Фактический код: {response.status_code}")
print(f"Тело ответа (JSON): {response.json()}")