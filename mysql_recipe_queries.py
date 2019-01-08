import MySQLdb
import my_details
import sshtunnel
import pymysql
from paramiko import SSHClient


def get_ethnic_meal_results_by_params(max_prep_time, courses, cuisine):
    # TODO: take care of case 4+ hours max prep time
    res = []
    max_prep_time_in_sec = max_prep_time*3600
    meals_by_id = get_recipe_from_db_by_ethnic_meal_filter(max_prep_time_in_sec, courses, cuisine)
    for meal_res in meals_by_id:
        meals = {}
        for course in courses:
            recipe_id = meal_res[course.lower()+"_recipe_id"]
            meals[course] = get_recipe_and_ingredients_by_id(recipe_id)
        res.append(meals)
    return res


def get_recipe_and_ingredients_by_id(recipe_id):
    with sshtunnel.SSHTunnelForwarder(
            ('nova.cs.tau.ac.il', 22),
            ssh_username=my_details.username,
            ssh_password=my_details.password,
            remote_bind_address=('mysqlsrv1.cs.tau.ac.il', 3306),
            local_bind_address=('localhost', 3305)
    ) as server:
        print(server.local_bind_port)
        conn = pymysql.connect(host="localhost",
                               port=3305,
                               user="DbMysql06",
                               passwd="DbMysql06",
                               db="DbMysql06")
        x = conn.cursor(MySQLdb.cursors.DictCursor)
        res = {}

        try:
            recipe_query = "SELECT * FROM Recipe WHERE Recipe.recipe_id = '" + recipe_id + "'"
            ingredients_query = "SELECT ingredient_name FROM ListOfIngredients WHERE recipe_id = '" + recipe_id + "'"

            x.execute(recipe_query)
            recipe = x.fetchall()
            x.execute(ingredients_query)
            ingredients = x.fetchall()

            res['dish'] = recipe[0]
            res['ingredients'] = ingredients

            try:
                conn.commit()
            except:
                print("Error")
                conn.rollback()
        except:
            print("failed to get recipe from db by id. query: " + recipe_query + " or: " + ingredients_query)
            pass

        conn.close()
        return res


def get_recipe_from_db_by_ethnic_meal_filter(max_prep_time_in_sec, courses, cuisine):
    with sshtunnel.SSHTunnelForwarder(
            ('nova.cs.tau.ac.il', 22),
            ssh_username=my_details.username,
            ssh_password=my_details.password,
            remote_bind_address=('mysqlsrv1.cs.tau.ac.il', 3306),
            local_bind_address=('localhost', 3305)
    ) as server:
        print(server.local_bind_port)
        conn = pymysql.connect(host="localhost",
                               port=3305,
                               user="DbMysql06",
                               passwd="DbMysql06",
                               db="DbMysql06")
        x = conn.cursor(MySQLdb.cursors.DictCursor)

        try:
            query = "SELECT DISTINCT " + get_courses_to_select(courses) + \
                    " FROM " + get_inner_tables_by_courses_and_cuisine(courses, cuisine) + \
                    "WHERE (" + get_sum_of_preps(courses) + ") <= " + max_prep_time_in_sec + \
                    get_course_difference(courses)

            x.execute(query)

            try:
                conn.commit()
            except:
                print("Error")
                conn.rollback()
        except:
            print("failed to get recipe from db by user filters. query: " + query)
            pass
        conn.close()
        return x.fetchall()


def get_courses_to_select(courses):
    res = ""
    idx = 0
    for course in courses:
        if course.lower() == "first":
            res += "firsts.recipe_id AS first_recipe_id"
        elif course.lower() == "main":
            res += "mains.recipe_id AS main_recipe_id"
        elif course.lower() == "dessert":
            res += "desserts.recipe_id AS dessert_recipe_id"
        if idx != len(courses) - 1:
            res += ", "
        else:
            res += " "
        idx += 1
    return res


def get_inner_tables_by_courses_and_cuisine(courses, cuisine):
    res = ""
    idx = 0
    base_query = "(SELECT Recipe.recipe_id, prep_time " \
                 "FROM ListOfCuisines, Recipe, ListOfCourses " \
                 "WHERE Recipe.recipe_id = ListOfCourses.recipe_id " \
                 "AND Recipe.recipe_id = ListOfCuisines.recipe_id AND (course_name = "
    for course in courses:
        if course.lower() == "first":
            res += (base_query + "'Appetizers' OR course_name = 'Soups') AND "
                                 "cuisine_name = '" + cuisine + "') AS firsts ")
        elif course.lower() == "main":
            res += (base_query + "'Main Dishes') AND "
                                 "cuisine_name = '" + cuisine + "') AS mains ")
        elif course.lower() == "dessert":
            res += (base_query + "'Desserts') AND "
                                 "cuisine_name = '" + cuisine + "') AS desserts ")
        if idx != len(courses)-1:
            res += ", "
        else:
            res += " "
        idx += 1
    return res


def get_sum_of_preps(courses):
    res = ""
    idx = 0
    for course in courses:
        if course.lower() == "first":
            res += "firsts.prep_time "
        elif course.lower() == "main":
            res += "mains.prep_time "
        elif course.lower() == "dessert":
            res += "desserts.prep_time "
        if idx != len(courses)-1:
            res += "+ "
        else:
            res += " "
        idx += 1
    return res


def get_all_options_of_column(column_name, values):
    res = ""
    start = 0
    for value in values:
        query = (column_name + " = " + value)
        if start == 0:
            res += query
        else:
            res += (" OR " + query)
        start += 1
    return res


def get_course_difference(courses):
    res = ""
    idx = 0

    if len(courses) == 1:
        return res

    for course in courses:
        if idx == 0:
            res += " AND "
        if idx == 2:
            res += ("AND " + course.lower() + "s.recipe_id != ")
        if course.lower() == "first":
            res += "firsts.recipe_id "
        elif course.lower() == "main":
            res += "mains.recipe_id "
        elif course.lower() == "dessert":
            res += "desserts.recipe_id "
        if idx == 0:
            res += "!= "
        idx += 1
    return res


def get_recipes_includes_ingredient(ingredients):
    query = ""
    idx = 0
    for ingredient in ingredients:
        if idx != 0:
            query += "AND "
        query += "LOWER(ingredient_name) LIKE ('%" + ingredient + "%')"
        idx += 1
    return query


print(get_ethnic_meal_results_by_params("1200", ["first"], "American"))

# cuisine = 'Italian'
#
# max_prep_time_in_sec = '1200'
#
# query = "SELECT DISTINCT " + get_courses_to_select(['first', 'main']) + \
#                 " FROM " + get_inner_tables_by_courses_and_cuisine(['first', 'main'], cuisine) + \
#                 "WHERE (" + get_sum_of_preps(['first', 'main']) + ") <= " + max_prep_time_in_sec + " AND " + \
#                 get_course_difference(['first', 'main'])



