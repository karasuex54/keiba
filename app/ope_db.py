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
    N_horse = 18
