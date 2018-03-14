from tinydb import TinyDB, Query, where
import json

db = TinyDB('db.json')
qr = Query()

def loadDataFromJSON(path):
    json_data=open(path).read()
    data = json.loads(json_data)
    return data

def saveRelicDataToDatabase(data):
    relicData = data["relicRewards"]
    for relics in relicData:
        for item in relicData[relics]['rewards']:
            #print(item)
            db.insert({'table': 'relic', 'tier':relicData[relics]['tier'], 'type':relicData[relics]['type'], 'name':item['name'], 'rarity':item['intact']['name']})

def saveRelationshipsToDatabase(data):
    part = []

    for typ in data:
        for item in data[typ]:
            part = []
            for parts in item["parts"]:
                part.append(parts["name"])
            part = list(set(part))
            #print(typ)
            #print(item["name"])
            #print(part)
            db.insert({'table': typ, 'name': item['name'], 'parts': part})

def findRelicForPartsList(parts):
    for part in parts:
        print(db.search(qr.table == "relic" and qr.name.matches(part+"*")))
    #return db.search(qr.table == "relic" and qr.name == parts)



def getPartsFromItem(item):
    #print(db.search((qr.name == item) & (qr.table != "relic")))
    item_data = db.search((qr.name == item) & ((qr.table == "warframe") | (qr.table == "primary") | (qr.table == "secondary") | (qr.table == "melee") ))
    #print(item_data[0]["parts"])
    return item_data[0]["parts"]



def addPartsFromItemToWanted(item):
    parts = getPartsFromItem(item)
    for part in parts:
        db.insert({'table': "wanted", 'name': part})

def insertPartToWanted(part):
    db.insert({'table': "wanted", 'name': part})

def removePartFromWanted(part):
    db.remove(((qr.table == "wanted") & qr.name.matches(part+"*")))

#saveRelationshipsToDatabase(loadDataFromJSON("./relationship.json"))
#saveRelicDataToDatabase(loadDataFromJSON('./allinone.json'))

#print(db.search(test.table == "warframes"))
#print(db.search(test.name.matches('Ember Prime Chassis*')))
#print(db.search((qr.table == 'relic') & (where("name").matches("Nekros*"))))
#findRelicForPartsList(["Vectis Prime Stock"])
#findRelicForPartsList(getPartsFromItem("Ash Prime"))
#addPartsFromItemToWanted("Bo Prime")
#removePartFromWanted("Bo Prime Ornament")
#insertPartToWanted("Bo Prime Ornament")
print(db.search(qr.table == "wanted"))