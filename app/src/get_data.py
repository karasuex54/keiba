import time
import re

import make_database

import requests
from bs4 import BeautifulSoup

# ===================================================

def get_race_id_from_date(date: str):
    URL = "https://db.netkeiba.com/race/list/" + date

    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "lxml")

    for a in soup.find_all("a", href=re.compile("/race/20")):
        title = a.get("title")
        href = a.get("href")
        print(title, href.split("/")[2])

def get_race_id_lists():
    for date in range(20210306, 20210307):
        date_str = str(date)
        get_race_id_from_date(date_str)
        time.sleep(3)

# ===================================================

def get_race_info(soup, race_id: str) -> list:
    race_info = [race_id]

    racedata = soup.find(class_="racedata fc")
    race_title = racedata.find("h1").text
    race_detail = racedata.find("span").text.replace(u'\xa0', u'')
    race_smalltxt = soup.find(class_="smalltxt").text.replace(u'\xa0', u'')

    race_detail = race_detail.split("/")
    for i, s in enumerate(race_detail[:-1]):
        if i == 0:
            race_info.append(s[:2])
            race_info.append(s.replace(" ", "")[2:])
        else:
            race_info.append(s.replace(" ", "").split(":")[-1])
    print(race_info)
    return race_info

def get_race_result(soup, race_id: str) -> list:
    table = soup.find(class_="race_table_01 nk_tb_common")
    detail_list = []
    for i, tr in enumerate(table.find_all("tr")[1:]):
        td = tr.find_all("td")
        detail = []
        for j, s in enumerate(td):
            if j in [9, 15, 16, 17]:
                continue
            if j in [3, 6]:
                a = s.find("a")
                detail.append(a.get("href").split("/")[2])
            else:
                detail.append(s.text.replace("\n", ""))
        detail = [race_id + str(i+1).zfill(2), race_id] + detail
        detail_list.append(detail)
    return detail_list

def get_race_from_id(race_id: str):
    URL = "https://db.netkeiba.com/race/" + race_id

    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "lxml")

    race_info = get_race_info(soup, race_id)
    horse_in_race_details = get_race_result(soup, race_id)
    make_database.insert_horse_in_race_details(horse_in_race_details)

# ===================================================

def main():
    make_database.make_database()

    #get_race_id_lists()
    get_race_from_id("202109010711")

if __name__ == "__main__":
    main()