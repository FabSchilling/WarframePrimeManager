from database_functions import db, qr


def findRelicForPartList(parts, tier = False):
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

#def sortRelics(list_of_relics):
 #   test = []
  #  tier_list = ['Lith', 'Meso', 'Neo', 'Axi']
   # for tier in tier_list:
    #    for relic in list_of_relics:
     #       if tier == relic[0]: