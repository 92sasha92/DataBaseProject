#import MySQLdb
import pymysql
import sshtunnel
from paramiko import SSHClient
import my_details


def add_drink_list_constraints(sql_get, l, col_name):
    i = 0
    for elem in l:
        if i == 0:
            sql_get += " (Drink.%s='%s'" % (col_name, elem)
        else:
            sql_get += " OR Drink.%s='%s'" % (col_name, elem)
        i += 1
    sql_get += ")"
    return sql_get


def add_drink_ingredients_list_constraints(sql_get, l, col_name):
    i = 0
    for elem in l:
        if i == 0:
            sql_get += " Drink.drink_id=ListOfDrinkIngredients.drink_id AND" \
                       " (ListOfDrinkIngredients.%s='%s'" % (col_name, elem)
        else:
            sql_get += " OR ListOfDrinkIngredients.%s='%s'" % (col_name, elem)
        i += 1
    sql_get += ")"
    return sql_get


def add_join_list_not_wanted(sql_get, l, col_name):
    i = 0
    for elem in l:
        if i == 0:
            sql_get += " (Drink.%s<>'%s'" % (col_name, elem)
        else:
            sql_get += " AND Drink.%s<>'%s'" % (col_name, elem)
        i += 1
    sql_get += ")"
    return sql_get


def get_drinks_from_db(alcoholic, ingredients, glasses, max_ingredients, conn):
    cur = conn.cursor(pymysql.cursors.DictCursor)
    sql_get = "SELECT Drink.* FROM Drink, ListOfDrinkIngredients WHERE"

    if glasses:
        sql_get = add_drink_list_constraints(sql_get, glasses, 'glass')
    if glasses and ingredients:
        sql_get += " AND"
        sql_get = add_drink_ingredients_list_constraints(sql_get, ingredients, 'ingredient_name')
    elif ingredients:
        sql_get = add_drink_ingredients_list_constraints(sql_get, ingredients, 'ingredient_name')

    if alcoholic != "both":
        sql_get += " AND Drink.is_alcoholic='%s'" % alcoholic

    if max_ingredients:
        sql_get += " AND (Drink.drink_id IN (SELECT ListOfDrinkIngredients.drink_id " \
                   "FROM ListOfDrinkIngredients "\
                   "GROUP BY ListOfDrinkIngredients.drink_id "\
                   "HAVING COUNT(*) <= %s))" % max_ingredients
    print(sql_get)
    cur.execute(sql_get)
    try:
        conn.commit()
    except:
        print("Error")
        conn.rollback()
    return cur.fetchall()


def get_drink_ingredients_from_db(drink_id, conn):
    cur = conn.cursor(pymysql.cursors.DictCursor)
    sql_get = "SELECT ListOfDrinkIngredients.ingredient_name, ListOfDrinkIngredients.ingredient_measure" \
              " FROM Drink, ListOfDrinkIngredients" \
              " WHERE Drink.drink_id='%s' AND ListOfDrinkIngredients.drink_id=Drink.drink_id" % drink_id

    cur.execute(sql_get)
    try:
        conn.commit()
    except:
        print("Error")
        conn.rollback()
    return cur.fetchall()


def get_drink_results_by_params(alcoholic, ingredients, glasses, max_ingredients, side_dish):
    with sshtunnel.SSHTunnelForwarder(
            ('nova.cs.tau.ac.il', 22),
            ssh_username="%s" % my_details.username,
            ssh_password="%s" % my_details.password,
            remote_bind_address=('mysqlsrv1.cs.tau.ac.il', 3306),
            local_bind_address=('localhost', 3305)
    ) as server:
        print(server.local_bind_port)
        conn = pymysql.connect(host="localhost",
                               port=3305,
                               user="DbMysql06",
                               passwd="DbMysql06",
                               db="DbMysql06")
        res = []
        drinks_by_id = get_drinks_from_db(alcoholic, ingredients, glasses, max_ingredients, conn)
        print("hi")
        for drink_res in drinks_by_id:
            drink = {}
            drink_id = drink_res['drink_id']
            drink['drink'] = drink_res
            drink['ingredients'] = get_drink_ingredients_from_db(drink_id, conn)
            print(drink['ingredients'])
            res.append(drink)
        print(res)
        res_snacks = get_snacks_results(side_dish, conn)
        conn.close()
        return res, res_snacks


def get_snacks_from_db(conn):
    cur = conn.cursor(pymysql.cursors.DictCursor)
    sql_get = "SELECT Recipe.* " \
              "FROM Recipe, ListOfCourses " \
              "WHERE Recipe.recipe_id = ListOfCourses.recipe_id AND course_name = 'Snacks' LIMIT 30"

    cur.execute(sql_get)
    try:
        conn.commit()
    except:
        print("Error")
        conn.rollback()
    return cur.fetchall()


def get_snack_ingredients_from_db(snack_id, conn):
    cur = conn.cursor(pymysql.cursors.DictCursor)
    sql_get = "SELECT ListOfIngredients.ingredient_name" \
              " FROM Recipe, ListOfIngredients" \
              " WHERE Recipe.recipe_id='%s' AND ListOfIngredients.recipe_id=Recipe.recipe_id" % snack_id
    print(sql_get)
    cur.execute(sql_get)
    try:
        conn.commit()
    except:
        print("Error")
        conn.rollback()
    return cur.fetchall()


def get_snacks_results(side_dish, conn):
    if side_dish == "ddffd":
        return

    res = []
    snacks_by_id = get_snacks_from_db(conn)
    print(snacks_by_id)
    for snack_res in snacks_by_id:
        snack = {}
        snack_id = snack_res['recipe_id']
        snack['snack'] = snack_res
        snack['ingredients'] = get_snack_ingredients_from_db(snack_id, conn)
        print(snack['ingredients'])
        res.append(snack)
    print(res)
    return res

