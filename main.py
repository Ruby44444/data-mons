import urllib3
import re
import pyinputplus as pyip

def getData():
    date = input("Date ? :")
    format = input("Format ? :")
    if format == 'gen9ou' or format == 'gen9doublesou':
        rank = pyip.inputMenu(["0", "1500", "1695", "1825"])
    else:
        rank = pyip.inputMenu(["0", "1500", "1630", "1760"])



    link = 'https://www.smogon.com/stats/' + date + '/moveset/' + format + '-' + rank + '.txt'

    file = urllib3.PoolManager().request("GET", link)

    return file

def getMon(mon):
    count = -1
    regex = re.sub(' [|] {} *[|]'.format(mon))

    raw_usage = 0
    abilities = []
    items = []
    spreads = []
    moves = []
    tera = []
    teammates = []
    checks_counters = []
    
    lis = [raw_usage, abilities, items, spreads, moves, tera, teammates, checks_counters]

    file_content = getData()  # Fetch data

    if not file_content:
        return  

    # Split content into lines
    lines = file_content.split("\n")

    # Search for Pokémon names in the file
    for line in lines:
        if count < 9: #garde compte du nombre de la section actuelle
            check = bool(re.search(regex, line))
            if check or (count > 0):
                if check or line == "+----------------------------------------+":
                    count += 1
                match count:
                    case 1: #Nombre d'utilisations du mon
                        if bool(re.search(r" [|] Raw count: \d* *[|] ", line)):
                            raw_usage = int(line.split().remove('%')[3])
                    case 2: #Pourcentage de chaque talent
                        if not bool(re.search(r" [|] Abilities *[|] ", line)):
                            ability_index = re.search(r" [|] [a-zA-Z -]* *[|] ", line)
                            ability = line[ability_index[0]]
                            abilities.append((ability, line.split().remove('%')[-2]))


                

                

getMon()