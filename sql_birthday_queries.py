import mysql_recipe_queries
import my_connect
import random

gluten_keywords = ['gluten', 'flour', 'wheat', 'durum', 'emmer', 'semolina', 'spelt', 'farina',
                   'farro', 'graham', 'rye', 'barely', 'triticale', 'malt', 'yeast', 'pasta', 'spaghetti', 'ravioli',
                   'couscous', 'gnocchi', 'noodles', 'bread', 'cracker', 'flakes', 'puffs', 'crouton', 'beer',
                   'granola']

dairy_keywords = ['milk', 'butter', 'cheese', 'curds', 'custard', 'nougat', 'paneer', 'pudding', 'cream', 'whey',
                  'yogurt']

sesame_keywords = ['benne', 'benniseed', 'seed', 'sesame', 'gomasio', 'halvah', 'tahini',
                   'tahina', 'tehina', 'tehini', 'til']

egg_keywords = ['egg', 'mayo', 'meringue', 'surimi', 'marzipan', 'marshmallow', 'nougat', 'pasta', 'noodles']

peanut_keywords = ['peanut', 'arachis', 'nut', 'goobers', 'lupin', 'mandelonas', 'marzipan', 'nougat', 'seed']


def get_birthday_meal_results_by_params(allergies, is_kids_party, max_prep_time):
    conn = my_connect.connect_to_db()
    print("ok")
    res = []
    max_prep_time_in_sec = str(max_prep_time * 3600)
    print(is_kids_party)
    meals_by_id = get_recipe_from_db_by_birthday_meal_filter(allergies, is_kids_party, max_prep_time_in_sec, conn)
    # print("before shufle")
    # meals_by_id = random.sample(meals_by_id, len(meals_by_id))
    # print("after shufle")
    # if len(meals_by_id) > 20:
    #     meals_by_id = meals_by_id[0:20]
    for meal_res in meals_by_id:
        meals = {}
        recipe_id = meal_res["snack_recipe_id"]
        meals["snack"] = mysql_recipe_queries.get_recipe_and_ingredients_by_id(recipe_id, conn)
        recipe_id = meal_res["main_recipe_id"]
        meals["main"] = mysql_recipe_queries.get_recipe_and_ingredients_by_id(recipe_id, conn)
        recipe_id = meal_res["side_recipe_id"]
        meals["side"] = mysql_recipe_queries.get_recipe_and_ingredients_by_id(recipe_id, conn)
        recipe_id = meal_res["cake_recipe_id"]
        meals["dessert"] = mysql_recipe_queries.get_recipe_and_ingredients_by_id(recipe_id, conn)
        res.append(meals)
    print(res)
    conn.close()
    return res


def get_recipe_from_db_by_birthday_meal_filter(allergies, is_kids_party, max_prep_time, conn):
    x = conn.cursor(my_connect.my_cursor)
    try:
        query = "SELECT DISTINCT snacks.recipe_id AS snack_recipe_id, sides.recipe_id AS side_recipe_id, " \
                "mains.recipe_id AS main_recipe_id, cakes.recipe_id AS cake_recipe_id " \
                "FROM (SELECT DISTINCT Recipe.recipe_id, prep_time FROM Recipe, ListOfCourses" + \
                (", ListOfCuisines" if is_kids_party else "") + " WHERE Recipe.recipe_id = ListOfCourses.recipe_id " \
                + ("AND Recipe.recipe_id = ListOfCuisines.recipe_id " if is_kids_party else "") + \
                "AND course_name = 'Side Dishes' " + (" AND cuisine_name LIKE '%Kid%'" if is_kids_party else "") + \
                " ORDER BY RAND() LIMIT 16) AS sides, (SELECT DISTINCT Recipe.recipe_id, prep_time " \
                "FROM Recipe, ListOfCourses" + (", ListOfCuisines" if is_kids_party else "") + \
                " WHERE Recipe.recipe_id = ListOfCourses.recipe_id " + \
                ("AND Recipe.recipe_id = ListOfCuisines.recipe_id " if is_kids_party else "") + \
                "AND course_name IN ('Snacks', 'Appetizers') " + \
                (" AND cuisine_name LIKE '%Kid%'" if is_kids_party else "") + \
                " ORDER BY RAND() LIMIT 16) AS snacks, (SELECT DISTINCT Recipe.recipe_id, prep_time " \
                "FROM Recipe, ListOfCourses" + (", ListOfCuisines" if is_kids_party else "") + \
                " WHERE Recipe.recipe_id = ListOfCourses.recipe_id " + \
                ("AND Recipe.recipe_id = ListOfCuisines.recipe_id" if is_kids_party else "") + \
                " AND course_name = 'Main Dishes' " + ("AND cuisine_name LIKE '%Kid%'" if is_kids_party else "") + \
                " ORDER BY RAND() LIMIT 16) AS mains, (SELECT DISTINCT Recipe.recipe_id, prep_time FROM Recipe, " \
                "ListOfCourses" + (", ListOfCuisines" if is_kids_party else "") + " WHERE Recipe.recipe_id = " \
                "ListOfCourses.recipe_id AND Recipe.name LIKE '%cake' AND course_name = 'Desserts'" + \
                (" AND Recipe.recipe_id = ListOfCuisines.recipe_id "
                 "AND cuisine_name LIKE '%Kid%'" if is_kids_party else "") + \
                " ORDER BY RAND() LIMIT 16) AS cakes WHERE (snacks.prep_time + sides.prep_time + " \
                "mains.prep_time + cakes.prep_time) <= "\
                + max_prep_time + get_ingredient_allergy_related(is_kids_party, allergies) + " ORDER BY RAND()" \
                                                                                             " LIMIT 20"

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


def get_ingredient_allergy_related(is_kids_party, allergies):
    res = ""
    if len(allergies) == 0 and (not is_kids_party):
        return res

    dishes = ['snacks', 'sides', 'mains', 'cakes']

    for dish in dishes:
        res += " AND "
        res += ("NOT EXISTS (SELECT DISTINCT recipe_id FROM ListOfIngredients WHERE ListOfIngredients.recipe_id = " +
                dish + ".recipe_id " + get_query_of_ingredients_like_keywords(allergies) +
                (" GROUP BY recipe_id, ingredient_name HAVING (COUNT(*) > 10)) " if is_kids_party else ") "))
    return res


def get_query_of_ingredients_like_keywords(allergies):
    if len(allergies) == 0:
        return ""

    res = "AND ("
    base_query = "ingredient_name LIKE '%"
    keywords = []

    idx = 0
    for allergy in allergies:
        if allergy.lower() == 'sesame':
            keywords = sesame_keywords
        elif allergy.lower() == 'peanuts':
            keywords = peanut_keywords
        elif allergy.lower() == 'dairy':
            keywords = dairy_keywords
        elif allergy.lower() == 'gluten':
            keywords = gluten_keywords
        for keyword in keywords:
            if idx != 0:
                res += "OR "
            res += base_query + keyword + "%' "
            idx += 1

    return res + ") "


def get_recipe_difference():
    res = ""
    dishes = ['snacks', 'mains', 'sides', 'cakes']
    for i in range(1, 5):
        for j in range(i+1, 5):
            res += (" AND " + dishes[i-1] + ".recipe_id != " + dishes[j-1] + ".recipe_id ")
    return res
