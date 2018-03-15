from database_functions import db, qr
from relic_functions import findRelicForPartList, printRelicList
from table_wanted_functions import addPartsFromItemToWanted, getListOfPartsFromWanted


def getListOfPartsFromItem(item):
    parts = []
    item_data = db.search((qr.name == item) & ((qr.table == "warframe") | (qr.table == "primary") | (
                qr.table == "secondary") | (qr.table == "melee")))

    if (item_data[0]["part1"] != []):
        parts.append(item_data[0]["part1"]["name"])
        if (item_data[0]["part2"] != []):
            parts.append(item_data[0]["part2"]["name"])
            if (item_data[0]["part3"] != []):
                parts.append(item_data[0]["part3"]["name"])
                if (item_data[0]["part4"] != []):
                    parts.append(item_data[0]["part4"]["name"])
                    if (item_data[0]["part5"] != []):
                        parts.append(item_data[0]["part5"]["name"])
                        if (item_data[0]["part6"] != []):
                            parts.append(item_data[0]["part6"]["name"])
                            if (item_data[0]["part7"] != []):
                                parts.append(item_data[0]["part7"]["name"])
    print(parts)
    return(parts)


def searchPartOrItemByName(name):
    return(db.search((qr.name.matches("\w*\s?&?\s?\w*\s?\w*\s?\w*" + name + "\w*\s?&?\s?\w*\s?\w*\s?\w*")) &
                     ((qr.table == "warframe") | (qr.table == "primary") |
                      (qr.table == "secondary") | (qr.table == "melee"))))


#print(db.search(test.table == "warframes"))
#print(db.search(test.name.matches('Ember Prime Chassis*')))
#print(db.search((qr.table == 'relic') & (where("name").matches("Nekros*"))))
#findRelicForPartList(["Vectis Prime Stock"])
#findRelicForPartList(getListOfPartsFromItem("Ash Prime"))
addPartsFromItemToWanted("Ash Prime")
#addPartsFromItemToWanted("Akbronco Prime")
#removePartFromWanted("Ankyros Prime Gauntlet")
#insertPartToWanted("Bo Prime Ornament")
#print(db.search(qr.table == "wanted"))
#searchPartOrItemByName("Ash")
#getListOfPartsFromItem("Ash Prime")
#print(searchPartOrItemByName("Ash Prime"))
#getListOfPartsFromWanted()
printRelicList(findRelicForPartList(getListOfPartsFromWanted()))

#database_functions.resetDatabase()
