# importing the requests library
import requests
import json
import MySQLdb
import mysql_queries
# authentication
X_Yummly_App_ID = "e5eade25"
X_Yummly_App_Key = "b3c6badec10eed98cb5e2580a4bbffdc"

# api-endpoint
base_url = "http://api.yummly.com/v1/api/recipes"
base_metadata_url = "http://api.yummly.com/v1/api/metadata/"
base_url_auth = "?_app_id={}&_app_key={}".format(X_Yummly_App_ID, X_Yummly_App_Key)
recipe_id = '0'
api_by_id_url = base_url + recipe_id + base_url_auth
print(api_by_id_url)