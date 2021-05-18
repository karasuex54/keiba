from save_data import init_db, insert_db
from get_data import netkeiba
from tqdm import tqdm

def make_date_list() -> list:
    date_list = []
    for year in range(2019, 2022):
        for month in range(1, 13):
            for day in range(1, 32):
                date_txt = str(year) + str(month).zfill(2) + str(day).zfill(2)
                if date_txt > "20210600":
                    break
                date_list.append(date_txt)
    return date_list

def main():
    init_db.init_database()
    date_list = make_date_list()
    for i,date in enumerate(date_list):
        race_list = netkeiba.get_race_id_from_date(date)
        for race_id in tqdm(race_list, desc=date):
            result = netkeiba.get_race_from_id(race_id)
            insert_db.all_insert(result)

main()