import re
import time
from time import sleep

import requests
from bs4 import BeautifulSoup

import make_database

ERROR_DATE = []
ERROR_RACE_ID = []

# ===================================================

def requests_get(url: str):
    sleep(3)
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
    for year in range(2021, 2022):
        for month in range(1, 13):
            for day in range(1, 32):
                date_txt = str(year) + str(month).zfill(2) + str(day).zfill(2)
                if date_txt > "20210400":
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
    race_name = soup.find(class_="RaceName")
    if race_name == None:
        return []
    race.append(race_name.text.strip())

    race_data_01 = soup.find(class_="RaceData01")
    race_data_01 = race_data_01.text.strip().replace("\n", "").replace(" ", "")
    race_data_01 = race_data_01.split("/")
    race += [race_data_01[1][0], race_data_01[1][1:]]
    race.append(race_data_01[2].split(":")[1])
    race.append(race_data_01[3].split(":")[1])

    race_data_02 = soup.find(class_="RaceData02")
    race_data_02 = race_data_02.text.strip().splitlines()
    for i, data in enumerate(race_data_02):
        if i == 1:
            race.append(data)
        elif i == 3:
            race.append(data +" "+ race_data_02[i+1])
        elif i == 6:
            race.append(data +" "+ race_data_02[i+1] +" "+ race_data_02[i+2])

    return [tuple(race)]

def get_race_result(soup, race_id: str) -> list:
    result = []

    table = soup.find(id="All_Result_Table")
    for i, tr in enumerate(table.find_all("tr")[1:]):
        res = [race_id+str(i+1).zfill(2), race_id]
        for j, td in enumerate(tr.find_all("td")):
            if j in [3, 6, 13]:
                href = td.find("a").get("href")
                if href[-1] == "/":
                    href = href[:-1]
                res.append(href.split("/")[-1])
            elif j == 4:
                txt = td.text.strip()
                res += [txt[0], txt[1]]
            elif j == 14:
                txt = td.text.split("(")
                if len(txt) == 1:
                    res += ["", ""]
                else:
                    res += [txt[0], txt[1][:-1]]
            else:
                res.append(td.text.strip())
        result.append(tuple(res))

    return result

def get_race_from_id(race_id: str):
    global ERROR_RACE_ID

    URL = "https://race.netkeiba.com/race/result.html?race_id=" + race_id

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
    race_id = "202107010109"
    get_race_from_id(race_id)

if __name__ == "__main__":
    main()
    #test()
    print("="*40)
    print(ERROR_DATE)
    print(ERROR_RACE_ID)
