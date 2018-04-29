import database_functions
import relic_functions
from tinydb import TinyDB, Query



db_wanted = TinyDB('db_wanted.json')
qr_wanted = Query()

def addPartsFromItemToWanted(item):
    print(item)
    parts = database_functions.getListOfPartsFromItem(item)
    for part in parts:
        insertPartToWanted(part)


def insertPartToWanted(part):
    if(db_wanted.search(qr_wanted.name == part) == []):
        db_wanted.insert({'item': part.split(' Prime')[0], 'name': part})


def removePartFromWanted(part):
    db_wanted.remove(qr_wanted.name == part)


def getListOfPartsFromWanted():
    wanted_list = []
    wanted_list_db = db_wanted.all()
    for wanted_part in wanted_list_db:
        wanted_list.append(wanted_part['name'])
    return wanted_list

def getListOfRelicsForListOfParts(parts):
    relic_list = []
    for part in parts:
        relics_list_db = relic_functions.getRelicForPartList(parts)
        for relics in relics_list_db:
            relic_list.append([relics['tier'], relics['type'], relics['rarity'], relics['name']])
    return relic_list

def getListOfItem():
    item_list = []
    wanted_list_db = db_wanted.all()
    for part in wanted_list_db:
        item_list.append(part['item'])
    return set(item_list)

def getListOfPartsOfItem(item):
    part_list = []
    part_list_db = db_wanted.search(qr_wanted.item == item)
    print(part_list_db)
    for parts in part_list_db:
        part_list.append(parts['name'])

    print(part_list)
    return part_list
