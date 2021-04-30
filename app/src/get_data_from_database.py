import re
import time
from time import sleep

import requests
from bs4 import BeautifulSoup

import make_database

ERROR_DATE = []
ERROR_RACE_ID = []

# ===================================================

def strip_function(x):
    if type(x) == str:
        return x.strip()
    else:
        return x

def time_to_seconds(time_txt: str) -> str:
    txt = time_txt.split(":")
    if len(txt) == 1:
        return time_txt
    txt = list(map(float, txt))
    txt = str(txt[0]*60 + txt[1])
    return txt

def requests_get(url: str):
    sleep(2)
    cnt = 0
    e = False
    while cnt < 5:
        try:
            r = requests.get(url, timeout=3.5)
            e = True
            break
        except:
            cnt += 1
            sleep(10)

    return r, e

def make_date_list() -> list:
    date_list = []
    for year in range(2018, 2022):
        for month in range(1, 13):
            for day in range(1, 32):
                date_txt = str(year) + str(month).zfill(2) + str(day).zfill(2)
                if date_txt > "20210500":
                    break
                date_list.append(date_txt)
    return date_list

# ===================================================

def get_race_id_from_date(date: str):
    global ERROR_DATE

    race_id_from_date = []

    URL = "https://db.netkeiba.com/race/list/" + date

    r, e = requests_get(URL)
    if e == False:
        print("Error:", date)
        ERROR_DATE.append(date)
        return []

    soup = BeautifulSoup(r.content, "lxml")

    for a in soup.find_all("a", href=re.compile("/race/20")):
        href = a.get("href")
        if href[-1] == "/":
            href = href[:-1]
        race_id_from_date.append(href.split("/")[-1])

    return race_id_from_date

def get_race_id_list():
    race_id_list = []

    date_list = make_date_list()

    for i, date in enumerate(date_list):
        print(date, len(race_id_list), "last:", len(date_list) - i)
        date_str = str(date)
        race_id_from_date = get_race_id_from_date(date_str)
        race_id_list += race_id_from_date

    return race_id_list

# ===================================================
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
    surface, distance = race_data_01[0][0],re.findall("[0-9]+",race_data_01[0])[0]
    rotation, weather = race_data_01[0][1], race_data_01[1].split(":")[1]
    condition = race_data_01[2].split(":")[1]
    race += [surface, distance, rotation, weather, condition]

    race_data_02 = race_data.find(class_="smalltxt").text
    race_data_02 = race_data_02.replace("\xa0\xa0", " ")
    race_data_02 = race_data_02.split(" ")
    place = re.findall("回.+[0-9]",race_data_02[1])[0][1:-1]
    grade,other = race_data_02[2:4]
    race += [place, grade, other]

    race = tuple(map(strip_function, race))
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
                res.append(time_to_seconds(txt))
            elif j in [14]:
                txt = td.text.split("(")
                if len(txt) == 1:
                    res += ["", ""]
                else:
                    res += [txt[0], txt[1][:-1]]
            else:
                res.append(txt)
        res = tuple(map(strip_function, res))
        result.append(res)
    return result

def get_race_from_id(race_id: str):
    global ERROR_RACE_ID

    URL = "https://db.netkeiba.com/race/" + race_id

    r, e = requests_get(URL)
    if e == False:
        print("Error:", race_id)
        ERROR_RACE_ID.append(race_id)
        return

    soup = BeautifulSoup(r.content, "lxml")

    race = get_race(soup, race_id)
    if not race:
        return
    make_database.insert_races(race)

    result = get_race_result(soup, race_id)
    make_database.insert_results(result)

# ===================================================

def main():
    make_database.make_database()

    race_id_list = get_race_id_list()
    print("get_race_id_list finished")

    for i, race_id in enumerate(race_id_list):
        print("get_race_from_id", race_id, "last:", len(race_id_list) - i)
        get_race_from_id(race_id)

def test():
    make_database.make_database()
    race_id = "201701020309"
    get_race_from_id(race_id)

if __name__ == "__main__":
    main()
    #test()
    print("="*40)
    print(ERROR_DATE)
    print(ERROR_RACE_ID)