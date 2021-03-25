import time
import re

import requests
from bs4 import BeautifulSoup

# ===================================================

def get_race_url_from_date(date: str):
    URL = "https://db.netkeiba.com/race/list/" + date

    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "lxml")

    for a in soup.find_all("a", href=re.compile("/race/20")):
        print(a)

def get_race_lists():
    for date in range(20210301, 20210330):
        date_str = str(date)
        get_race_url_from_date(date_str)
        time.sleep(3)

# ===================================================

def get_race_detail(race_url: str):
    pass

# ===================================================

def main():
    get_race_lists()

if __name__ == "__main__":
    main()