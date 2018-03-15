from database_functions import db, qr


def findRelicForPartList(parts):
    relics_list = []
    for part in parts:
        relics_list_db = db.search((qr.table == "relic") & (qr.name == part))
        for relics in relics_list_db:
            relics_list.append([relics['tier'], relics['type'], relics['rarity'], relics['name']])
    return relics_list


def printRelicList(relicList, vaubose = False, sort = False):
    if(vaubose):
        for relic in relicList:
            print("Part_Name: " + relic[3] + " tier: "+ relic[0] + " type: " + relic[1] + " rarity: " + relic[2])
    else:
        for relic in relicList:
            print("tier: "+ relic[0] + " type: " + relic[1])