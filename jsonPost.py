import requests
import json

url = 'http://127.0.0.1:5000'
headers = {'Content-type': 'application/json',  # Определение типа данных
           'Accept': 'text/plain',
           'Content-Encoding': 'utf-8'}
data = {"id": "999"}
data = {'id': "9-9-7", 'name': 'Магнит2',
        'description': 'Магазин продуктоv',
        'website': 'magnit2.com',
        'image': 'None',
        'marks': [{'name': 'Холодильник', #'id': '13',
                   'description': 'Холодильник с мороженым',
                   'position': {'lat': 123.12, 'lng': 321.32121}}],
        'position': {'lat': 123.1, 'lng': 321.3}}
data = {"id": "9-9-7"}
markAll = "/api/shop/mark/all" # id: shopID
markAdd = "/api/shop/mark/put" # 
markGet = "/api/mark/get" # id: markID
markDel = "/api/mark/del" # id: markID

shopAll = "/api/shop/all" 
shopAdd = "/api/shop/put"
shopGet = "/api/shop/get" # id: shopID
shopDel = "/api/shop/del" # id: shopID
answer = requests.post(url + "/api/shop/mark/all", data=json.dumps(data))
print(answer)
response = answer.json()
print(response)
