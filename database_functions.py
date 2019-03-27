import json
import re
from urllib.request import Request, urlopen

from tinydb import TinyDB, Query

db = TinyDB('db.json')
qr = Query()


def downloadRawDatabase():
    req = Request('https://drops.warframestat.us/data/all.json', headers={'User-Agent': 'Mozilla/5.0'})
    database = urlopen(req).read().decode('utf-8')
    return database

def updateDatabase():
    rawData = downloadRawDatabase()
    db.purge()
    data = loadDataFromJSON(rawData)
    saveRelicDataToDatabase(data)


def loadDataFromJSON(rawData):
    data = json.loads(rawData)
    return data


def saveRelicDataToDatabase(data):
    relic_Data = data["relics"]
    tier_list = ["Lith", "Meso", "Neo", "Axi"]

    for relics in relic_Data:
        #print(relics)
        if(relics['state'] == "Intact"):
            for rewards in relics['rewards']:
                db.insert({'tier': relics['tier'], 'relicName': relics['relicName'], 'name': rewards['itemName'], 'rarity': rewards['rarity'], 'vaulted': False})

    vaulted_Relics = getVaultedRelicsFromData(data)
    for tier in tier_list:
        print(tier)
        for relic_type in vaulted_Relics[tier_list.index(tier)]:
            print(relic_type)
            db.update({'vaulted': True}, ((qr.tier == tier) & (qr.relicName == relic_type)))


def getListOfPartsFromItem(item):
    parts = []
    db_list = db.search((qr.name.matches(item)))
    for i in db_list:
        parts.append(i["name"])

    return parts


def getVaultedRelicsFromData(data):
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
        for relic in tier:
            vaulted_relics[count].remove(relic)
        count += 1
    return vaulted_relics


def getAllRelics():
    relic_list =[]
    query_result = db.all()
    for tier in ['Lith', 'Meso', 'Neo', 'Axi']:
        sub_list = []
        for relic in query_result:
            if relic["tier"] == tier:
                sub_list.append(relic["relicName"])
        sub_list = list(set(sub_list))
        sub_list = sorted(sub_list)
        relic_list.append(sub_list)
    return relic_list

def isRelicVaulted(tier, relic):
    relic = db.get((qr.tier == tier) & (qr.relicName == relic))
    return relic["vaulted"]
