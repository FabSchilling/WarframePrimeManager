from database_functions import db, qr
import table_wanted_functions
from tinydb import TinyDB, Query

db_relic = TinyDB('db_relic.json')
qr_relic = Query()


def getRelicForPartList(parts, tier = False):
    relic_list = []

    if tier == False:
        for part in parts:
            relics_list_db = db.search((qr.table == "relic") & (qr.name == part))
            for relics in relics_list_db:
                relic_list.append([relics['tier'], relics['type'], relics['rarity'], relics['name']])
    else:
        for part in parts:
            relics_list_db = db.search((qr.table == "relic") & (qr.name == part) & (qr.tier == tier))
            for relics in relics_list_db:
                relic_list.append([relics['tier'], relics['type'], relics['rarity'], relics['name']])
    return relic_list




def printRelicList(relic_List, vaubose = False):
    if(vaubose):
        for relic in relic_List:
            print("Part_Name: " + relic[3] + " tier: "+ relic[0] + " type: " + relic[1] + " rarity: " + relic[2])
    else:
        for relic in relic_List:
            print("tier: "+ relic[0] + " type: " + relic[1])


def getAllRelics():
    relic_list =[]
    query_result = db.search(qr.table == "relic")
    for tier in ['Lith', 'Meso', 'Neo', 'Axi']:
        sub_list = []
        for relic in query_result:
            if relic["tier"] == tier:
                sub_list.append(relic["type"])
        sub_list = list(set(sub_list))
        sub_list = sorted(sub_list)
        relic_list.append(sub_list)
    return relic_list

def addRelicToRelicDB(tier, type):
    if isRelicInRelicDB(tier, type) == False:
        db_relic.insert({'tier': tier, 'type': type})

def removeRelicFromRelicDB(tier, type):
    db_relic.remove((qr.tier == tier) & (qr.type == type))

def isRelicInRelicDB(tier, type):
    test_query = db_relic.search((qr.tier == tier) & (qr.type == type))

    if test_query != []:
        return True
    return False

def getFilteredRelicList(tier = False):
    filter_relic_list = []
    relic_list = getRelicForPartList(table_wanted_functions.getListOfPartsFromWanted())

    print(relic_list)
    if tier != False:
        for relic in relic_list:
            if ((relic[0] == tier) & (isRelicInRelicDB(relic[0], relic[1]))):
                filter_relic_list.append(relic)

    else:
        for relic in relic_list:
            print(relic)
            if isRelicInRelicDB(relic[0], relic[1]):
                filter_relic_list.append(relic)

    return filter_relic_list

