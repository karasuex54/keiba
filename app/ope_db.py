import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
import sqlite3

import src.get_data_from_database as gdfd

DBPATH = "./src/keiba.db"

# ===================================================

def list_to_columns(column_list:list = []):
    if column_list == []:
        return "*"
    else:
        pass

# ===================================================
def read_races():
    races = []
    conn = sqlite3.connect(DBPATH)
    cur = conn.cursor()
    cur.execute("""
    SELECT * FROM races
    """)
    races = cur.fetchall()
    conn.close()
    return races

def read_results()-> dict:
    results = []
    results_dict = {}
    conn = sqlite3.connect(DBPATH)
    cur = conn.cursor()
    cur.execute("""
    SELECT * FROM results
    """)
    results = cur.fetchall()
    conn.close()
    for result in results:
        race_id = result[1]
        if not (race_id in results_dict):
            results_dict[race_id] = []
        results_dict[race_id].append(list(result))
    return results_dict

def read_pedigrees()-> dict:
    pedigrees = []
    pedigrees_dict = {}
    conn = sqlite3.connect(DBPATH)
    cur = conn.cursor()
    cur.execute("""
    SELECT * FROM pedigrees
    """)
    pedigrees = cur.fetchall()
    conn.close()
    for pedigree in pedigrees:
        pedigrees_dict[pedigree[0]] = list(pedigree[1:])
    return pedigrees_dict
# ===================================================
def get_races_columns():
    name = []
    conn = sqlite3.connect(DBPATH)
    cur = conn.execute("SELECT * FROM races")
    name = [des[0] for des in cur.description]
    conn.close()
    return name

def get_results_columns():
    name = []
    conn = sqlite3.connect(DBPATH)
    cur = conn.execute("SELECT * FROM results")
    name = [des[0] for des in cur.description]
    conn.close()
    return name

def get_pedigrees_columns():
    name = []
    conn = sqlite3.connect(DBPATH)
    cur = conn.execute("SELECT * FROM pedigrees")
    name = [des[0] for des in cur.description]
    conn.close()
    return name

def get_columns(N_hourse:int = 18):
    res = get_races_columns()
    results_columns = get_results_columns()
    pedigrees_columns = get_pedigrees_columns()
    for i in range(N_hourse):
        res += [str(i+1) + "_" +col for col in results_columns]
        res += [str(i+1) + "_" +col for col in pedigrees_columns[1:]]
    return res

# ===================================================

def use_database(race_id:str = ""):
    if race_id == "":
        print("please input race id")
        return
    res = []
    columns = tuple(get_columns()) + tuple(["top_number"])
    N = len(columns)
    pedigrees = read_pedigrees()
    races = read_races()
    results = read_results()
    res.append(columns)
    for race in races:
        r = race
        result = results[r[0]]
        top_number = result[0][4]
        for i in result:
            r += tuple(i)+tuple(pedigrees[i[5]])
        r += tuple([-1 for i in range(N - 1 - len(r))] + [top_number])
        res.append(r)

    race, hors = gdfd.get_target(race_id)
    for i in hors:
        race += i+pedigrees[i[5]]
    race += [-1 for i in range(N - len(race))]
    res.append(race)
    return res

# ===================================================