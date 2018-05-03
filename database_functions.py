import json
import vault_functions
import re
from six.moves import urllib

from tinydb import TinyDB, Query

db = TinyDB('db.json')
qr = Query()


def updateDatabase():
    download_Path_allinone = "https://destiny.trade/JSON/allinone.json"
    urllib.request.urlretrieve(download_Path_allinone, "./allinone.json")
    resetDatabase()

def resetDatabase():
    #db.purge()
    #saveRelicDataToDatabase(loadDataFromJSON('./allinone.json'))
    vault_functions.saveVaultedToDatabase(loadDataFromJSON('./allinone.json'))

def loadDataFromJSON(path):
    json_data=open(path).read()
    data = json.loads(json_data)
    return data


def saveRelicDataToDatabase(data):
    relic_Data = data["relicRewards"]
    vaulted_Relics = getVaultedRelics(data)

    tier = ["Lith", "Meso", "Neo", "Axi"]
    for relics in relic_Data:
        for item in relic_Data[relics]['rewards']:
            if relic_Data[relics]['type'] in vaulted_Relics[tier.index(relic_Data[relics]['tier'])]:
                db.insert({'tier': relic_Data[relics]['tier'], 'type': relic_Data[relics]['type'], 'name': item['name'], 'rarity': item['intact']['name'], 'vaulted': True})
            else:
                db.insert({'tier': relic_Data[relics]['tier'], 'type': relic_Data[relics]['type'], 'name': item['name'], 'rarity': item['intact']['name'], 'vaulted': False})



def getListOfPartsFromItem(item):
    parts = []
    db_list = db.search((qr.name.matches(item)))
    for i in db_list:
        parts.append(i["name"])

    return parts

def getAllRelics():
    return db.all()


def getVaultedRelics(data):
    relic_data = getAllRelics()
    not_vaulted_relics = [[], [], [], []]
    vaulted_relics = relic_data
    pattern = '\w*\s\w*\sRelic'
    text = str(data)

    for match in re.findall(pattern, text):
        if match[:4] == 'Lith':
            if match[5:7] in relic_data[0]:
                not_vaulted_relics[0].append(match[5:7])
        elif match[:4] == 'Meso':
            if match[5:7] in relic_data[1]:
                not_vaulted_relics[1].append(match[5:7])
        elif match[:3] == 'Neo':
            if match[4:6] in relic_data[2]:
                not_vaulted_relics[2].append(match[4:6])
        elif match[:3] == 'Axi':
            if match[4:6] in relic_data[3]:
                not_vaulted_relics[3].append(match[4:6])

    not_vaulted_relics = [list(set(not_vaulted_relics[0])), list(set(not_vaulted_relics[1])), list(set(not_vaulted_relics[2])), list(set(not_vaulted_relics[3]))]

    count = 0
    for tier in not_vaulted_relics:
        for typ in tier:
            vaulted_relics[count].remove(typ)
        count += 1

    return vaulted_relics


