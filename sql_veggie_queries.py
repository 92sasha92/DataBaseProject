import my_connect
import mysql_recipe_queries

meat_keywords = ['beef', 'chicken', 'lamb', 'turkey', 'pork', 'meat', 'steak', 'burger', 'partridge',
                 'keema', 'liver', 'heart', 'ham', 'kidney', 'crab', 'chops', 'bacon', 'quail', 'mutton']

veg_keywords = ['bok choy', 'beans', 'leaves', 'drumstick', 'tomato', 'lime', 'plantain', 'turnip',
                'potatoes', 'gourd', 'pepper', 'spinach', 'onion', 'mushroom', 'radish', 'shallots',
                'lettuce', 'leek', 'pumpkin', 'yam', 'jalapeno', 'fruit', 'peas', 'chilly', 'garlic',
                'cucumber', 'zucchini', 'corn', 'celery', 'cauliflower', 'carrot', 'capers', 'broccoli', 'beet',
                'weed', 'cabbage', 'bamboo', 'kale', 'avocado', 'eggplant', 'asparagus', 'artichoke',
                'ginger', 'sprout']


def get_all_ingredients_like_items_in_list(keywords):
    res = ""
    idx = 0
    for keyword in keywords:
        res += "ingredient_name LIKE '%" + keyword + "%' "
        if idx < len(keywords)-1:
            res += "OR "
        idx += 1
    return res


def get_veg_recipes_from_db(min_veg_num, conn):
    cur = conn.cursor(my_connect.my_cursor)
    try:
        query = "SELECT DISTINCT Recipe.*, ListOfVegIngredientsNum.veg_ingredient_num " \
                "FROM Recipe, (SELECT DISTINCT recipe_id , COUNT(recipe_id) AS veg_ingredient_num " \
                "FROM ListOfIngredients WHERE " + get_all_ingredients_like_items_in_list(veg_keywords) + \
                "GROUP BY recipe_id) AS ListOfVegIngredientsNum " \
                "WHERE ListOfVegIngredientsNum.recipe_id = Recipe.recipe_id  AND Recipe.recipe_id NOT IN " \
                "(SELECT DISTINCT recipe_id FROM ListOfIngredients WHERE " + \
                get_all_ingredients_like_items_in_list(meat_keywords) + \
                ") AND ListOfVegIngredientsNum.veg_ingredient_num >= " + min_veg_num + \
                " ORDER BY ListOfVegIngredientsNum.veg_ingredient_num DESC, rating DESC LIMIT 20"
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


def get_veg_recipes_results_by_params(min_veg_num):
    conn = my_connect.connect_to_db()
    res = []
    recipes = get_veg_recipes_from_db(min_veg_num, conn)
    for recipe in recipes:
        meal = {}
        recipe_id = recipe['recipe_id']
        meal['meal'] = recipe
        meal['meal']['prep_time'] = mysql_recipe_queries.get_time_str(meal['meal']['prep_time'])
        meal['ingredients'] = mysql_recipe_queries.get_recipe_ingredients_from_db(recipe_id, conn)
        print(meal['ingredients'])
        res.append(meal)
    print(res)
    conn.close()
    return res
