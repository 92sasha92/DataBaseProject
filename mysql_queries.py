
def insert_name_to_db(table_name, obj_name, conn):
    x = conn.cursor()
    query = "INSERT INTO "+table_name+" VALUES (%s)"
    x.execute(query, (obj_name,))
    try:
        conn.commit()
    except:
        print("Error")
        conn.rollback()


def insert_multi_data_to_db(table_name, names, id, conn):
    x = conn.cursor()
    for name in names:
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
    sql_get = "SELECT drink_id FROM Drink Where drink_id={}".format(drink_id)
    is_exit = x.execute(sql_get)
    if is_exit == 0:
        x.execute(sql, (drink_id, drink_name, drink_category, drink_image, instructions, glass))
    try:
        conn.commit()
    except:
        print("Error")
        conn.rollback()


def insert_drink_ingredient_to_db(drink_ingredient, drink_measure, conn):
    x = conn.cursor()
    sql = "INSERT INTO DrinkIngredients VALUES (%s, %s)"
    sql_get = "SELECT drink_ingredient, drink_measure " \
              "FROM DrinkIngredients " \
              "Where drink_ingredient={} AND drink_measure={}".format(drink_ingredient, drink_measure)
    is_exit = x.execute(sql_get)
    if is_exit == 0:
        x.execute(sql, (drink_ingredient, drink_measure))
    try:
        conn.commit()
    except:
        print("Error")
        conn.rollback()


def insert_to_drink_ingredient_list_db(drink_id, drink_ingredient, drink_measure, conn):
    x = conn.cursor()
    sql = "INSERT INTO ListOfDrinkIngredients VALUES (%d, %s, %s)"
    sql_get = "SELECT drink_id, drink_ingredient, drink_measure " \
              "FROM ListOfDrinkIngredients " \
              "Where drink_id={} AND drink_ingredient={} " \
              "AND drink_measure={}".format(drink_id, drink_ingredient, drink_measure)
    is_exit = x.execute(sql_get)
    if is_exit == 0:
        x.execute(sql, (drink_id, drink_ingredient, drink_measure))
    try:
        conn.commit()
    except:
        print("Error")
        conn.rollback()

