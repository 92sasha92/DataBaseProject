
def insert_name_to_db(table_name, obj_name, conn):
    x = conn.cursor()
    x.execute("""INSERT INTO %s VALUES (%s)""", (table_name, obj_name))
    try:
        conn.commit()
    except:
        print("Error")
        conn.rollback()


def insert_multi_data_to_db(table_name, names, id, conn):
    x = conn.cursor()
    for name in names:
        x.execute("""INSERT INTO %s VALUES (%s, %s)""", (table_name, name, id))
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

