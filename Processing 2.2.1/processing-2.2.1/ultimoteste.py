import requests

url = 'http://127.0.0.1:7861/predict'
headers = {'Content-type': 'application/json'}
data = {'input': 'Um gato sentado em uma caixa'}

response = requests.post(url, json=data, headers=headers)

with open('imagem_gerada.png', 'wb') as f:
    f.write(response.content)
