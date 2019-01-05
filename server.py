from flask import Flask, render_template, redirect, url_for, request
#import sql_drink_queries

app = Flask(__name__)

import pymysql
import sshtunnel

pymysql.install_as_MySQLdb()
import MySQLdb

#with sshtunnel.SSHTunnelForwarder(('nova.cs.tau.ac.il', 22), ssh_password='baSM9292', ssh_username='aleksandrm',
#                                 remote_bind_address=('mysqlsrv1.cs.tau.ac.il', 3306), local_bind_address=('0.0.0.0', 3306)) as server:

#conn = MySQLdb.connect(host="mysqlsrv1.cs.tau.ac.il",
              #             port=server.local_bind_port,
 #                      user="DbMysql06",
  #                     passwd="DbMysql06",
   #                    db="DbMysql06",
    #                   use_unicode=True, charset="utf8")


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
        prepTime = request.form['Maximum Preparation Time']
        typeOfMeal = request.form.getlist('Type Of Meal')
        cuisine = request.form.getlist('Cuisine')
        return 'RESULT PAGE'
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
        prepTime = request.form['Maximum Preparation Time']
        holiday= request.form['Holiday']
        numberOfDishes = request.form['Number Of Dishes']
        numberOfGuests = request.form['Number Of Guests']
        return 'RESULT PAGE'
    else:
        return 'failed to load page or to send request'

@app.route('/romantic_start')
def romantic_page():
    return render_template('pages/romantic_start.html')


@app.route('/romantic', methods=['POST', 'GET'])
def romantic():
    if request.method == 'GET':
        return render_template('pages/romantic.html')
    elif request.method == 'POST':
        prepTime = request.form['Maximum Preparation Time']
        firstPortion = request.form['First Portion']
        mainPortion = request.form['Main Portion']
        dessert = request.form['Dessert']

        return 'RESULT PAGE'
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





rows = ({'drink_image': u'https://www.thecocktaildb.com/images/media/drink/xa58bb1504373204.jpg',
         'drink_id': 11600, 'glass': u'Cocktail glass', 'is_alcoholic': u'Alcoholic',
         'drink_category': u'Ordinary Drink', 'drink_name': u'Kamikaze', 'instructions': u'Shake all ingredients together with ice. Strain into glass, garnish and serve.'},
        {'drink_image': u'https://www.thecocktaildb.com/images/media/drink/vr6kle1504886114.jpg', 'drink_id': 11872, 'glass': u'Cocktail glass', 'is_alcoholic': u'Alcoholic',
         'drink_category': u'Ordinary Drink', 'drink_name': u'Orgasm', 'instructions': u'Shake all ingredients with ice, strain into a chilled cocktail glass, and serve.'},
        {'drink_image': u'https://www.thecocktaildb.com/images/media/drink/x894cs1504388670.jpg', 'drink_id': 13625, 'glass': u'Cocktail glass', 'is_alcoholic': u'Alcoholic',
         'drink_category': u'Ordinary Drink', 'drink_name': u'Screaming Orgasm', 'instructions': u"Pour first vodka, then Bailey's, then Kahlua into a cocktail glass over crushed ice. Stir. Caution: use only high quality vodka. Cheap vodka can cause the Bailey's to curdle. Test your brand of vodka by mixing 1 Tsp each of vodka and Bailey's first."},
        {'drink_image': u'https://www.thecocktaildb.com/images/media/drink/upxxpq1439907580.jpg', 'drink_id': 14133, 'glass': u'Cocktail Glass', 'is_alcoholic': u'Alcoholic',
         'drink_category': u'Cocktail', 'drink_name': u'Cosmopolitan Martini', 'instructions': u'Pour all ingredients in mixing glass half filled with ice, shake and strain into chilled Martini glass.'},
        {'drink_image': u'https://www.thecocktaildb.com/images/media/drink/3h9wv51504389379.jpg', 'drink_id': 16176, 'glass': u'Cocktail glass', 'is_alcoholic': u'Alcoholic',
         'drink_category': u'Ordinary Drink', 'drink_name': u'Bellini Martini', 'instructions': u'Add ice cubes to shaker.\r\nAdd vodka.\r\nAdd peach schnapps.\r\nAdd peach nectar.\r\nShake.\r\nStrain into glass.\r\nAdd lemon twist peel.'},
        {'drink_image': u'https://www.thecocktaildb.com/images/media/drink/wwqvrq1441245318.jpg', 'drink_id': 16178, 'glass': u'Cocktail Glass', 'is_alcoholic': u'Alcoholic',
         'drink_category': u'Cocktail', 'drink_name': u'Jitterbug', 'instructions': u"Wet glass, dip rim in sugar. Then add Ice. Then add everything else. It's that simple!"},
        {'drink_image': u'https://www.thecocktaildb.com/images/media/drink/wtkqgb1485621155.jpg', 'drink_id': 16963, 'glass': u'Cocktail glass', 'is_alcoholic': u'Alcoholic',
         'drink_category': u'Cocktail', 'drink_name': u'Zorbatini', 'instructions': u'Prepare like a Martini. Garnish with a green olive.'},
        {'drink_image': u'https://www.thecocktaildb.com/images/media/drink/55muhh1493068062.jpg', 'drink_id': 17066, 'glass': u'Cocktail glass', 'is_alcoholic': u'Alcoholic',
         'drink_category': u'Cocktail', 'drink_name': u'Army special', 'instructions': u'Pour Vodka, Gin and lime cordial into glass, and top up with crushed ice. Wait for ice to melt slightly and sip without a straw.'},
        {'drink_image': u'https://www.thecocktaildb.com/images/media/drink/vcyvpq1485083300.jpg', 'drink_id': 17181, 'glass': u'Cocktail glass', 'is_alcoholic': u'Alcoholic',
         'drink_category': u'Cocktail', 'drink_name': u'Dirty Martini', 'instructions': u'Pour the vodka, dry vermouth and olive brine into a cocktail shaker with a handful of ice and shake well.\r\nRub the rim of a martini glass with the wedge of lemon.\r\nStrain the contents of the cocktail shaker into the glass and add the olive.\r\nA dirty Martini contains a splash of olive brine or olive juice and is typically garnished with an olive.'},
        {'drink_image': u'https://www.thecocktaildb.com/images/media/drink/n0sx531504372951.jpg', 'drink_id': 17212, 'glass': u'Cocktail glass', 'is_alcoholic': u'Alcoholic',
         'drink_category': u'Cocktail', 'drink_name': u'Espresso Martini', 'instructions': u'Pour ingredients into shaker filled with ice, shake vigorously, and strain into chilled martini glass'},
        {'drink_image': u'https://www.thecocktaildb.com/images/media/drink/clth721504373134.jpg', 'drink_id': 17213, 'glass': u'Cocktail glass', 'is_alcoholic': u'Alcoholic',
         'drink_category': u'Cocktail', 'drink_name': u'French Martini', 'instructions': u'Pour all ingredients into shaker with ice cubes. Shake well and strain into a chilled cocktail glass. Squeeze oil from lemon peel onto the drink.'},
        {'drink_image': u'https://www.thecocktaildb.com/images/media/drink/mtdxpa1504374514.jpg', 'drink_id': 17218, 'glass': u'Cocktail glass', 'is_alcoholic': u'Alcoholic',
         'drink_category': u'Cocktail', 'drink_name': u'Vesper', 'instructions': u'Shake over ice until well chilled, then strain into a deep goblet and garnish with a thin slice of lemon peel.'})




@app.route('/cocktail', methods=['POST', 'GET'])
def cocktail():
    if request.method == 'GET':
        return render_template('pages/cocktail.html')
    elif request.method == 'POST':
        side_dish = request.form['side dish']
        alcoholic = request.form['Alcoholic']
        mainIngredient = request.form['Main Ingredient']
        preferableGlasses = request.form.getlist('Preferable Glasses')
        print(side_dish+" "+alcoholic+" "+mainIngredient)
       # qry = sql_drink_queries.get_drinks_from_db(alcoholic, mainIngredient, preferableGlasses, 0)
        print(rows)
        #redirect to results page instead of just writing "RESULT PAGE"
     #   results = qry.all()
        return render_template('cocktail_results.html', rows=rows)
    else:
        return 'failed to load page or to send request'


if __name__ == "__main__":
    app.run()
