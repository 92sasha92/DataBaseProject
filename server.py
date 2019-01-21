from flask import Flask, render_template, redirect, url_for, request
import sql_drink_queries
import mysql_recipe_queries
import sql_holiday_queries
import sql_romantic_queries
import sql_easy_recipes_queries
import sql_birthday_queries
import sql_professional_recipes_queries
import sql_veggie_queries

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('pages/main_page.html')


@app.route('/ethnic_cuisines_start')
def ethnic_cuisines_page():
    return render_template('pages/intro_animation.html', type="Ethnic Cuisines",
                           goto_url="ethnic_cuisines", image="worldfood.jpg")


@app.route('/ethnic_cuisines', methods=['POST', 'GET'])
def ethnic_cuisines():
    if request.method == 'GET':
        return render_template('pages/ethnic_cuisines.html')
    elif request.method == 'POST':
        prep_time = request.form['Maximum Preparation Time']
        type_of_meals = request.form.getlist('Type Of Meal')
        if type_of_meals == []:
            return render_template('results/ethnic_cuisines_results.html', meals=[])
        #print("HERE:          ",type_of_meals)
        cuisine = request.form['Cuisine']
        meals = mysql_recipe_queries.get_ethnic_meal_results_by_params(prep_time, type_of_meals, cuisine)
        print(meals)
        return render_template('results/ethnic_cuisines_results.html', meals=meals)
    else:
        return 'failed to load page or to send request'


@app.route('/professional_recipes_start')
def professional_recipes_page():
    return render_template('pages/intro_animation.html', type="Professional Recipes",
                           goto_url="professional_recipes", image="professional_recipes.jpg")


@app.route('/professional_recipes')
def professional_recipes():
    meals = sql_professional_recipes_queries.get_professional_meals_results()
    return render_template('results/recipes_results.html', meals=meals)


@app.route('/holiday_start')
def holiday_page():
    return render_template('pages/intro_animation.html', type="Holiday Dinner",
                           goto_url="holiday", image="family.jpg")


@app.route('/holiday', methods=['POST', 'GET'])
def holiday():
    if request.method == 'GET':
        return render_template('pages/holiday.html')
    elif request.method == 'POST':
        prep_time = int(request.form['Maximum Preparation Time'])
        holiday = request.form['Holiday']
        number_of_dishes = int(request.form['Number Of Dishes'])
        min_num_of_servings = request.form['Number Of Guests']

        meals = sql_holiday_queries.get_holiday_meal_results_by_params(holiday, prep_time,
                                                                       min_num_of_servings,
                                                                       number_of_dishes)
        print(meals)
        return render_template('results/holiday_results.html', meals=meals, num_of_dishes=number_of_dishes)
    else:
        return 'failed to load holiday result page or to send request'


@app.route('/romantic_start')
def romantic_page():
    return render_template('pages/intro_animation.html', type="Romantic Dinner",
                           goto_url="romantic", image="romantic.jpg")


@app.route('/romantic', methods=['POST', 'GET'])
def romantic():
    if request.method == 'GET':
        return render_template('pages/romantic.html')
    elif request.method == 'POST':
        prep_time = int(request.form['Maximum Preparation Time'])
        main_ingredient = request.form['Main Ingredient']
        side_ingredient = request.form['Side Ingredient']
        dessert = request.form['Dessert']
        meals = sql_romantic_queries.get_romantic_meal_results_by_params(main_ingredient, side_ingredient,
                                                                         dessert, prep_time)
        return render_template('results/romantic_results.html', meals=meals)
    else:
        return 'failed to load page or to send request'


@app.route('/meatless_monday_start')
def meatless_monday_page():
    return render_template('pages/intro_animation.html', type="Meatless Monday",
                           goto_url="meatless_monday", image="meatless_monday.jpg")


@app.route('/meatless_monday', methods=['POST', 'GET'])
def meatless_monday():
    if request.method == 'GET':
        return render_template('pages/meatless_monday.html')
    elif request.method == 'POST':
        # get the time in minutes
        min_veg_num = request.form['Minimum Vegetables']
        meals = sql_veggie_queries.get_veg_recipes_results_by_params(min_veg_num)
        return render_template('results/recipes_results.html', meals=meals)
    else:
        return 'failed to load page or to send request'


@app.route('/easy_recipes_start')
def easy_recipe_page():
    return render_template('pages/intro_animation.html', type="Easy Recipes",
                           goto_url="easy_recipes", image="easy_recipes.jpg")


@app.route('/easy_recipes', methods=['POST', 'GET'])
def easy_recipes():
    if request.method == 'GET':
        return render_template('pages/easy_recipes.html')
    elif request.method == 'POST':
        # get the time in minutes
        max_prep_time = request.form['Maximum Preparation Time']
        max_ingredients = request.form['Maximum Ingredients']
        ingredients_common_level = request.form['Common Level']
        meals = sql_easy_recipes_queries.get_easy_meals_results_by_params(max_prep_time, max_ingredients,
                                                                          ingredients_common_level)
        return render_template('results/recipes_results.html', meals=meals)
    else:
        return 'failed to load page or to send request'


@app.route('/birthday_start')
def birthday_page():
    return render_template('pages/intro_animation.html', type="Birthday Party",
                           goto_url="birthday", image="birthday.jpg")


@app.route('/birthday', methods=['POST', 'GET'])
def birthday():
    if request.method == 'GET':
        return render_template('pages/birthday.html')
    elif request.method == 'POST':
        prep_time = int(request.form['Maximum Preparation Time'])
        include_children = request.form['with children'] == 'True'
        allergies = request.form.getlist('Allergy')
        meals = sql_birthday_queries.get_birthday_meal_results_by_params(allergies, include_children, prep_time)
        return render_template('results/birthday_results.html', meals=meals)
    else:
        return 'failed to load page or to send request'


@app.route('/cocktail_start')
def cocktail_page():
    return render_template('pages/intro_animation.html', type="Cocktail Party",
                           goto_url="cocktail", image="cocktail.jpg")


@app.route('/cocktail', methods=['POST', 'GET'])
def cocktail():
    if request.method == 'GET':
        return render_template('pages/cocktail.html')
    elif request.method == 'POST':
        side_dish = request.form['side dish']
        alcoholic = request.form['Alcoholic']
        main_ingredient = (request.form['Main Ingredient'],)
        preferable_glasses = request.form.getlist('Preferable Glasses')
        max_ingredients = request.form['Max Ingredients']
        qry, snacks = sql_drink_queries.get_drink_results_by_params(alcoholic, main_ingredient,
                                                                    preferable_glasses, max_ingredients,
                                                                    side_dish)
        print(qry)
        if qry == [ ]:
            print("drink result is empty")
        else:
            print("drink result is no empty")
        print(snacks)
        print("333 check: end of cocktail in server.py")
        return render_template('results/cocktail_results.html', drinks=qry, snacks=snacks)
    else:
        return 'failed to load page or to send request'


if __name__ == "__main__":
    app.run()
