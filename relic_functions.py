import database_functions
import table_wanted_functions
from tinydb import TinyDB, Query

db_relic = TinyDB('db_relic.json')
qr_relic = Query()


def getRelicForPartList(parts, tier = False):
    relic_list = []

    if tier == False:
        for part in parts:
            relics_list_db = database_functions.db.search(database_functions.qr.name == part)
            for relics in relics_list_db:
                relic_list.append([relics['tier'], relics['type'], relics['rarity'], relics['name']])
    else:
        for part in parts:
            relics_list_db = database_functions.db.search((database_functions.name == part) & (database_functions.qr.tier == tier))
            for relics in relics_list_db:
                relic_list.append([relics['tier'], relics['type'], relics['rarity'], relics['name']])
    return relic_list


def addRelicToRelicDB(tier, relic_type):
    if isRelicInRelicDB(tier, relic_type) == False:
        db_relic.insert({'tier': tier, 'type': relic_type})

def removeRelicFromRelicDB(tier, relic_type):
    db_relic.remove((database_functions.qr.tier == tier) & (database_functions.qr.type == relic_type))

def isRelicInRelicDB(tier, relic_type):
    test_query = db_relic.search((database_functions.qr.tier == tier) & (database_functions.qr.type == relic_type))

    if test_query != []:
        return True
    return False

def getFilteredRelicList(tier = False):
    filter_relic_list = []
    relic_list = getRelicForPartList(table_wanted_functions.getListOfPartsFromWanted())

    if tier != False:
        for relic in relic_list:
            if ((relic[0] == tier) & (isRelicInRelicDB(relic[0], relic[1]))):
                filter_relic_list.append(relic)
        filter_relic_list = sorted(filter_relic_list)
    else:
        for tier in ['Lith', 'Meso', 'Neo', 'Axi']:
            sub_list = []

            for relic in relic_list:
                if ((relic[0] == tier) & (isRelicInRelicDB(relic[0], relic[1]))):
                    sub_list.append(relic)
            filter_relic_list.append(sorted(sub_list))
        tmp = []
        for i in filter_relic_list:
            for j in i:
                tmp.append(j)
        filter_relic_list = tmp




    return filter_relic_list

