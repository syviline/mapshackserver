import requests
import json

URL = url = 'http://127.0.0.1:5000'
# URL = "https://mapshack.herokuapp.com/"
CITY = "Тюмень"

_markAll = "/api/shop/mark/all" # id: shopID
_markAdd = "/api/shop/mark/put" # 
_markGet = "/api/mark/get" # id: markID
_markDel = "/api/mark/del" # id: markID

_shopAll = "/api/shop/all" 
_shopAdd = "/api/shop/put"
_shopGet = "/api/shop/get" # id: shopID
_shopDel = "/api/shop/del" # id: shopID

_cityAll = "/api/city/all" 

def reqePost(url, command, data={}):
    answer = requests.post(url + command, data=json.dumps(data))
    response = answer.json()
    return response 

def addMark(shopID, name, descript, lat, lng, markID=None):
    data = {"shopID": shopID, "name": name,
            "description": descript,
            "position": {"lat": lat, "lng": lng}}
    if markID:
        data["markID"] = markID
    return reqePost(URL, _markAdd, data)


def addShop(ID, name, descript, lat, lng, website="NULL", image="NULL", marks=[], city="NULL"):
    data = {"id": ID, "name": name,
            "description": descript,
            "website": website,
            "image": image,
            "position": {"lat": lat, "lng": lng},
            "marks": marks,
            "city": city}
    
    return reqePost(URL, _shopAdd, data)

data = {"id": "9-9-6"}
dataM = {"id": "1-7"}

print(_cityAll, reqePost(URL, _cityAll), sep="\n")
input()

print(_shopAdd, addShop("9-9-6", "Монеточка",
                        "Магазин продуктов", 12.1, 46.34,
                        "monetka.ru", image="nulllll",
                        city = CITY,
                        marks = [{'name': 'Холодильник', #'id': '13',
                   'description': 'Холодильник с молоком',
                   'position': {'lat': 12.12, 'lng': 32.31},
                                  'id': '1-7'}]), sep="\n")
input()
print(_shopAll, reqePost(URL, _shopAll), sep="\n")
input()

print(_markAdd, addMark("9-9-6", "Полка", "Полка шеколадками2", 12.1, 46.34, "1-7"), sep="\n")
input()
print(_markAdd, addMark("9-9-6", "Полка", "Полка nuts", 12.2, 46.35, "1-8"), sep="\n")
input()
print(_markAll, reqePost(URL, _markAll, data), sep="\n")
input()
print(_markGet, reqePost(URL, _markGet, dataM), sep="\n")
input()
print(_shopGet, reqePost(URL, _shopGet, data), sep="\n")
input()
print(_markDel, reqePost(URL, _markDel, dataM), sep="\n")
input()
print(_markAll, reqePost(URL, _markAll, data), sep="\n")
input()
print(_markDel, reqePost(URL, _markDel, {"id": "18"}), sep="\n")
input()
print(_shopDel, reqePost(URL, _shopDel, data), sep="\n")
input()
print(_shopAll, reqePost(URL, _shopAll, {"city": CITY}), sep="\n")
input()
