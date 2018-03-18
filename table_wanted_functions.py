from database_functions import db, qr
from other import getListOfPartsFromItem


def addPartsFromItemToWanted(item):
    #print(item)
    parts = getListOfPartsFromItem(item)
    for part in parts:
        insertPartToWanted(part)


def insertPartToWanted(part):
    if(db.search((qr.table == "wanted") & (qr.name == part)) == []):
        db.insert({'table': "wanted", 'name': part})


def removePartFromWanted(part):
    db.remove(((qr.table == "wanted") & (qr.name == part)))


def getListOfPartsFromWanted():
    wanted_list = []
    wanted_list_db = db.search(qr.table == "wanted")
    for wanted_part in wanted_list_db:
        wanted_list.append(wanted_part['name'])
    #print(wanted_list)
    return wanted_list