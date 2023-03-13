from requests import get, post


# Задача 6


# Корректный запрос
response = post("http://127.0.0.1:5000/api/jobs",
                json={"id": 15, "job": "some job", "team_leader": 1})
print(response.json())


# Запрос добавления по существующему id
response = post("http://127.0.0.1:5000/api/jobs",
                json={"id": 15, "job": "some job", "team_leader": 1})
print(response.json())


# Нет обязательного поля id
response = post("http://127.0.0.1:5000/api/jobs",
                json={"job": "some job", "team_leader": 1})
print(response.json())


# Пустой запрос
response = post("http://127.0.0.1:5000/api/jobs",
                json={})
print(response.json())


# Список всех работ
response = get("http://127.0.0.1:5000/api/jobs")