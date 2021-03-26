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
        stable TEXT,
        weight TEXT
    )""")

    conn.commit()
    conn.close()

def insert_horse_in_race_details(horse_in_race_details):
    DB_name = "keiba.db"
    conn = sqlite3.connect(DB_name)
    cur = conn.cursor()

    cur.executemany("""
    REPLACE INTO horse_in_race (
        id,
        race_id,
        ord,
        post_position,
        gate,
        horse_id,
        sex_age,
        saddle_weight,
        jockey_id,
        finish,
        margin,
        section_position,
        g_3f,
        win_odds,
        popular,
        horse_weight,
        trainer,
        owner,
        prize_money
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
    )""", horse_in_race_details)

    conn.commit()
    conn.close()