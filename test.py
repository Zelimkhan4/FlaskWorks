from requests import get


# Задача номер 3
response = get("http://127.0.0.1:5000/api/jobs").json()
print(response)
response = get("http://127.0.0.1:5000/api/jobs/2").json()
print(response)
response = get("http://127.0.0.1:5000/api/jobs/100").json()
print(response)
response = get("http://127.0.0.1:5000/api/jobs/some_job").json()
print(response)

