# importing the requests library
import requests
import json
import MySQLdb
import mysql_queries


def insert_cocktails():
    conn = MySQLdb.connect(host="mysqlsrv1.cs.tau.ac.il",
                           user="DbMysql06",
                           passwd="DbMysql06",
                           db="DbMysql06",
                           use_unicode=True, charset="utf8")

    drinks_types = ['Ordinary_Drink', 'Cocktail']
    base_url = "https://www.thecocktaildb.com/api/json/v1/1/"
    filter_url = 'filter.php?c='
    lookup_url = 'lookup.php?i='

    # defining a params dict for the parameters to be sent to the API
    for drinkType in drinks_types:
        api_url = base_url + filter_url + drinkType
        # sending get request and saving the response as response object
        r = requests.get(url=api_url)
        # extracting data in json format
        drinks = json.loads(r.content)
        for drink in drinks['drinks']:
            drink_id = drink['idDrink']
            api_drink_url = base_url + lookup_url + drink_id
            # sending get request and saving the response as response object
            res = requests.get(url=api_drink_url)
            # extracting data in json format
            drink_details = json.loads(res.content)
            drink_details = drink_details['drinks'][0]
            drink_name = drink_details['strDrink']
            drink_category = drink_details['strCategory']
            drink_image = drink_details['strDrinkThumb']
            instructions = drink_details['strInstructions']
            glass = drink_details['strGlass']
            is_alcoholic = drink_details['strAlcoholic']
            mysql_queries.insert_drink_to_db(drink_id, drink_name, drink_category,
                                             drink_image, instructions, glass, is_alcoholic, conn)
            for i in range(1, 15):
                drink_ingredient = drink_details['strIngredient%d' % i]
                drink_measure = drink_details['strMeasure%d' % i]
                if drink_ingredient == "" or (drink_ingredient is None)\
                        or drink_measure == ""\
                        or (drink_measure is None):
                    break
                drink_ingredient = drink_ingredient.replace("'", "")
                drink_ingredient = drink_ingredient.replace("-", " ")
                drink_measure = drink_measure.replace("'", "")
                drink_measure = drink_measure.replace("-", " ")
                drink_ingredient = drink_ingredient.rstrip()
                drink_measure = drink_measure.rstrip()
                mysql_queries.insert_drink_ingredient_to_db(drink_ingredient, drink_measure, conn)
                mysql_queries.insert_to_drink_ingredient_list_db(drink_id, drink_ingredient, drink_measure, conn)

    conn.close()


insert_cocktails()
