import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

print("С какого языка переводить")
from_lang = str(input())
print("На какой язык переводить")
to_lang = str(input())
print("Введите текст для перевода")
text = str(input())

params = {
    'key': API_KEY,
    'text': text,
    'lang': '{}-{}'.format(from_lang, to_lang),
}

response = requests.get(URL, params=params)
json_ = response.json()
output_text = ''.join(json_['text'])

print('\n', output_text)
