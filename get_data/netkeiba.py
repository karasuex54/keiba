import re
from bs4 import BeautifulSoup
from get_data import common as cm
import sqlite3

# ===================================================

# "  test  " => "test"
def strip_function(x):
    if type(x) == str:return x.strip()
    else:return x

# ===================================================
def get_race_id_from_date(date: str):
    race_id_from_date = []
    URL = "https://db.netkeiba.com/race/list/" + date
    r, e = cm.custom_get(URL)
    if e == False:
        print("Error:", date)
        return []
    soup = BeautifulSoup(r.content, "lxml")
    for a in soup.find_all("a", href=re.compile("/race/20")):
        href = a.get("href")
        if href[-1] == "/":
            href = href[:-1]
        race_id_from_date.append(href.split("/")[-1])
    return race_id_from_date

# ===================================================
def get_horse_pedigree(horse_id: str):
    pedig = [horse_id]
    URL = "https://db.netkeiba.com/horse/" + horse_id
    r, e = cm.custom_get(URL)
    if e == False:
        print("Error:", horse_id)
        return []
    soup = BeautifulSoup(r.content, "lxml")
    table = soup.find(class_="blood_table")
    pedig += [a.get("href").split("/")[-2] for a in table.find_all("a")]
    return pedig

def get_race(soup, race_id: str) -> list:
    race = [race_id]
    race_data = soup.find(class_="mainrace_data")
    race_name = race_data.find("h1").text.strip()
    race.append(race_name)
    if race_data == None:
        return []
    race_data_01 = race_data.find("dd").find("span").text
    race_data_01 = race_data_01.replace("\xa0", "").replace(" ", "")
    race_data_01 = race_data_01.split("/")
    surface, distance = race_data_01[0][0],re.findall("[0-9]+",race_data_01[0])[-1]
    rotation, weather = race_data_01[0][1], race_data_01[1].split(":")[1]
    if not (rotation in ["直","右","左"]):rotation=""
    condition = race_data_01[2].replace("芝:","").replace("ダート:","")
    race += [surface, distance, rotation, weather, condition]
    race_data_02 = race_data.find(class_="smalltxt").text
    race_data_02 = race_data_02.replace("\xa0\xa0", " ").replace("  "," ")
    race_data_02 = race_data_02.split(" ")
    place = re.findall("回.+[0-9]",race_data_02[1])[0][1:3]
    grade,other = race_data_02[2:4]
    race += [place, grade, other]
    return [race]

def get_race_result(soup, race_id: str) -> list:
    result = []
    table = soup.find(class_="race_table_01")
    for i, tr in enumerate(table.find_all("tr")[1:]):
        res = [race_id+str(i+1).zfill(2), race_id]
        for j, td in enumerate(tr.find_all("td")):
            txt = td.text.strip()
            if j in [9, 15, 16, 17, 19, 20]:
                continue
            elif j in [3, 6, 18]:
                href = td.find("a").get("href")
                if href[-1] == "/":
                    href = href[:-1]
                res.append(href.split("/")[-1])
            elif j in [4]:
                res += [txt[0], txt[1:]]
            elif j in [7]:
                res.append(cm.time_to_seconds(txt))
            elif j in [14]:
                txt = td.text.split("(")
                if len(txt) == 1:
                    res += ["", ""]
                else:
                    res += [txt[0], txt[1][:-1]]
            else:
                res.append(txt)
        result.append(res)
    return result

def get_race_from_id(race_id: str):
    URL = "https://db.netkeiba.com/race/" + race_id
    r, e = cm.custom_get(URL)
    if e == False:
        print("Error:", race_id)
        return
    soup = BeautifulSoup(r.content, "lxml")
    race_info = get_race(soup, race_id)
    if not race_info:
        return [None]
    result_info = get_race_result(soup, race_id)
    pedig_info = []
    for result in result_info:
        horse_id = result[5]
        if not(is_horse_pedigrees(horse_id)):
            pedig_info.append(get_horse_pedigree(horse_id))
    return [race_info, result_info, pedig_info]

def is_horse_pedigrees(horse_id)-> list:
    DBNAME = "keiba.db"
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()
    cur.execute("""
    SELECT * From pedigrees WHERE id = ?
    """, (horse_id, ))
    res = cur.fetchall()
    conn.commit()
    conn.close()
    return res != []