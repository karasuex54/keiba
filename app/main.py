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

def use_database():
    pass

# ===================================================

def test():
    results = od.get_columns()
    for r in results:
        print(r)

if __name__ == "__main__":
    test()