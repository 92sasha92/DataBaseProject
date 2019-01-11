import my_connect
import mysql_recipe_queries


def get_recipes_from_db_by_professional_meal_filter(conn):
    cur = conn.cursor(my_connect.my_cursor)
    try:
        more_that_avg = 10
        limit = 20
        query = "SELECT Recipe.*" \
                "FROM Recipe, ListOfIngredients " \
                "WHERE Recipe.recipe_id = ListOfIngredients.recipe_id AND Recipe.rating >= (SELECT AVG(rating)" \
                "                                                                           FROM Recipe) " \
                "GROUP BY Recipe.recipe_id " \
                "HAVING COUNT(*) > %d + " \
                "   (SELECT AVG(recipe_to_ingredients.num_ingredients) " \
                "    FROM (SELECT Recipe.recipe_id AS id, COUNT(*) AS num_ingredients " \
                "          FROM   Recipe, ListOfIngredients " \
                "          WHERE  Recipe.recipe_id = ListOfIngredients.recipe_id " \
                "          GROUP BY Recipe.recipe_id) AS recipe_to_ingredients) " \
                "ORDER BY RAND() LIMIT %d" % (more_that_avg, limit)
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


def get_professional_meals_results():
    with my_connect.tunnel() as server:
        print(server.local_bind_port)
        conn = my_connect.connect_to_db()
        res = []
        meals_by_id = get_recipes_from_db_by_professional_meal_filter(conn)
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
