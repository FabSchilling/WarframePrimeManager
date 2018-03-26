from database_functions import db, qr


def getListOfPartsFromItem(item):
    parts = []
    if (item != []):
        item_data = db.search((qr.name == item) & ((qr.table == "warframe") | (qr.table == "primary") | (
                    qr.table == "secondary") | (qr.table == "melee") | (qr.table == "companions") | (qr.table == "archwings")))
        if(item_data != []):
            if (item_data[0]["part1"] != []):
                parts.append(item_data[0]["part1"])
                if (item_data[0]["part2"] != []):
                    parts.append(item_data[0]["part2"])
                    if (item_data[0]["part3"] != []):
                        parts.append(item_data[0]["part3"])
                        if (item_data[0]["part4"] != []):
                            parts.append(item_data[0]["part4"])
                            if (item_data[0]["part5"] != []):
                                parts.append(item_data[0]["part5"])
                                if (item_data[0]["part6"] != []):
                                    parts.append(item_data[0]["part6"])
                                    if (item_data[0]["part7"] != []):
                                        parts.append(item_data[0]["part7"])
    return(parts)

'''
def searchPartOrItemByName(name):
    db_list = db.search((qr.name.matches("\w*\s?&?\s?\w*\s?\w*\s?\w*" + name + "\w*\s?&?\s?\w*\s?\w*\s?\w*"))                          &
                        ((qr.table == "warframe") | (qr.table == "primary") | (qr.table == "secondary") | (qr.table == "melee")))

    
    print(db_list)
    for items in db_list:
        for k in items:
            print(items[k])

    return db_list
'''