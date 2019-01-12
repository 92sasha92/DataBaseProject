import pymysql
import mysql_recipe_queries
import my_connect

meat_keywords = ['beef', 'chicken', 'lamb', 'turkey', 'pork', 'meat', 'steak', 'burger', 'sausage', 'kebab',
                 'chops']

seafood_keywords = ['seafood', 'shrimp', 'crab', 'lobster', 'scallop', 'calamari', 'octopus', 'mussels', 'oyster']

fish_keywords = ['tuna', 'salmon', 'sardines', 'fish', 'trout', 'bass', 'halibut', 'cod', 'anchovies']

fruit_keywords = ['apple', 'peach', 'strawberries', 'berries', 'grape', 'apricot', 'banana',
                  'strawberry', 'berry', 'cherries', 'plum', 'fruit', 'fig', 'guava', 'melon',
                  'lime', 'lemon', 'orange', 'papaya', 'paw paw', 'pineapple']

salad_keywords = ['salad', 'slaw', 'chopped']


def get_romantic_meal_results_by_params(main_ingredient, side_ingredient, dessert_taste, max_prep_time):
    with my_connect.tunnel() as server:
        print(server.local_bind_port)
        conn = my_connect.connect_to_db()
        res = []
        max_prep_time_in_sec = str(max_prep_time*3600)
        print(max_prep_time_in_sec)
        meals_by_id = get_recipe_from_db_by_romantic_meal_filter(main_ingredient, side_ingredient, dessert_taste, max_prep_time_in_sec,  conn)
        for meal_res in meals_by_id:
            meals = {}
            recipe_id = meal_res["main_recipe_id"]
            meals["main"] = mysql_recipe_queries.get_recipe_and_ingredients_by_id(recipe_id, conn)
            recipe_id = meal_res["side_recipe_id"]
            meals["side"] = mysql_recipe_queries.get_recipe_and_ingredients_by_id(recipe_id, conn)
            recipe_id = meal_res["dessert_recipe_id"]
            meals["dessert"] = mysql_recipe_queries.get_recipe_and_ingredients_by_id(recipe_id, conn)
            res.append(meals)
        print(res)
        conn.close()
        return res


def get_recipe_from_db_by_romantic_meal_filter(main_ingredient, side_ingredient, dessert_ingredient, max_prep_time_in_sec,
                                               conn):
    x = conn.cursor(my_connect.my_cursor)
    try:
        query = "SELECT DISTINCT sides.recipe_id AS side_recipe_id, mains.recipe_id AS main_recipe_id," \
                " desserts.recipe_id AS dessert_recipe_id FROM " \
                "(SELECT DISTINCT Recipe.recipe_id, prep_time FROM Recipe, ListOfCourses " \
                "WHERE Recipe.recipe_id = ListOfCourses.recipe_id " \
                "AND course_name = 'Side Dishes' ORDER BY RAND()) AS sides, " \
                "(SELECT DISTINCT Recipe.recipe_id, prep_time FROM Recipe, ListOfCourses " \
                "WHERE Recipe.recipe_id = ListOfCourses.recipe_id AND course_name = 'Main Dishes') AS mains, " \
                "(SELECT DISTINCT Recipe.recipe_id, prep_time FROM Recipe, ListOfCourses " \
                "WHERE Recipe.recipe_id = ListOfCourses.recipe_id AND course_name = 'Desserts') AS desserts " \
                "WHERE (sides.prep_time + mains.prep_time + desserts.prep_time) <= " + max_prep_time_in_sec + \
                " AND (" + get_query_of_recipes_like_keywords(main_ingredient) + ") AND "
        if side_ingredient.lower() == 'salad':
            query += ("(" + get_query_of_recipes_like_keywords(side_ingredient) + ") ")
        else:
            query += ("sides.recipe_id IN (SELECT DISTINCT recipe_id FROM ListOfIngredients "
                      "WHERE LOWER(ingredient_name) LIKE '%" + side_ingredient + "%') ")

        if dessert_ingredient.lower() == "nosugar":
            query += "AND desserts.recipe_id NOT IN (SELECT DISTINCT recipe_id FROM ListOfIngredients " \
                     "WHERE LOWER(ingredient_name) LIKE '%sugar%')"
        elif dessert_ingredient.lower() == "fruit":
            print("fruitttttt")
            query += ("AND (" + get_query_of_recipes_like_keywords(dessert_ingredient) + ") ")
            print(query)
        else:
            query += "AND desserts.recipe_id IN (SELECT DISTINCT recipe_id FROM ListOfIngredients " \
                     "WHERE LOWER(ingredient_name) LIKE '%" + dessert_ingredient + "%')"
        query += get_recipe_difference() + " LIMIT 20"
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


def get_query_of_recipes_like_keywords(main_ingredient):

    res = ""
    base_query = "mains.recipe_id LIKE '%"
    keywords = []
    if main_ingredient.lower() == 'meat':
        keywords = meat_keywords
    elif main_ingredient.lower() == 'seafood':
        keywords = seafood_keywords
    elif main_ingredient.lower() == 'fish':
        keywords = fish_keywords
    if main_ingredient.lower() == 'salad':
        base_query = "sides.recipe_id LIKE '%"
        keywords = salad_keywords
    elif main_ingredient.lower() == 'fruit':
        base_query = "desserts.recipe_id LIKE '%"
        keywords = fruit_keywords

    idx = 0
    for keyword in keywords:
        if idx != 0:
            res += "OR "
        res += base_query + keyword + "%' "
        idx += 1

    return res


def get_recipe_difference():
    res = ""
    dishes = ['mains', 'sides', 'desserts']
    for i in range(1, 4):
        for j in range(i+1, 4):
            res += (" AND " + dishes[i-1] + ".recipe_id != " + dishes[j-1] + ".recipe_id ")
    return res
