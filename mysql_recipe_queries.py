import my_connect


def get_ethnic_meal_results_by_params(max_prep_time, courses, cuisine):
    conn = my_connect.connect_to_db()
    print("ok")
    res = []
    unlimited = False
    if int(max_prep_time) == 4:
        unlimited = True

    max_prep_time_in_sec = int(max_prep_time) * 3600
    meals_by_id = get_recipe_from_db_by_ethnic_meal_filter(unlimited, max_prep_time_in_sec, courses, cuisine, conn)
    print(meals_by_id)
    for meal_res in meals_by_id:
        meals = {}
        for course in courses:
            recipe_id = meal_res[course.lower() + "_recipe_id"]
            meals[course.lower()] = get_recipe_and_ingredients_by_id(recipe_id, conn)
        res.append(meals)
    conn.close()
    return res


def get_recipe_ingredients_from_db(recipe_id, conn):
    cur = conn.cursor(my_connect.my_cursor)
    sql_get = "SELECT ingredient_name" \
              " FROM ListOfIngredients" \
              " WHERE recipe_id='%s'" % recipe_id
    cur.execute(sql_get)
    try:
        conn.commit()
    except:
        print("Error")
        conn.rollback()
    return cur.fetchall()


def get_time_str(str_seconds):
    time = int(str_seconds)
    hours = time // 3600
    time %= 3600
    minutes = time // 60
    if hours == 0:
        return str(minutes) + ' minutes'
    elif hours == 1 and minutes == 0:
        return "1 hour"
    elif hours == 1:
        return "1 hour and " + str(minutes) + " minutes"
    elif minutes == 0:
        return str(hours) + " hours"
    else:
        return str(hours) + " hours and " + str(minutes) + " minutes"


def get_recipe_and_ingredients_by_id(recipe_id, conn):
    cur = conn.cursor(my_connect.my_cursor)
    res = {}
    try:
        recipe_query = "SELECT * FROM Recipe WHERE Recipe.recipe_id = '" + recipe_id + "'"
        ingredients_query = "SELECT ingredient_name FROM ListOfIngredients WHERE recipe_id = '" + recipe_id + "'"

        cur.execute(recipe_query)
        recipe = cur.fetchall()
        cur.execute(ingredients_query)
        ingredients = cur.fetchall()

        res['dish'] = recipe[0]
        res['dish']['prep_time'] = get_time_str(res['dish']['prep_time'])
        res['ingredients'] = ingredients

        try:
            conn.commit()
        except:
            print("Error")
            conn.rollback()
    except:
        print("failed to get recipe from db by id. query: " + recipe_query + " or: " + ingredients_query)
        pass

    return res


def time_check_str(unlimited, max_prep_time_in_sec, courses):
    if unlimited:
        return ""
    else:
        return "(" + get_sum_of_preps(courses) + (") <= %d" % max_prep_time_in_sec)


def get_recipe_from_db_by_ethnic_meal_filter(unlimited, max_prep_time_in_sec, courses, cuisine, conn):
    cur = conn.cursor(my_connect.my_cursor)
    try:
        query = "SELECT DISTINCT " + get_courses_to_select(courses) + \
                " FROM " + get_inner_tables_by_courses_and_cuisine(courses, cuisine) + \
                " WHERE " + time_check_str(unlimited, max_prep_time_in_sec, courses) + \
                get_course_difference(unlimited, courses) + " ORDER BY RAND() LIMIT 20"
        print(query)

        cur.execute(query)

        try:
            conn.commit()
        except:
            print("Error")
            conn.rollback()
    except:
        print("failed to get recipe from db by user filters. query: " + query)
        pass
    return cur.fetchall()


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
    base_query = "(SELECT DISTINCT Recipe.recipe_id, prep_time " \
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


def get_course_difference(unlimited, courses):
    res = ""

    if len(courses) == 1:
        return res

    for i in range(1, len(courses)+1):
        for j in range(i+1, len(courses)+1):
            if unlimited and i == 1 and j == i+1:
                res += (courses[i - 1].lower() + "s.recipe_id != " + courses[j - 1].lower() + "s.recipe_id")
            else:
                res += (" AND " + courses[i-1].lower() + "s.recipe_id != " + courses[j-1].lower() + "s.recipe_id")
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

