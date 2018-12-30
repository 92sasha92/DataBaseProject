import MySQLdb


def load_names_from_db(table_name, col_name, conn):
    x = conn.cursor(MySQLdb.cursors.DictCursor)
    res = []
    sql = "SELECT * FROM "+table_name

    try:
        x.execute(sql)
        for row in x.fetchall():
            res.append(row[col_name])
        return res
    except:
        print("Error in fetching data from table %s" % table_name)


def insert_name_to_db(table_name, obj_name, col_name, conn):
    x = conn.cursor()
    try:
        is_exist = x.execute("SELECT * FROM "+table_name+" WHERE "+col_name+"='%s'" % obj_name)
        if is_exist == 0:
            query = "INSERT INTO "+table_name+" VALUES (%s)"
            x.execute(query, (obj_name,))
        try:
            conn.commit()
        except:
            print("Error")
            conn.rollback()
    except:
        print("failed to insert data into db. table: " + table_name + " failed to insert name: " + obj_name)
        pass


def insert_multi_data_to_db(table_list_name, table_name, names, id, col_name, conn):
    x = conn.cursor()
    for name in names:
        name = name.replace("'", "")
        name = name.replace("-", " ")
        try:
            insert_name_to_db(table_name, name, col_name, conn)

            is_exist = x.execute("SELECT * FROM " + table_list_name + (" WHERE recipe_id='%s'" % id) +
                                 " AND " + col_name + "='%s'" % name)
            if is_exist == 0:
                sql = "INSERT INTO "+table_list_name+" VALUES (%s, %s)"
                x.execute(sql, (id, name))
            try:
                conn.commit()
            except:
                print("Error")
                conn.rollback()
        except:
            print("failed to insert data into db. table: " + table_list_name + " failed to insert name: " + name)
            pass


def insert_recipe_to_db(recipe_id, recipe_name, recipe_img, recipe_ins, prep_time, num_of_servings, rating, conn):
    x = conn.cursor()
    try:
        is_exist = x.execute("SELECT * FROM Recipe WHERE recipe_id='%s'" % recipe_id)
        if is_exist == 0:
            x.execute("""INSERT INTO Recipe VALUES (%s, %s, %s, %s, %s, %s, %s)""", (recipe_id, recipe_name, recipe_img, recipe_ins, prep_time, num_of_servings, rating))
            try:
                conn.commit()
            except:
                print("Error")
                conn.rollback()
    except:
        print("failed to insert data into db. table: Recipe failed to insert name: " + recipe_name)


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

