import requests

endpoint = 'http://127.0.0.1:8000/libro/2'
endpoint_add = 'http://127.0.0.1:8000/libro/create'
endpoint_api_view = 'http://127.0.0.1:8000/libro'
response = requests.get(endpoint_api_view)
# response = requests.post(endpoint_add, json={'titulo': 'Los juegos del hambre', 'autor': 'Suzanne Collins'})

print(response.json())