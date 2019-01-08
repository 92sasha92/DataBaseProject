import my_details
import sshtunnel
import pymysql
import mysql_recipe_queries


def get_holiday_meal_results_by_params(holiday, max_prep_time, min_num_of_guests, num_of_dishes):
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
        res = []
        max_prep_time_in_sec = str(max_prep_time*3600)
        print(max_prep_time_in_sec)
        meals_by_id = get_recipe_from_db_by_holiday_meal_filter(holiday, max_prep_time_in_sec, min_num_of_guests, num_of_dishes, conn)
        for meal_res in meals_by_id:
            meals = {}
            for num in range(1, num_of_dishes+1):
                recipe_id = meal_res["recipe_id_"+str(num)]
                meals["recipe_"+str(num)] = mysql_recipe_queries.get_recipe_and_ingredients_by_id(recipe_id, conn)
            res.append(meals)
        print(res)
        conn.close()
        return res


def get_recipe_from_db_by_holiday_meal_filter(holiday, max_prep_time_in_sec, min_num_of_guests, num_of_dishes, conn):
    x = conn.cursor(pymysql.cursors.DictCursor)

    try:
        query = "SELECT DISTINCT " + get_recipe_ids_to_select(num_of_dishes) + "FROM " \
                + get_inner_selection(num_of_dishes, holiday) + "WHERE (" + \
                get_query_sum_of_attribute(num_of_dishes, "prep_time") + \
                ") <= " + max_prep_time_in_sec + " AND (" + \
                get_query_sum_of_attribute(num_of_dishes, "num_of_servings") + ") >= " + \
                min_num_of_guests + " AND EXISTS (SELECT recipe_id FROM ListOfCourses " \
                "WHERE (" + get_courses_join_to_options(num_of_dishes) + \
                ") AND course_name IN ('Main Dishes', 'Lunch')) " \
                "ORDER BY RAND() LIMIT 10"
        print(query)
        x.execute(query)

        try:
            conn.commit()
        except:
            print("Error")
            conn.rollback()
    except:
        print("failed to get recipe from db by user filters. query")
        pass

    return x.fetchall()


def get_recipe_ids_to_select(num_of_dishes):
    res = ""
    for i in range(1, num_of_dishes+1):
        res += ("options"+str(i)+".recipe_id AS recipe_id_"+str(i))
        if i != num_of_dishes:
            res += ", "
    return res + " "


def get_inner_selection(num_of_dishes, holiday):
    res = ""
    base_query = "(SELECT ListOfHolidays.recipe_id, prep_time, num_of_servings " \
                 "FROM Recipe, ListOfHolidays, ListOfCourses " \
                 "WHERE Recipe.recipe_id = ListOfHolidays.recipe_id " \
                 "AND Recipe.recipe_id = ListOfCourses.recipe_id " \
                 "AND holiday_name = '" + holiday + "' AND course_name NOT IN " \
                 "('Afternoon Tea', 'Beverages', 'Cocktails', 'Condiments and Sauces')) AS options"
    for i in range(1, num_of_dishes+1):
        res += (base_query + str(i))
        if i != num_of_dishes:
            res += ", "
    return res + " "


def get_query_sum_of_attribute(num_of_dishes, attribute):
    res = ""
    for i in range(1, num_of_dishes + 1):
        res += ("options" + str(i) + "." + attribute)
        if i != num_of_dishes:
            res += " + "
    return res + " "


def get_courses_join_to_options(num_of_dishes):
    res = ""
    for i in range(1, num_of_dishes + 1):
        res += ("ListOfCourses.recipe_id = options" + str(i) + ".recipe_id")
        if i != num_of_dishes:
            res += " OR "
    return res
