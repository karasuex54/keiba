import sqlite3

DBNAME = "keiba.db"

def insert_races(race):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()
    cur.executemany("""
    REPLACE INTO races (
        id, name, surface, distance, rotation, weather, condition, place, grade, other
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, race)
    conn.commit()
    conn.close()

def insert_results(result):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()
    cur.executemany("""
    REPLACE INTO results (
        id, race_id, ord, post, number, horse_id, sex, age,
        penalty, jockey_id, finish, margin, corner, g_3f,
        odds, popular, weight, weight_dif, stable_id
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, result)
    conn.commit()
    conn.close()

def insert_pedigrees(pedig):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()
    cur.executemany("""
    REPLACE INTO pedigrees (
        id, b_ml, b_ml_ml, b_ml_fml,
        b_fml, b_fml_ml, b_fml_fml
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, pedig)
    conn.commit()
    conn.close()

def all_insert(res):
    race_info, result_info, pedig_info = res
    insert_races(race_info)
    insert_results(result_info)
    insert_pedigrees(pedig_info)