import json
import os
import tarfile
from six.moves import urllib

from tinydb import TinyDB, Query

db = TinyDB('db.json')
qr = Query()


def loadDataFromJSON(path):
    json_data=open(path).read()
    data = json.loads(json_data)
    return data


def saveRelicDataToDatabase(data):
    relic_Data = data["relicRewards"]
    for relics in relic_Data:
        for item in relic_Data[relics]['rewards']:
            db.insert({'table': 'relic', 'tier':relic_Data[relics]['tier'], 'type':relic_Data[relics]['type'], 'name':item['name'], 'rarity':item['intact']['name']})


def resetDatabase():
    db.purge()
    saveRelicDataToDatabase(loadDataFromJSON('./allinone.json'))


def updateDatabase():
    download_Path_allinone = "https://destiny.trade/JSON/allinone.json"
    urllib.request.urlretrieve(download_Path_allinone, "./allinone.json")
    resetDatabase()


