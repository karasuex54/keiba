import ope_db as od

# ===================================================

def read_races():
    races = od.read_races()
    return races

def read_results():
    results = od.read_results()
    return results

# ===================================================

def get_races_columns():
    names = od.get_races_columns()
    return names

def get_results_columns():
    names = od.get_results_columns()
    return names

# ===================================================

def use_database(race_id:str = ""):
    db = od.use_database(race_id)
    return db

# ===================================================

def main():
    db = use_database("202109021211")
    for d in db:
        print(",".join([str(i) for i in d]))

def test():
    pass

if __name__ == "__main__":
    main()