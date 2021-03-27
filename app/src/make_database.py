import sqlite3

def make_database():
    #path = "../"
    DB_name = "keiba.db"
    conn = sqlite3.connect(DB_name)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS race (
        id TEXT PRIMARY KEY,
        name TEXT,
        surface TEXT,
        distance TEXT,
        weather TEXT,
        condition TEXT,
        place TEXT,
        grade TEXT,
        other TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id TEXT PRIMARY KEY,
        race_id TEXT,
        ord TEXT,
        post TEXT,
        number TEXT,
        horse_id TEXT,
        sex TEXT,
        age TEXT,
        penalty TEXT,
        jockey_id TEXT,
        finish TEXT,
        margin TEXT,
        popular TEXT,
        odds TEXT,
        g_3f TEXT,
        corner TEXT,
        stable_id TEXT,
        weight TEXT
    )""")

    conn.commit()
    conn.close()

def insert_race(race):
    DB_name = "keiba.db"
    conn = sqlite3.connect(DB_name)
    cur = conn.cursor()

    cur.executemany("""
    REPLACE INTO race (
        id, name, surface, distance, weather, condition, place, grade, other
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, race)

    conn.commit()
    conn.close()

def insert_results(result):
    DB_name = "keiba.db"
    conn = sqlite3.connect(DB_name)
    cur = conn.cursor()

    cur.executemany("""
    REPLACE INTO results (
        id, race_id, ord, post, number, horse_id, sex, age,
        penalty, jockey_id, finish, margin, popular, odds, g_3f,
        corner, stable_id, weight
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, result)

    conn.commit()
    conn.close()