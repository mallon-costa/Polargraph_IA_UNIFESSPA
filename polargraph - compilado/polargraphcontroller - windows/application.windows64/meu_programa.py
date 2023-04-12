import json
import base64
import argparse
from textblob import TextBlob
import requests


def submit_post(url: str, data: dict):
    """
    Submit a POST request to the given URL with the given data.
    """
    return requests.post(url, data=json.dumps(data))


def save_encoded_image(b64_image: str, output_path: str):
    """
    Save the given image to the given output path.
    """
    with open(output_path, "wb") as image_file:
        image_file.write(base64.b64decode(b64_image))


if __name__ == '__main__':
    # Crie o analisador de argumentos
    parser = argparse.ArgumentParser()
    parser.add_argument('--prompt', type=str, help='prompt string')

    # Analise os argumentos da linha de comando
    args = parser.parse_args()

    # Obtenha o valor do argumento 'prompt'
    prompt = args.prompt

    # Se o valor de 'prompt' não foi especificado, defina um valor padrão
    if not prompt:
        prompt = "a dog"

    blob = TextBlob(prompt)
    traducao = blob.translate(from_lang='pt', to='en')
    prompt = str(traducao)
    print(prompt)
    
    # Defina o URL do endpoint do txt2img
    txt2img_url = 'http://127.0.0.1:7860/sdapi/v1/txt2img'
    data = {'prompt': prompt}

    # Envie uma solicitação POST para o endpoint
    response = submit_post(txt2img_url, data)

    # Print the response content and status code for debugging
    print(response.content)
    print(response.status_code)

    # Salve a imagem gerada
    save_encoded_image(response.json()['images'][0], 'saida.png')
