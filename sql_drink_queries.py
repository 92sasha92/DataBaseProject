#import MySQLdb
import pymysql
import sshtunnel
from paramiko import SSHClient


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


def get_drinks_from_db(alcoholic, ingredients, glasses, max_ingredients):
    with sshtunnel.SSHTunnelForwarder(
            ('nova.cs.tau.ac.il', 22),
            ssh_username="",
            ssh_password="",
            remote_bind_address=('mysqlsrv1.cs.tau.ac.il', 3306),
            local_bind_address=('localhost', 3305)
    ) as server:
        print(server.local_bind_port)
        conn = pymysql.connect(host="localhost",
                               port=3305,
                               user="DbMysql06",
                               passwd="DbMysql06",
                               db="DbMysql06")
        print("ok")
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
        conn.close()
        return cur.fetchall()
