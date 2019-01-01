def get_recipe_from_db_by_filter(max_prep_time_in_sec, num_of_servings_min, num_of_servings_max,  filter_col_name
                                 , filter_val, filter_table_name,  ingredients_to_include, ingredients_to_exclude, conn):
    x = conn.cursor()
    try:
        query = "SELECT * FROM Recipe, " + filter_table_name + " WHERE Recipe.recipe_id = "+ filter_table_name +\
                ".recipe_id AND "+filter_col_name+" = " + filter_val + " AND prep_time <= " + max_prep_time_in_sec + \
                " AND num_of_servings >= " + num_of_servings_min + "AND num_of_servings <= " + num_of_servings_max
        if ingredients_to_exclude:
            query += " AND Recipe.recipe_id NOT IN (SELECT recipe_id FROM ListOfIngredients WHERE " + \
                     get_recipes_includes_ingredient(ingredients_to_exclude)
        if ingredients_to_include:
            query += " AND Recipe.recipe_id IN (SELECT recipe_id FROM ListOfIngredients WHERE " + \
                     get_recipes_includes_ingredient(ingredients_to_include)

        x.execute(query)
        try:
            conn.commit()
        except:
            print("Error")
            conn.rollback()
    except:
        print("failed to get recipe from db by user filters. query: " + query)
        pass


def get_recipes_includes_ingredient(ingredients):
    query = ""
    idx = 0
    for ingredient in ingredients:
        if idx != 0:
            query += "AND "
        query += "LOWER(ingredient_name) LIKE ('%" + ingredient + "%')"
        idx += 1
    return query

