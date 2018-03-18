import json

from tinydb import TinyDB, Query


def loadDataFromJSON(path):
    json_data=open(path).read()
    data = json.loads(json_data)
    return data


def saveRelicDataToDatabase(data):
    relic_Data = data["relicRewards"]
    for relics in relic_Data:
        for item in relic_Data[relics]['rewards']:
            db.insert({'table': 'relic', 'tier':relic_Data[relics]['tier'], 'type':relic_Data[relics]['type'], 'name':item['name'], 'rarity':item['intact']['name']})


def saveRelationshipsToDatabase(data):
    for typ in data:
        for item in data[typ]:
            part1, part2, part3, part4, part5, part6, part7 = [], [], [], [], [], [], []
            part_Number = len(item["parts"])
            if (part_Number > 0):
                part1 = item["parts"][0]['name']
                if(part_Number > 1):
                    part2 = item["parts"][1]['name']
                    if (part_Number > 2):
                        part3 = item["parts"][2]['name']
                        if (part_Number > 3):
                            part4 = item["parts"][3]['name']
                            if (part_Number > 4):
                                part5 = item["parts"][4]['name']
                                if (part_Number > 5):
                                    part6 = item["parts"][5]['name']
                                    if (part_Number > 6):
                                        part7 = item["parts"][6]['name']
            #print(part1)
            db.insert({'table': typ, 'name': item['name'], 'part1': part1, 'part2': part2, 'part3': part3, 'part4': part4, 'part5': part5, 'part6': part6, 'part7': part7})


def resetDatabase():
    db.purge()
    saveRelationshipsToDatabase(loadDataFromJSON("./relationship.json"))
    saveRelicDataToDatabase(loadDataFromJSON('./allinone.json'))


db = TinyDB('db.json')
qr = Query()