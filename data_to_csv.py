import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import sqlite3

DBNAME = "keiba.db"

def read_races():
    conn = sqlite3.connect(DBNAME)
    cur = conn.execute("SELECT * FROM races")
    column_name = [des[0] for des in cur.description]
    races = list(map(list,cur.fetchall()))
    conn.close()
    return column_name, races

def read_results():
    conn = sqlite3.connect(DBNAME)
    cur = conn.execute("SELECT * FROM results")
    column_name = [des[0] for des in cur.description]
    results = list(map(list,cur.fetchall()))
    conn.close()
    return column_name, results

def read_pedigrees():
    conn = sqlite3.connect(DBNAME)
    cur = conn.execute("SELECT * FROM pedigrees")
    column_name = [des[0] for des in cur.description]
    pedigrees = list(map(list,cur.fetchall()))
    conn.close()
    return column_name, pedigrees

# ===================================================

def make_csv_column(race_column, result_column, pedig_column):
    csv_column = list(race_column[::])
    for i in range(18):
        num_column = [str(i+1)+"_"+c for c in result_column]
        num_column += [str(i+1)+"_"+c for c in pedig_column]
        csv_column += num_column
    return csv_column

def make_dict(lists, index:int = 0):
    res_dict = {}
    for ele in lists:
        _id = ele[index]
        if not(_id in res_dict):
            res_dict[_id] = []
        res_dict[_id].append(ele)
    return res_dict

def main():
    race_column,races = read_races()
    result_column,results = read_results()
    pedig_column,pedigrees = read_pedigrees()
    csv_column = make_csv_column(race_column, result_column, pedig_column[1:])
    results_dict = make_dict(results, index=1)
    pedig_dist = make_dict(pedigrees, index=0)
    csv_data = []
    for race in races:
        data = race[::]
        race_id = race[0]
        if not(race_id in results_dict):continue
        horses = results_dict[race_id]
        for horse in horses:
            horse_id = horse[5]
            data+=horse+pedig_dist[horse_id][0][1:]
        data += [""]*(len(csv_column) - len(data))
        csv_data.append(data)
    print(",".join(csv_column))
    for data in csv_data:
        print(",".join(data))

if __name__ == "__main__":
    main()