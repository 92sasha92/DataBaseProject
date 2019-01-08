from flask import Flask, render_template, redirect, url_for, request
import sql_drink_queries

app = Flask(__name__)

#import pymysql
#import sshtunnel

#pymysql.install_as_MySQLdb()
#import MySQLdb

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
        print("hi")
        meals = [{'first': {'dish': ({'rating': 4, 'recipe_image': u'https://lh3.googleusercontent.com/Z3CpIKLjb1e8X_sr1tAjxhU4c2q4V4Kf9zAf8VdHYxqviXx-SPO3o2JAG7rGa3TdF35GSgiB4RK3S4HmQbaEyG0=s360', 'name': u'30-Minute Lighter Italian Wedding Soup', 'num_of_servings': 6, 'prep_time': 1800, 'recipe_instructions': u'http://www.girlversusdough.com/2016/01/21/30-minute-lighter-italian-wedding-soup/', 'recipe_id': u'30-Minute-Lighter-Italian-Wedding-Soup-1473974'},), 'ingredients': ({'ingredient_name': u'diced tomatoes'}, {'ingredient_name': u'egg'}, {'ingredient_name': u'grated parmesan cheese'}, {'ingredient_name': u'ground turkey'}, {'ingredient_name': u'kale'}, {'ingredient_name': u'low sodium chicken broth'}, {'ingredient_name': u'minced garlic'}, {'ingredient_name': u'olive oil'}, {'ingredient_name': u'pepper'}, {'ingredient_name': u'plain dry breadcrumbs'}, {'ingredient_name': u'salt'}, {'ingredient_name': u'yellow onion'})}}, {'first': {'dish': ({'rating': 5, 'recipe_image': u'http://lh3.ggpht.com/tJRr0owNyYhvz7S1FaBnDjWvDfZmeIrqTe5pW2rCrAl-1-14Gt_QCaH_ZGE9kGBegVe7BeRLMfRHzc8EQKq9=s360', 'name': u'Artichoke-Olive Crostini', 'num_of_servings': 4, 'prep_time': 1200, 'recipe_instructions': u'https://smittenkitchen.com/2009/04/artichoke-olive-crostini/', 'recipe_id': u'Artichoke-olive-crostini-307101'},), 'ingredients': ({'ingredient_name': u'artichoke hearts'}, {'ingredient_name': u'capers'}, {'ingredient_name': u'crusty bread'}, {'ingredient_name': u'extra virgin olive oil'}, {'ingredient_name': u'garlic clove'}, {'ingredient_name': u'green pitted olives'})}}, {'first': {'dish': ({'rating': 4, 'recipe_image': u'http://lh4.ggpht.com/MhGZaD5zf_4-d93uCPgqO7Y2TWAW3fRtvrF1jnoEpgEBKq-f_RskBPDAK6AAVAfT73eQFdR4YcH_JPJNlJY991w=s360', 'name': u'Asiago Toasts', 'num_of_servings': 4, 'prep_time': 900, 'recipe_instructions': u'http://www.yummly.co/recipe/Asiago-toasts-304500', 'recipe_id': u'Asiago-toasts-304500'},), 'ingredients': ({'ingredient_name': u'Best Foods Mayonnaise Dressing with Extra Virgin Olive Oil'}, {'ingredient_name': u'flat leaf parsley'}, {'ingredient_name': u'French baguette'}, {'ingredient_name': u'fresh oregano leaves'}, {'ingredient_name': u'garlic'}, {'ingredient_name': u'parmigiano reggiano cheese'})}}, {'first': {'dish': ({'rating': 5, 'recipe_image': u'http://lh3.googleusercontent.com/yX6yZkXUAM1op0gGo_3Vxz0Ud6h3YPPampQRr-Z5-5NUkZZJfaMaLuC2wZnQOaEbU3-Q3BxMlmgB-6ho9Q9_PL0=s360', 'name': u'Baked Parmesan Garlic Chicken Wings', 'num_of_servings': 4, 'prep_time': 2100, 'recipe_instructions': u'http://steamykitchen.com/7055-baked-parmesan-garlic-chicken-wings.html', 'recipe_id': u'Baked-Parmesan-Garlic-Chicken-Wings-512628'},), 'ingredients': ({'ingredient_name': u'blue cheese dressing'}, {'ingredient_name': u'chicken wings'}, {'ingredient_name': u'dijon mustard'}, {'ingredient_name': u'dried oregano'}, {'ingredient_name': u'dried rosemary'}, {'ingredient_name': u'extra virgin olive oil'}, {'ingredient_name': u'fresh basil'}, {'ingredient_name': u'garlic cloves'}, {'ingredient_name': u'grated parmesan cheese'}, {'ingredient_name': u'ground cumin'}, {'ingredient_name': u'sea salt'}, {'ingredient_name': u'seasoning salt'})}}, {'first': {'dish': ({'rating': 4, 'recipe_image': u'http://lh5.ggpht.com/OGQKpnOZK4ClutEyiPMB7h20v4xvdZQe57tl-HGfxUEQqKt1rigmQWkMu7jbPNQjm8lzxrK9kFHUONr_Gy34eA=s360', 'name': u'Bertolli Bruschetta', 'num_of_servings': 24, 'prep_time': 900, 'recipe_instructions': u'http://www.yummly.co/recipe/Bertolli-bruschetta-304683', 'recipe_id': u'Bertolli-bruschetta-304683'},), 'ingredients': ({'ingredient_name': u'Bertolli Extra Virgin Olive Oil'}, {'ingredient_name': u'Bertolli Tomato & Basil Sauce'}, {'ingredient_name': u'bruschetta toppings'}, {'ingredient_name': u'garlic'}, {'ingredient_name': u'loaf italian bread, cut into'})}}, {'first': {'dish': ({'rating': 4, 'recipe_image': u'http://lh4.ggpht.com/HTb_us3a_0wAXfVREadmddHn0JMSwxLPlL_iK5U0UPWo2ipzJoNUcRtgTcB5icyQjfDp0sDYnkaMDHAmn-DT8Q=s360', 'name': u'Bruschetta, Bocconcini, Basil and Prosciutto Appetizer', 'num_of_servings': 4, 'prep_time': 1500, 'recipe_instructions': u'http://iadorefood.com/recipes/bruschetta-bocconcini-basil-and-prosciutto-appetizer/', 'recipe_id': u'Bruschetta_-Bocconcini_-Basil-and-Prosciutto-Appetizer-I-Adore-Food_-203361'},), 'ingredients': ({'ingredient_name': u'bocconcini'}, {'ingredient_name': u'ciabatta'}, {'ingredient_name': u'fresh basil leaves'}, {'ingredient_name': u'prosciutto'})}}, {'first': {'dish': ({'rating': 4, 'recipe_image': u'https://lh3.googleusercontent.com/Q4W2y2JnTPNYS4uQMkDr1kQ-Kdxc7tKMZO8Cs2d2rx1PRFA4adE198rrly2VwD82hXD_YqkrOZYILS3xm6ZzwBE=s360', 'name': u'Bruschetta', 'num_of_servings': 4, 'prep_time': 1500, 'recipe_instructions': u'http://vanillaandlace.blogspot.com/2010/08/tomato-basil-two-ways.html', 'recipe_id': u'Bruschetta-1749843'},), 'ingredients': ({'ingredient_name': u'baguette'}, {'ingredient_name': u'balsamic vinegar'}, {'ingredient_name': u'extra virgin olive oil'}, {'ingredient_name': u'fresh basil leaves'}, {'ingredient_name': u'freshly ground black pepper'}, {'ingredient_name': u'garlic'}, {'ingredient_name': u'plum tomatoes'}, {'ingredient_name': u'salt'})}}, {'first': {'dish': ({'rating': 5, 'recipe_image': u'http://lh6.ggpht.com/eQ7LSFY41APBOY4P4TYrmW0LwKk2TClDFd-wHu5YIC8c7ob6BJTUxi0LXIUc_Sh6lX4aqsmrUMJ5Ie1smhzcaQ=s360', 'name': u'Bruschetta with Provolone Cheese', 'num_of_servings': 4, 'prep_time': 1020, 'recipe_instructions': u'https://www.jocooks.com/appetizers/bruschetta-with-provolone-cheese/', 'recipe_id': u'Bruschetta-with-Provolone-Cheese-Jo-Cooks-55151'},), 'ingredients': ({'ingredient_name': u'basil'}, {'ingredient_name': u'cherry tomatoes'}, {'ingredient_name': u'french bread'}, {'ingredient_name': u'garlic'}, {'ingredient_name': u'olive oil'}, {'ingredient_name': u'onion'}, {'ingredient_name': u'pepper'}, {'ingredient_name': u'provolone cheese'}, {'ingredient_name': u'salt'})}}, {'first': {'dish': ({'rating': 4, 'recipe_image': u'http://lh3.googleusercontent.com/sTaql4C934ttFfhaEaa7NJ5H5MVUa3oYwgiKp1Mu8Ao__rPIBPBo6KVjM4cLz0zqiI9Syb8YsWlM864DBrj2Ivs=s360', 'name': u'Bruschetta with Ricotta and Pesto', 'num_of_servings': 9, 'prep_time': 1800, 'recipe_instructions': u'http://www.floatingkitchen.net/bruschetta-with-ricotta-and-pesto/', 'recipe_id': u'Bruschetta-with-Ricotta-and-Pesto-1196561'},), 'ingredients': ({'ingredient_name': u'balsamic vinegar'}, {'ingredient_name': u'extra virgin olive oil'}, {'ingredient_name': u'French baguette'}, {'ingredient_name': u'grape tomatoes'}, {'ingredient_name': u'part skim ricotta cheese'}, {'ingredient_name': u'pepper'}, {'ingredient_name': u'pesto'}, {'ingredient_name': u'salt'}, {'ingredient_name': u'shallot'})}}, {'first': {'dish': ({'rating': 4, 'recipe_image': u'http://lh3.googleusercontent.com/iWag54b-ME3WWwaoLawPYu5nsGzeafXF8MJhPoiaZ49pMWAcRiIRp9Muihg_0BoyZB9JOVKgcWkaugTFe7yRaA=s360', 'name': u'Burrata Caprese Crostini with Prosciutto', 'num_of_servings': 14, 'prep_time': 2880, 'recipe_instructions': u'http://thecrumbycupcake.com/burrata-caprese-crostini-with-prosciutto/', 'recipe_id': u'Burrata-Caprese-Crostini-with-Prosciutto-1246022'},), 'ingredients': ({'ingredient_name': u'balsamic vinegar'}, {'ingredient_name': u'basil chiffonade'}, {'ingredient_name': u'burrata cheese'}, {'ingredient_name': u'ciabatta bread'}, {'ingredient_name': u'Heirloom tomatoes'}, {'ingredient_name': u'prosciutto'})}}, {'first': {'dish': ({'rating': 5, 'recipe_image': u'http://lh6.ggpht.com/STtSOzAcqWgUv169hR42ShbfK70lC7SG8nqejZnTF034ZnW-TyoPR1QNd0EVl-jNyATiOVNnO0atojJjk0WCfg=s360', 'name': u'Cheese-Stuffed Bread Sticks', 'num_of_servings': 16, 'prep_time': 2700, 'recipe_instructions': u'http://www.thekitchn.com/side-dish-recipe-cheese-stuffed-bread-sticks-165427', 'recipe_id': u'Cheese-stuffed-bread-sticks-308313'},), 'ingredients': ({'ingredient_name': u'extra virgin olive oil'}, {'ingredient_name': u'garlic powder'}, {'ingredient_name': u'kosher salt'}, {'ingredient_name': u'oregano'}, {'ingredient_name': u'part skim mozzarella'}, {'ingredient_name': u'pizza dough'}, {'ingredient_name': u'shredded parmesan cheese'}, {'ingredient_name': u'tomato sauce'})}}, {'first': {'dish': ({'rating': 5, 'recipe_image': u'http://lh4.ggpht.com/TXok4yKVDrj7TUHSfb41TAuet8P00sqUwSfW54-m3VpPwywzZ5cG6HsiVoWNtIMCPUREA4SZr5bf5pbEMpR4=s360', 'name': u'Cheese-Stuffed Meatballs', 'num_of_servings': 4, 'prep_time': 1800, 'recipe_instructions': u'http://www.foodrepublic.com/recipes/cheese-stuffed-meatballs-recipe/', 'recipe_id': u'Cheese-Stuffed-Meatballs-511771'},), 'ingredients': ({'ingredient_name': u'breadcrumbs'}, {'ingredient_name': u'egg'}, {'ingredient_name': u'garlic'}, {'ingredient_name': u'ground beef'}, {'ingredient_name': u'ground black pepper'}, {'ingredient_name': u'Italian parsley'}, {'ingredient_name': u'kosher salt'}, {'ingredient_name': u'mozzarella'}, {'ingredient_name': u'olive oil'}, {'ingredient_name': u'white onion'})}}, {'first': {'dish': ({'rating': 4, 'recipe_image': u'http://lh3.googleusercontent.com/NtWkditT78CksaIkIQ-JHhtWg6nwWNhQ4oSpvOrbv-pvnF7BnirVjf4c9776K8s7MpEkVZ814HBR3708Da0rmA=s360', 'name': u'Classic Bruschetta', 'num_of_servings': 4, 'prep_time': 1800, 'recipe_instructions': u'http://www.italianbellavita.com/2014/08/classic-bruschetta-tomatoes-basil-garli/', 'recipe_id': u'Classic-Bruschetta-1236951'},), 'ingredients': ({'ingredient_name': u'balsamic vinegar'}, {'ingredient_name': u'black pepper'}, {'ingredient_name': u'extra virgin olive oil'}, {'ingredient_name': u'fresh basil leaves'}, {'ingredient_name': u'garlic'}, {'ingredient_name': u'Italian bread'}, {'ingredient_name': u'lemon'}, {'ingredient_name': u'plum tomatoes'}, {'ingredient_name': u'sea salt'})}}, {'first': {'dish': ({'rating': 4, 'recipe_image': u'https://lh3.googleusercontent.com/dvLtbYOrZHM9Fhe7Gjw274AnIKrI8CSGELlRYuM0caKeDMWKtCs2doNC5M-tvwLLFhkOp6Yt5Zl9VKXlOlVDbQ=s360', 'name': u'Copycat Olive Garden Pasta e Fagioli Soup', 'num_of_servings': 6, 'prep_time': 3000, 'recipe_instructions': u'https://www.cookingclassy.com/olive-garden-pasta-e-fagioli-soup-copycat-recipe/', 'recipe_id': u'Copycat-Olive-Garden-Pasta-e-Fagioli-Soup-2195765'},), 'ingredients': ({'ingredient_name': u'carrots'}, {'ingredient_name': u'diced celery'}, {'ingredient_name': u'diced tomatoes'}, {'ingredient_name': u'ditalini pasta'}, {'ingredient_name': u'dried basil'}, {'ingredient_name': u'dried oregano'}, {'ingredient_name': u'dried thyme'}, {'ingredient_name': u'fresh parsley'}, {'ingredient_name': u'freshly ground black pepper'}, {'ingredient_name': u'garlic'}, {'ingredient_name': u'granulated sugar'}, {'ingredient_name': u'Great Northern Beans'}, {'ingredient_name': u'lean ground beef'}, {'ingredient_name': u'low sodium chicken broth'}, {'ingredient_name': u'marjoram'}, {'ingredient_name': u'olive oil'}, {'ingredient_name': u'red kidney beans'}, {'ingredient_name': u'romano cheese'}, {'ingredient_name': u'salt'}, {'ingredient_name': u'tomato sauce'}, {'ingredient_name': u'water'}, {'ingredient_name': u'yellow onion'})}}, {'first': {'dish': ({'rating': 4, 'recipe_image': u'http://lh6.ggpht.com/VKnS8sNVmn8uJsj8qoF78zifuAv43qRMc-HAjhHvGcGtFvshbYcVIO9qHn2bJYjkHWhm4Smb-aV7eAnoKS2_-PQ=s360', 'name': u'Creamy Artichoke Bruschetta', 'num_of_servings': 4, 'prep_time': 960, 'recipe_instructions': u'http://www.yummly.co/recipe/Creamy-artichoke-bruschetta-300061', 'recipe_id': u'Creamy-artichoke-bruschetta-300061'},), 'ingredients': ({'ingredient_name': u'grated parmesan cheese'}, {'ingredient_name': u'Hellmanns\xae or Best Foods\xae Light Mayonnaise'}, {'ingredient_name': u'Italian bread'}, {'ingredient_name': u'marinated artichoke hearts'}, {'ingredient_name': u'sun dried tomatoes in oil'})}}, {'first': {'dish': ({'rating': 5, 'recipe_image': u'http://lh6.ggpht.com/-K2J_sLSgLUX6MFbeVi63rnYL82pcj9xHU-i44Zq5uvABkRPVC1yEMLuZIGHIcCD9GtM51ijVC6vY4Ke58aX=s360', 'name': u'Crispy Baked Eggplant Fries with Marinara Dipping Sauce (aka Eggplant Parmesan Fries!)', 'num_of_servings': 2, 'prep_time': 1800, 'recipe_instructions': u'http://www.closetcooking.com/2012/09/crispy-baked-eggplant-fries-with.html', 'recipe_id': u'Crispy-baked-eggplant-fries-with-marinara-dipping-sauce-_aka-eggplant-parmesan-fries_-351171'},), 'ingredients': ({'ingredient_name': u'eggplant'}, {'ingredient_name': u'eggs'}, {'ingredient_name': u'flour'}, {'ingredient_name': u'italian seasoning'}, {'ingredient_name': u'panko breadcrumbs'}, {'ingredient_name': u'parmigiano reggiano'}, {'ingredient_name': u'pepper'}, {'ingredient_name': u'salt'})}}, {'first': {'dish': ({'rating': 4, 'recipe_image': u'http://lh4.ggpht.com/mLCIQ6uRVNQbnN3-Rlibeq9DcEEVmSWEsJS8qjUJhyN0sUzxA3nWHFHPHsalR_usCbN6HxiEQ-3nP75seV-ecyY=s360', 'name': u'Easy Mini Tortilla Pizzas', 'num_of_servings': 20, 'prep_time': 1800, 'recipe_instructions': u'http://www.thecomfortofcooking.com/2014/04/easy-mini-tortilla-pizzas.html', 'recipe_id': u'Easy-Mini-Tortilla-Pizzas-562748'},), 'ingredients': ({'ingredient_name': u'flour tortillas'}, {'ingredient_name': u'fresh parsley'}, {'ingredient_name': u'pasta sauce'}, {'ingredient_name': u'pepperoni'}, {'ingredient_name': u'shredded mozzarella cheese'})}}, {'first': {'dish': ({'rating': 4, 'recipe_image': u'http://lh3.googleusercontent.com/5YR9J7R593oswXB7i3EaxkV6Cn5XmW_CNXXiS4chAIHfYFoLVpWWLgQAtFbRlsbX0GP9d5nFc7_IkOC2LE9o=s360', 'name': u'Fresh Tomato and Ricotta Bruschetta', 'num_of_servings': 8, 'prep_time': 1200, 'recipe_instructions': u'http://www.goeatandrepeat.com/fresh-tomato-and-ricotta-bruschetta/', 'recipe_id': u'Fresh-Tomato-and-Ricotta-Bruschetta-1246168'},), 'ingredients': ({'ingredient_name': u'crusty bread'}, {'ingredient_name': u'extra virgin olive oil'}, {'ingredient_name': u'fresh basil'}, {'ingredient_name': u'garlic salt'}, {'ingredient_name': u'ground black pepper'}, {'ingredient_name': u'medium tomatoes'}, {'ingredient_name': u'part skim ricotta cheese'}, {'ingredient_name': u'red pepper flakes'}, {'ingredient_name': u'salt'})}}, {'first': {'dish': ({'rating': 5, 'recipe_image': u'http://lh4.ggpht.com/poTWP7MsD7N--m8kDAFF5z9kajhrI__pA3wZQT4Ys16B4Gn5hueeanBRuhEOWbbj0cAMw0qB8R-P4bnNutNH3g=s360', 'name': u'Fresh Tomato Bruschetta with Basil', 'num_of_servings': 16, 'prep_time': 1800, 'recipe_instructions': u'http://www.foodrepublic.com/recipes/fresh-tomato-bruschetta-with-basil-recipe/', 'recipe_id': u'Fresh-Tomato-Bruschetta-with-Basil-512210'},), 'ingredients': ({'ingredient_name': u'balsamic vinegar'}, {'ingredient_name': u'extra virgin olive oil'}, {'ingredient_name': u'fresh basil'}, {'ingredient_name': u'garlic'}, {'ingredient_name': u'Italian bread'}, {'ingredient_name': u'plum tomatoes'})}}, {'first': {'dish': ({'rating': 4, 'recipe_image': u'http://lh5.ggpht.com/xC-wqE2NVSa16KqFhZE8OLqFnAlUmoUgUQhfhRseo6xMr7lLX_d7zYrm192S4eiKpypxfE4xmFy4JZpeKj0WfQ=s360', 'name': u'Garden Fresh Bruschetta', 'num_of_servings': 4, 'prep_time': 2400, 'recipe_instructions': u'http://www.spendwithpennies.com/hollys-bruschetta/', 'recipe_id': u'Garden-Fresh-Bruschetta-760485'},), 'ingredients': ({'ingredient_name': u'baguette'}, {'ingredient_name': u'fresh basil'}, {'ingredient_name': u'fresh tomatoes'}, {'ingredient_name': u'garlic'}, {'ingredient_name': u'olive oil'}, {'ingredient_name': u'red wine vinegar'}, {'ingredient_name': u'salt'})}}, {'first': {'dish': ({'rating': 4, 'recipe_image': u'https://lh3.googleusercontent.com/q_4pBhybEOd26kKxhvna_IVad3Czi1gAP-VMEIFOpjRBMnRpWwWluWsUSjz1SwQnUEtZDCBxMjrlAFmekftZXg=s360', 'name': u'Healthy Tuscan Vegetable Soup', 'num_of_servings': 4, 'prep_time': 2400, 'recipe_instructions': u'https://www.yummyhealthyeasy.com/healthy-tuscan-vegetable-soup-easy/', 'recipe_id': u'Healthy-Tuscan-Vegetable-Soup-2197935'},), 'ingredients': ({'ingredient_name': u'cannellini beans'}, {'ingredient_name': u'celery'}, {'ingredient_name': u'chicken broth'}, {'ingredient_name': u'chopped fresh sage'}, {'ingredient_name': u'chopped fresh thyme'}, {'ingredient_name': u'diced tomatoes'}, {'ingredient_name': u'garlic'}, {'ingredient_name': u'grated parmesan cheese'}, {'ingredient_name': u'ground black pepper'}, {'ingredient_name': u'medium carrot'}, {'ingredient_name': u'olive oil'}, {'ingredient_name': u'onion'}, {'ingredient_name': u'salt'}, {'ingredient_name': u'spinach'}, {'ingredient_name': u'zucchini'})}}, {'first': {'dish': ({'rating': 4, 'recipe_image': u'https://lh3.googleusercontent.com/ZdKQMOxzK1wEuxm1ZI2x_tK85GGDWxfbfM55w5zlDbjVo9XOX5OFWxecvfBgS5QmEg1_ICHxUeQv2mkxAgiWhQ=s360', 'name': u'Hearty Italian Vegetable Beef Soup', 'num_of_servings': 11, 'prep_time': 3300, 'recipe_instructions': u'https://barefeetinthekitchen.com/italian-vegetable-beef-soup-recipe/', 'recipe_id': u'Hearty-Italian-Vegetable-Beef-Soup-2273970'},), 'ingredients': ({'ingredient_name': u'celery'}, {'ingredient_name': u'crushed tomatoes'}, {'ingredient_name': u'diced tomatoes'}, {'ingredient_name': u'dried basil'}, {'ingredient_name': u'dried oregano'}, {'ingredient_name': u'dried thyme'}, {'ingredient_name': u'freshly ground black pepper'}, {'ingredient_name': u'garlic'}, {'ingredient_name': u'green cabbage'}, {'ingredient_name': u'ground beef'}, {'ingredient_name': u'kosher salt'}, {'ingredient_name': u'medium carrot'}, {'ingredient_name': u'small yellow onion'}, {'ingredient_name': u'tomato sauce'}, {'ingredient_name': u'water'})}}, {'first': {'dish': ({'rating': 5, 'recipe_image': u'http://lh4.ggpht.com/YYD8urZL866D7ph8an4jN7csfmWKWopDKBteApxiG-FrBAycVBPtp72Km0trqA3efAZl2Z1y-zhalTqA50agYw=s360', 'name': u'Hot Caprese Dip', 'num_of_servings': 3, 'prep_time': 1500, 'recipe_instructions': u'http://www.howsweeteats.com/2010/12/hot-caprese-dip/', 'recipe_id': u'Hot-caprese-dip-333822'},), 'ingredients': ({'ingredient_name': u'basil'}, {'ingredient_name': u'fresh mozzarella'}, {'ingredient_name': u'roma tomatoes'})}}, {'first': {'dish': ({'rating': 4, 'recipe_image': u'http://lh3.ggpht.com/yKzUdNHFv7tzcNedtznB7h_l5fh45MvvAGPmAig1FV1THs_PVZq62Gc3jt8KItrPZluf7KgVXh77W69zoZWfpuM=s360', 'name': u'Italian Bread With Tomato Appetizers', 'num_of_servings': 4, 'prep_time': 960, 'recipe_instructions': u'http://www.yummly.co/recipe/Italian-bread-with-tomato-appetizers-298566', 'recipe_id': u'Italian-bread-with-tomato-appetizers-298566'},), 'ingredients': ({'ingredient_name': u'fresh basil leaves'}, {'ingredient_name': u'ground black pepper'}, {'ingredient_name': u'Italian bread'}, {'ingredient_name': u'purple onion'}, {'ingredient_name': u'tomatoes'}, {'ingredient_name': u'Wish Bone Italian Dressing'})}}, {'first': {'dish': ({'rating': 4, 'recipe_image': u'https://lh3.googleusercontent.com/f-ctaiCMrR2rg73OxAx8ZzAz4NFE-cmj3oZLghUkg22Bvmox9a6QwTKJrlgY3BOezEF8TVX47pr7DvqQlpqUvks=s360', 'name': u'Italian Bruschetta', 'num_of_servings': 4, 'prep_time': 1500, 'recipe_instructions': u'http://easyitalianrecipes.org/vegetable-recipes/italian-bruschetta-recipe/', 'recipe_id': u'Italian-Bruschetta-2062983'},), 'ingredients': ({'ingredient_name': u'french bread'}, {'ingredient_name': u'fresh basil'}, {'ingredient_name': u'garlic cloves'}, {'ingredient_name': u'olive oil'}, {'ingredient_name': u'red onion'}, {'ingredient_name': u'red wine vinegar'}, {'ingredient_name': u'roma tomatoes'}, {'ingredient_name': u'salt'})}}, {'first': {'dish': ({'rating': 4, 'recipe_image': u'https://lh3.googleusercontent.com/POboDJC3ipMRVb90gP7Ar6_UZ64sPPYDghsczroYevysqI4qn1fI5Y7TN_9kxkNpYBHWTf8f77HxA8aUH4OO=s360', 'name': u'Italian Cheese Bombs', 'num_of_servings': 4, 'prep_time': 1200, 'recipe_instructions': u'https://selfproclaimedfoodie.com/italian-cheese-bombs/', 'recipe_id': u'Italian-Cheese-Bombs-2540163'},), 'ingredients': ({'ingredient_name': u'biscuit dough'}, {'ingredient_name': u'Italian seasoning'}, {'ingredient_name': u'low moisture mozzarella'}, {'ingredient_name': u'olive oil'}, {'ingredient_name': u'parmesan cheese'}, {'ingredient_name': u'salami'})}}, {'first': {'dish': ({'rating': 4, 'recipe_image': u'https://lh3.googleusercontent.com/iITXH1rNkUmAueIQhpAJDwMyk30p1FAI8g8tVnWzfG2gDs3d4vs2Snkm0_KqP2Dw30UZhz6mkqeXjDqQsHk2h7w=s360', 'name': u'Italian Dipping Oil', 'num_of_servings': 4, 'prep_time': 3300, 'recipe_instructions': u'https://bunnyswarmoven.net/italian-dipping-oil/', 'recipe_id': u'Italian-Dipping-Oil-2557704'},), 'ingredients': ({'ingredient_name': u'balsamic vinegar'}, {'ingredient_name': u'crusty bread'}, {'ingredient_name': u'garlic'}, {'ingredient_name': u'grated parmesan cheese'}, {'ingredient_name': u'ground pepper'}, {'ingredient_name': u'olive oil'}, {'ingredient_name': u'red pepper flakes'}, {'ingredient_name': u'salt'})}}, {'first': {'dish': ({'rating': 4, 'recipe_image': u'http://lh3.googleusercontent.com/MtapWWicZqB1ditiJsDo5drRLfSGomBQpif7fF05kHjD82dhlrNJfRcmEaK4mrp9mLbHnToGmB_8T_jn_-q_ww=s360', 'name': u'Italian Pinwheels', 'num_of_servings': 4, 'prep_time': 1800, 'recipe_instructions': u'http://www.muchkneadedrecipes.com/2011/10/italian-pinwheels.html', 'recipe_id': u'Italian-Pinwheels-1267020'},), 'ingredients': ({'ingredient_name': u'cream cheese'}, {'ingredient_name': u'deli ham'}, {'ingredient_name': u'fat'}, {'ingredient_name': u'flour tortillas'}, {'ingredient_name': u'pepperoncinis'}, {'ingredient_name': u'pepperoni'}, {'ingredient_name': u'salami'})}}, {'first': {'dish': ({'rating': 4, 'recipe_image': u'https://lh3.googleusercontent.com/ACFsGSU8DMpMp0lUvhWrkIE-_plxzJP1AA6zTI38fBXULPnmvAIoCoVfxOeukRt-FDn4pJM8ZmA_BgRRIC1GVQ=s360', 'name': u'Italian Rice Balls', 'num_of_servings': 4, 'prep_time': 5100, 'recipe_instructions': u'http://easyitalianrecipes.org/snack-recipes/italian-rice-balls-recipe/', 'recipe_id': u'Italian-Rice-Balls-2063062'},), 'ingredients': ({'ingredient_name': u'dried basil'}, {'ingredient_name': u'dried breadcrumbs'}, {'ingredient_name': u'eggs'}, {'ingredient_name': u'fresh ground black pepper'}, {'ingredient_name': u'grated parmesan cheese'}, {'ingredient_name': u'low sodium chicken broth'}, {'ingredient_name': u'mozzarella cheese'}, {'ingredient_name': u'olive oil'}, {'ingredient_name': u'salt'}, {'ingredient_name': u'white rice'})}}, {'first': {'dish': ({'rating': 5, 'recipe_image': u'http://lh6.ggpht.com/cQrb4p__I3bSv8rufrcUVgE07qIgeTiStO4AHJeX9tKiR4s1tnuukN3Q3-36WzwY2pyuHTR23FzXMOdCbK2xIQ=s360', 'name': u'Italian Sausage, Tomato, and Macaroni Soup with Basil', 'num_of_servings': 7, 'prep_time': 3600, 'recipe_instructions': u'https://kalynskitchen.com/easy-recipe-for-italian-sausage-tomato/', 'recipe_id': u'Italian-sausage_-tomato_-and-macaroni-soup-with-basil-309363'},), 'ingredients': ({'ingredient_name': u'dried basil'}, {'ingredient_name': u'fennel'}, {'ingredient_name': u'fresh basil'}, {'ingredient_name': u'grated parmesan cheese'}, {'ingredient_name': u'homemade chicken stock'}, {'ingredient_name': u'italian sausage'}, {'ingredient_name': u'macaroni'}, {'ingredient_name': u'minced garlic'}, {'ingredient_name': u'olive oil'}, {'ingredient_name': u'onion'}, {'ingredient_name': u'tomatoes with juice'})}}, {'first': {'dish': ({'rating': 4, 'recipe_image': u'https://lh3.googleusercontent.com/nnTiloaDefUx721TSPnqMmZe5QpZI0X8FaNR0byt8VPFEit-b1JQyw4ExU_mjLRxIJbxl3kd4Rwae-Be1NQ0=s360', 'name': u'Italian Wedding Soup with Chicken Meatballs', 'num_of_servings': 6, 'prep_time': 4800, 'recipe_instructions': u'http://www.goodlifeeats.com/italian-wedding-soup-with-chicken-meatballs/', 'recipe_id': u'Italian-Wedding-Soup-with-Chicken-Meatballs-1923004'},), 'ingredients': ({'ingredient_name': u'balsamic vinegar'}, {'ingredient_name': u'black pepper'}, {'ingredient_name': u'breadcrumbs'}, {'ingredient_name': u'carrots'}, {'ingredient_name': u'celery'}, {'ingredient_name': u'chicken broth'}, {'ingredient_name': u'diced tomatoes'}, {'ingredient_name': u'fresh parsley'}, {'ingredient_name': u'fresh spinach'}, {'ingredient_name': u'garlic'}, {'ingredient_name': u'garlic powder'}, {'ingredient_name': u'grated parmesan'}, {'ingredient_name': u'ground chicken'}, {'ingredient_name': u'italian seasoning'}, {'ingredient_name': u'italian seasonings'}, {'ingredient_name': u'medium eggs'}, {'ingredient_name': u'olive oil'}, {'ingredient_name': u'orzo'}, {'ingredient_name': u'salt'}, {'ingredient_name': u'water'}, {'ingredient_name': u'yellow onion'})}}, {'first': {'dish': ({'rating': 3, 'recipe_image': u'https://lh3.googleusercontent.com/67ZycFd1YbAcNK-c-Ll0jRr7sQQTRsvCOIf5fsC_zEIr0-fTCq90Kp6UMdoEDITNrDj538_o0YPLiNLYzPXnWA=s360', 'name': u'Italian Wedding Soup With Escarole', 'num_of_servings': 8, 'prep_time': 22500, 'recipe_instructions': u'http://www.bhg.com/recipe/soups/italian-wedding-soup-with-escarole/', 'recipe_id': u'Italian-Wedding-Soup-With-Escarole-2447038'},), 'ingredients': ({'ingredient_name': u'carrots'}, {'ingredient_name': u'dry bread crumbs'}, {'ingredient_name': u'eggs'}, {'ingredient_name': u'escarole'}, {'ingredient_name': u'finely chopped onion'}, {'ingredient_name': u'flat leaf parsley'}, {'ingredient_name': u'fresh oregano'}, {'ingredient_name': u'grated parmesan cheese'}, {'ingredient_name': u'ground black pepper'}, {'ingredient_name': u'lean ground beef'}, {'ingredient_name': u'pasta'}, {'ingredient_name': u'reduced sodium chicken broth'}, {'ingredient_name': u'salt'}, {'ingredient_name': u'vegetable oil'})}}, {'first': {'dish': ({'rating': 5, 'recipe_image': u'http://lh3.ggpht.com/DFQQ9s8XVQ5wfndsF_x7G69XfdoAIHD_x1rTiRyxONwk6aCp1EqjIzt7jw3fPp_xn0UncRI98cuIiwSe4Cpecg=s360', 'name': u'Kale and Roasted Vegetable Soup', 'num_of_servings': 6, 'prep_time': 5100, 'recipe_instructions': u'http://www.simplyrecipes.com/recipes/kale_and_roasted_vegetable_soup/', 'recipe_id': u'Kale-and-Roasted-Vegetable-Soup-Simply-Recipes-42872'},), 'ingredients': ({'ingredient_name': u'bay leaf'}, {'ingredient_name': u'butternut squash'}, {'ingredient_name': u'carrots'}, {'ingredient_name': u'garlic cloves'}, {'ingredient_name': u'great northern white beans'}, {'ingredient_name': u'kale'}, {'ingredient_name': u'olive oil'}, {'ingredient_name': u'onion'}, {'ingredient_name': u'thyme sprigs'}, {'ingredient_name': u'tomatoes'}, {'ingredient_name': u'vegetable broth'})}}]

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


@app.route('/cocktail', methods=['POST', 'GET'])
def cocktail():
    if request.method == 'GET':
        return render_template('pages/cocktail.html')
    elif request.method == 'POST':
        side_dish = request.form['side dish']
        alcoholic = request.form['Alcoholic']
        main_ingredient = (request.form['Main Ingredient'],)
        preferable_glasses = request.form.getlist('Preferable Glasses')
        qry = sql_drink_queries.get_drink_results_by_params(alcoholic, main_ingredient, preferable_glasses, 0)
        print(qry)
        return render_template('cocktail_results.html', drinks=qry)
    else:
        return 'failed to load page or to send request'


if __name__ == "__main__":
    app.run()
