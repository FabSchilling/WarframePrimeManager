import database_functions
import relic_functions
import re
from tinydb import TinyDB, Query
import json

db_vaulted= TinyDB('db_vault.json')
qr_vaulted = Query()

def saveVaultedToDatabase(data):
    db_vaulted.purge()
    relic_data = relic_functions.getAllRelics()
    not_vaulted_relics = [[], [], [], []]
    vaulted_relics = relic_data
    pattern = '\w*\s\w*\sRelic'
    text = str(data)

    for match in re.findall(pattern, text):
        if match[:4] == 'Lith':
            if match[5:7] in relic_data[0]:
                not_vaulted_relics[0].append(match[5:7])
        elif match[:4] == 'Meso':
            if match[5:7] in relic_data[1]:
                not_vaulted_relics[1].append(match[5:7])
        elif match[:3] == 'Neo':
            if match[4:6] in relic_data[2]:
                not_vaulted_relics[2].append(match[4:6])
        elif match[:3] == 'Axi':
            if match[4:6] in relic_data[3]:
                not_vaulted_relics[3].append(match[4:6])

    not_vaulted_relics = [list(set(not_vaulted_relics[0])), list(set(not_vaulted_relics[1])), list(set(not_vaulted_relics[2])), list(set(not_vaulted_relics[3]))]

    count = 0
    for tier in not_vaulted_relics:
        for typ in tier:
            vaulted_relics[count].remove(typ)
        count += 1

    tier1 = ['Lith', 'Meso', 'Neo', 'Axi']
    count = 0
    print(vaulted_relics)
    for tier in vaulted_relics:
        for typ in tier:
            db_vaulted.insert({'tier': tier1[count], 'type': typ})
        count += 1








#{'rotations': {'A': {'name': 'Phase Specter Blueprint', 'rarity': {'name': 'Very Common', 'value': '100.00%'}}, 'C': {'name': 'Cosmic Specter Blueprint', 'rarity': {'name': 'Very Common', 'value': '100.00%'}}, 'B': {'name': 'Force Specter Blueprint', 'rarity': {'name': 'Very Common', 'value': '100.00%'}}}, 'planet': 'Kuva Fortress', 'missionType': 'Rescue', 'extra': [], 'node': 'Garus'}
#{'rarity': {'value': '9.48%', 'name': 'Rare'}, 'name': 'Neo B2 Relic'}
