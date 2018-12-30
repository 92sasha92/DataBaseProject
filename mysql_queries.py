
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

