import requests
import json

# Enviar uma solicitação GET para o endpoint raiz da API
response = requests.get("http://127.0.0.1:7861/")

# Verificar se a resposta é uma string JSON válida
try:
    api_info = json.loads(response.content)
except json.JSONDecodeError as e:
    print(f"A resposta da API não é uma string JSON válida: {e}")
else:
    # Filtrar os métodos que usam o parâmetro "prompt"
    prompt_methods = [method for method in api_info['endpoints'] if 'prompt' in method['inputs']]

    # Imprimir os métodos filtrados
    print(prompt_methods)
