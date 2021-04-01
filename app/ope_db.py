import sqlite3

# ===================================================

def list_to_columns(column_list:list = []):
    if column_list == []:
        return "*"
    else:
        pass

# ===================================================

def read_races():
    races = []

    path = "./src/"
    DB_name = "keiba.db"
    conn = sqlite3.connect(path + DB_name)
    cur = conn.cursor()

    cur.execute("""
    SELECT * FROM races
    """)

    races = cur.fetchall()

    conn.close()

    return races

def read_results():
    results = []

    path = "./src/"
    DB_name = "keiba.db"
    conn = sqlite3.connect(path + DB_name)
    cur = conn.cursor()

    cur.execute("""
    SELECT * FROM results
    """)

    results = cur.fetchall()

    conn.close()

    return results

# ===================================================

def get_races_columns():
    name = []

    path = "./src/"
    DB_name = "keiba.db"
    conn = sqlite3.connect(path + DB_name)
    cur = conn.execute("SELECT * FROM races")

    name = [des[0] for des in cur.description]

    conn.close()

    return name

def get_results_columns():
    name = []

    path = "./src/"
    DB_name = "keiba.db"
    conn = sqlite3.connect(path + DB_name)
    cur = conn.execute("SELECT * FROM results")

    name = [des[0] for des in cur.description]

    conn.close()

    return name

def get_columns(N_hourse:int = 18):
    res = get_races_columns()
    results_columns = get_results_columns()
    for i in range(N_hourse):
        res += [str(i+1) + "_" +col for col in results_columns]
    return res

# ===================================================

def use_database():
    res = []

    columns = tuple(get_columns()) + tuple(["top_number"])
    N = len(columns)
    races = read_races()
    results = read_results()

    results_index = 0
    res.append(columns)
    for race in races:
        r = race
        top_number = "0"
        race_id = race[0]
        while results_index < len(results):
            if race_id != results[results_index][1]:
                break
            r += results[results_index]
            if top_number == "0":
                top_number = results[results_index][4]
            results_index += 1
        r += tuple([-1 for i in range(len(columns) - 1 - len(r))] + [top_number])
        res.append(r)

    return res