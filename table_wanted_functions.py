from other import getListOfPartsFromItem
import relic_functions
from tinydb import TinyDB, Query



db_wanted = TinyDB('db_wanted.json')
qr_wanted = Query()

def addPartsFromItemToWanted(item):
    print(item)
    parts = getListOfPartsFromItem(item)
    for part in parts:
        insertPartToWanted(part)


def insertPartToWanted(part):
    if(db_wanted.search((qr_wanted.table == "wanted") & (qr_wanted.name == part)) == []):

        relic_list = relic_functions.findRelicForPartList([part])
        for relic in relic_list:
            print(relic)
            db_wanted.insert({'table': "relic", 'tier': relic[0], 'type': relic[1], 'rarity': relic[2], 'name': part})
        db_wanted.insert({'table': "wanted", 'name': part})


def removePartFromWanted(part):
    db_wanted.remove(((qr_wanted.table == "wanted") & (qr_wanted.name == part)))


def getListOfPartsFromWanted():
    wanted_list = []
    wanted_list_db = db_wanted.search(qr_wanted.table == "wanted")
    for wanted_part in wanted_list_db:
        wanted_list.append(wanted_part['name'])
    #print(wanted_list)
    return wanted_list

def getListOfPartsFromWanted():
    wanted_list = []
    wanted_list_db = db_wanted.search(qr_wanted.table == "wanted")
    for wanted_part in wanted_list_db:
        wanted_list.append(wanted_part['name'])
    #print(wanted_list)
    return wanted_list

def getListOfRelicsForListOfParts(parts):
    relic_list = []
    print(parts)
    for part in parts:
        #print(part)
        relics_list_db = db_wanted.search((qr_wanted.table == "relic") & (qr_wanted.name == part))
        #print(relics_list_db)
        for relics in relics_list_db:
            print(relics)
            relic_list.append([relics['tier'], relics['type'], relics['rarity'], relics['name']])
    return relic_list