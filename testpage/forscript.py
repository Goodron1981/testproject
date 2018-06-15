import requests
from django.utils.baseconv import base64


def speech():
    url = "https://texttospeech.googleapis.com/v1beta1/text:synthesize"

    querystring = {"key":"AIzaSyA3pUu1l9rLzOnNtFaszrIB9weEq1Za3Ws"}
    proxies = {
        'http': 'http://10.18.7.6:3128',
        'https': 'http://10.18.7.6:3128',
    }

    payload = "{\r\n  \"audioConfig\": {\r\n    \"audioEncoding\": \"LINEAR16\",\r\n    \"pitch\": \"0.00\",\r\n    \"speakingRate\": \"1.00\"\r\n  },\r\n  \"input\": {\r\n    \"text\": \"Google Cloud Text-to-Speech enables developers to synthesize natural-sounding speech with 32 voices, available in multiple languages and variants. It applies DeepMind’s groundbreaking research in WaveNet and Google’s powerful neural networks to deliver the highest fidelity possible. As an easy-to-use API, you can create lifelike interactions with your users, across many applications and devices.\"\r\n  },\r\n  \"voice\": {\r\n    \"languageCode\": \"en-US\",\r\n    \"name\": \"en-US-Wavenet-D\"\r\n  }\r\n  \r\n}\r\n"
    headers = {
        'Content-Type': "application/json",
        'Cache-Control': "no-cache",
        'Postman-Token': "6ee70ade-5e80-433a-9692-8c157c5cc915"
        }

    #response = requests.request("POST", url, data=payload, headers=headers, params=querystring, proxies=proxies)
    # response = requests.post(url=url, data=payload, headers=headers, proxies=proxies, params=querystring)
    f = open('Pos.txt', 'r')
    b = base64.b64decode(f.read())
    f.close()
    # print(response.text)
    with open('output.mp3', 'wb') as out:
        out.write(b)
        print('Audio content written to file "output.mp3"')