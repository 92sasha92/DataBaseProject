
def insert_name_to_db(table_name, obj_name, col_name, conn):
    x = conn.cursor()
    is_exist = x.execute("SELECT * FROM "+table_name+" WHERE "+col_name+"='%s'" % obj_name)
    if is_exist == 0:
        query = "INSERT INTO "+table_name+" VALUES (%s)"
        x.execute(query, (obj_name,))
    try:
        conn.commit()
    except:
        print("Error")
        conn.rollback()


def insert_multi_data_to_db(table_name, names, id, col_name, conn):
    x = conn.cursor()
    for name in names:
        is_exist = x.execute("SELECT * FROM " + table_name + (" WHERE recipe_id='%s'" % id) + " AND " + col_name + "='%s'" % name)
        if is_exist == 0:
            sql = "INSERT INTO "+table_name+" VALUES (%s, %s)"
            x.execute(sql, (name, id))
        try:
            conn.commit()
        except:
            print("Error")
            conn.rollback()


def insert_recipe_to_db(recipe_id, recipe_name, recipe_img, recipe_ins, prep_time, num_of_servings, rating, conn):
    x = conn.cursor()
    x.execute("""INSERT INTO Recipe VALUES (%s, %s, %s, %s, %d, %d, %d)""", (recipe_id, recipe_name, recipe_img, recipe_ins, prep_time, num_of_servings, rating))
    try:
        conn.commit()
    except:
        print("Error")
        conn.rollback()


def insert_drink_to_db(drink_id, drink_name, drink_category, drink_image, instructions, glass, conn):
    x = conn.cursor()
    sql = "INSERT INTO Drink VALUES (%d, %s, %s, %s, %s, %s, %s)"
    x.execute(sql, (drink_id, drink_name, drink_category, drink_image, instructions, glass))
    try:
        conn.commit()
    except:
        print("Error")
        conn.rollback()


def insert_drink_ingredient_to_db(drink_ingredient, drink_measure, conn):
    x = conn.cursor()
    sql = "INSERT INTO DrinkIngredients VALUES (%s, %s)"
    x.execute(sql, (drink_ingredient, drink_measure))
    try:
        conn.commit()
    except:
        print("Error")
        conn.rollback()


def insert_to_drink_ingredient_list_db(drink_id, drink_ingredient, drink_measure, conn):
    x = conn.cursor()
    sql = "INSERT INTO ListOfDrinkIngredients VALUES (%d, %s, %s)"
    x.execute(sql, (drink_id, drink_ingredient, drink_measure))
    try:
        conn.commit()
    except:
        print("Error")
        conn.rollback()

