import json

from tinydb import TinyDB, Query


def loadDataFromJSON(path):
    json_data=open(path).read()
    data = json.loads(json_data)
    return data


def saveRelicDataToDatabase(data):
    relicData = data["relicRewards"]
    for relics in relicData:
        for item in relicData[relics]['rewards']:
            db.insert({'table': 'relic', 'tier':relicData[relics]['tier'], 'type':relicData[relics]['type'], 'name':item['name'], 'rarity':item['intact']['name']})


def saveRelationshipsToDatabase(data):
    for typ in data:
        for item in data[typ]:
            part1, part2, part3, part4, part5, part6, part7 = [], [], [], [], [], [], []
            partNumber = len(item["parts"])
            if (partNumber > 0):
                part1 = item["parts"][0]
                if(partNumber > 1):
                    part2 = item["parts"][1]
                    if (partNumber > 2):
                        part3 = item["parts"][2]
                        if (partNumber > 3):
                            part4 = item["parts"][3]
                            if (partNumber > 4):
                                part5 = item["parts"][4]
                                if (partNumber > 5):
                                    part6 = item["parts"][5]
                                    if (partNumber > 6):
                                        part7 = item["parts"][6]

            db.insert({'table': typ, 'name': item['name'], 'part1': part1, 'part2': part2, 'part3': part3, 'part4': part4, 'part5': part5, 'part6': part6, 'part7': part7})


def resetDatabase():
    db.purge()
    saveRelationshipsToDatabase(loadDataFromJSON("./relationship.json"))
    saveRelicDataToDatabase(loadDataFromJSON('./allinone.json'))


db = TinyDB('db.json')
qr = Query()