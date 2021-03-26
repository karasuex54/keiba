import sqlite3

def make_database():
    #path = "../"
    DB_name = "keiba.db"
    conn = sqlite3.connect(DB_name)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS horse_in_race (
        id INTEGER PRIMARY KEY,
        race_id INTEGER,
        ord TEXT,
        post_position TEXT,
        gate TEXT,
        horse_name TEXT,
        sex_age TEXT,
        saddle_weight TEXT,
        jockey TEXT,
        finish TEXT,
        margin TEXT,
        section_position TEXT,
        g_3f TEXT,
        win_odds TEXT,
        popular TEXT,
        horse_weight TEXT,
        trainer TEXT,
        owner TEXT,
        prize_money TEXT DEFAULT "0"
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
        horse_name,
        sex_age,
        saddle_weight,
        jockey,
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