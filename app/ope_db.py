import sqlite3

def read_races():
    res = []

    path = "./src/"
    DB_name = "keiba.db"
    conn = sqlite3.connect(path + DB_name)
    cur = conn.cursor()

    cur.execute("""
    SELECT * FROM races
    """)

    res = cur.fetchall()

    conn.close()

    return res
