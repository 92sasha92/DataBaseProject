from flask import Flask, render_template, redirect, url_for, request
import sql_drink_queries
import mysql_recipe_queries
import sql_holiday_queries
import sql_romantic_queries

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('first_page.html')


@app.route('/home_page')
def home_page():
    return render_template('pages/main_page.html')


@app.route('/ethnic_cuisines_start')
def ethnic_cuisines_page():
    return render_template('pages/ethnic_cuisines_start.html')


@app.route('/ethnic_cuisines', methods=['POST', 'GET'])
def ethnic_cuisines():
    if request.method == 'GET':
        return render_template('pages/ethnic_cuisines.html')
    elif request.method == 'POST':
        prep_time = request.form['Maximum Preparation Time']
        type_of_meals = request.form.getlist('Type Of Meal')
        cuisine = request.form['Cuisine']

        meals = mysql_recipe_queries.get_ethnic_meal_results_by_params(prep_time, type_of_meals, cuisine)
        print(meals)
        return render_template('ethnic_cuisines_results.html', meals=meals)
    else:
        return 'failed to load page or to send request'


@app.route('/picnic_start')
def picnic_page():
    return render_template('pages/picnic_start.html')


@app.route('/picnic')
def picnic_cuisines():
    return render_template('pages/picnic.html')


@app.route('/holiday_start')
def holiday_page():
    return render_template('pages/holiday_start.html')


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
        return render_template('holiday_results.html', meals=meals, num_of_dishes=number_of_dishes)
    else:
        return 'failed to load holiday result page or to send request'


@app.route('/romantic_start')
def romantic_page():
    return render_template('pages/romantic_start.html')


@app.route('/romantic', methods=['POST', 'GET'])
def romantic():
    if request.method == 'GET':
        return render_template('pages/romantic.html')
    elif request.method == 'POST':
        prep_time = int(request.form['Maximum Preparation Time'])
        main_ingredient = request.form['Main Ingredient']
        side_ingredient = request.form['Side Ingredient']
        dessert = request.form['Dessert']
        meals = sql_romantic_queries.get_romantic_meal_results_by_params(main_ingredient, side_ingredient, dessert, prep_time)
        return render_template('holiday_results.html', meals=meals)
    else:
        return 'failed to load page or to send request'


@app.route('/breakfast_start')
def breakfast_page():
    return render_template('pages/breakfast_start.html')


@app.route('/breakfast', methods=['POST', 'GET'])
def breakfast():
    if request.method == 'GET':
        return render_template('pages/breakfast.html')
    elif request.method == 'POST':
        typeOfBreakfast = request.form['Type Of Breakfast']
        numberOfSalads = request.form['Number Of Salads']
        typeOfBread = request.form['Type Of Bread']
        return 'RESULT PAGE'
    else:
        return 'failed to load page or to send request'


@app.route('/bbq_start')
def bbq_page():
    return render_template('pages/bbq_start.html')


@app.route('/bbq', methods=['POST', 'GET'])
def bbq():
    if request.method == 'GET':
        return render_template('pages/bbq.html')
    elif request.method == 'POST':
        kindOfMeat = request.form['Kind Of Meat']
        numberOfSideDishes = request.form['Number Of Side Dishes']
        vegan = request.form['Vegan']
        return 'RESULT PAGE'
    else:
        return 'failed to load page or to send request'


@app.route('/birthday_start')
def birthday_page():
    return render_template('pages/birthday_start.html')


@app.route('/birthday', methods=['POST', 'GET'])
def birthday():
    if request.method == 'GET':
        return render_template('pages/birthday.html')
    elif request.method == 'POST':
        #print("in  POST")
        prepTime = request.form['Maximum Preparation Time']
        numOfGuests = request.form['Number Of Guests']
        includeChildren = request.form['with children']
        season = request.form['Time']
        cakeFlavor = request.form.getlist('Cake Flavor')
        special = request.form.getlist('Special')
        allergy = request.form.getlist('Allergy')

        #redirect to results page instead of just writing "RESULT PAGE"
        return 'RESULT PAGE'
    else:
        return 'failed to load page or to send request'


@app.route('/cocktail_start')
def cocktail_page():
    return render_template('pages/cocktail_start.html')


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
        print(snacks)
        return render_template('cocktail_results.html', drinks=qry, snacks=snacks)
    else:
        return 'failed to load page or to send request'


if __name__ == "__main__":
    app.run()
