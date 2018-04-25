from database_functions import db, qr




def getListOfPartsFromItem(item):
    parts = []
    db_list = db.search((qr.name.matches(item)))
    for i in db_list:
        parts.append(i["name"])

    return parts
