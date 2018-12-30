# importing the requests library
import requests
import json
import MySQLdb
import mysql_queries


def insert_cocktails():
    conn = MySQLdb.connect(host="mysqlsrv1.cs.tau.ac.il",
                           user="DbMysql06",
                           passwd="DbMysql06",
                           db="DbMysql06")

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
        drinks = r.json()
        for drink in drinks:
            drink_id = drink['idDrink']
            api_drink_url = base_url + lookup_url + drink_id
            # sending get request and saving the response as response object
            res = requests.get(url=api_drink_url)
            # extracting data in json format
            drink_details = res.json()
            drink_name = drink_details['strDrink']
            drink_category = drink_details['strCategory']
            drink_image = drink_details['strDrinkThumb']
            instructions = drink_details['strInstructions']
            glass = drink_details['strGlass']
            mysql_queries.insert_drink_to_db(drink_id, drink_name, drink_category,
                                             drink_image, instructions, glass, conn)
            for i in range(1, 15):
                drink_ingredient = drink_details['strIngredient{}'.format(i)]
                drink_measure = drink_details['strMeasure{}'.format(i)]
                if drink_ingredient == "":
                    break
                mysql_queries.insert_drink_ingredient_to_db(drink_ingredient, drink_measure)
                mysql_queries.insert_to_drink_ingredient_list_db(drink_id, drink_ingredient, drink_measure)

    conn.close()
