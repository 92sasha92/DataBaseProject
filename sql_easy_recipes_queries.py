import my_connect
import mysql_recipe_queries


def get_recipes_from_db_by_easy_meal_filter(max_prep_time_in_sec, max_ingredients,
                                            ingredients_common_level, conn):
    cur = conn.cursor(my_connect.my_cursor)
    try:
        query = "SELECT Recipe.* " \
                "FROM Recipe, ListOfIngredients " \
                "WHERE Recipe.recipe_id = ListOfIngredients.recipe_id AND Recipe.prep_time <= %s " \
                "Group By Recipe.recipe_id " \
                "HAVING COUNT(ListOfIngredients.ingredient_name) <= %s AND " \
                "   COUNT(ListOfIngredients.ingredient_name) = " \
                "       (SELECT COUNT(ListOfIngredients.ingredient_name) " \
                "        FROM ListOfIngredients " \
                "        WHERE ListOfIngredients.recipe_id = Recipe.recipe_id " \
                "           AND ListOfIngredients.ingredient_name " \
                "               IN (SELECT common_ingredients.ingredient_name " \
                "                   FROM (SELECT ListOfIngredients.ingredient_name, COUNT(*) AS num_of_meals " \
                "                         FROM ListOfIngredients " \
                "                         GROUP BY ListOfIngredients.ingredient_name " \
                "                         HAVING COUNT(*) > %s " \
                "                         ORDER BY num_of_meals) AS common_ingredients)) " \
                "ORDER BY RAND()" % (max_prep_time_in_sec, max_ingredients, ingredients_common_level)
        print(query)
        cur.execute(query)

        try:
            conn.commit()
        except:
            print("Error")
            conn.rollback()
    except:
        print("failed to get recipe from db by user filters. query")
        pass

    return cur.fetchall()


def get_easy_meals_results_by_params(max_prep_time, max_ingredients, ingredients_common_level):
    conn = my_connect.connect_to_db()
    print("connected")
    res = []
    max_prep_time_in_sec = str(int(max_prep_time) * 60)
    meals_by_id = get_recipes_from_db_by_easy_meal_filter(max_prep_time_in_sec, max_ingredients,
                                                          ingredients_common_level, conn)
    for meal_res in meals_by_id:
        meal = {}
        snack_id = meal_res['recipe_id']
        meal['meal'] = meal_res
        meal['meal']['prep_time'] = mysql_recipe_queries.get_time_str(meal['meal']['prep_time'])
        meal['ingredients'] = mysql_recipe_queries.get_recipe_ingredients_from_db(snack_id, conn)
        res.append(meal)
    print(res)
    conn.close()
    return res
