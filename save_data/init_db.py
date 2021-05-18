import sqlite3

DBNAME = "keiba.db"

# ===================================================

def init_database():
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS races (
        id TEXT PRIMARY KEY,
        name TEXT,
        surface TEXT,
        distance TEXT,
        rotation TEXT,
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
        corner TEXT,
        g_3f TEXT,
        odds TEXT,
        popular TEXT,
        weight TEXT,
        weight_dif TEXT,
        stable_id TEXT
    )""")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS pedigrees (
        id TEXT PRIMARY KEY,
        b_ml TEXT,
        b_ml_ml TEXT,
        b_ml_fml TEXT,
        b_fml TEXT,
        b_fml_ml TEXT,
        b_fml_fml TEXT
    )
    """)
    conn.commit()
    conn.close()
