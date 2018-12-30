# importing the requests library
import requests
import json
import MySQLdb
import mysql_queries

conn = MySQLdb.connect(host="mysqlsrv1.cs.tau.ac.il",
                      user="DbMysql06",
                      passwd="DbMysql06",
                      db="DbMysql06")

# authentication
X_Yummly_App_ID = "e5eade25"
X_Yummly_App_Key = "b3c6badec10eed98cb5e2580a4bbffdc"

# api-endpoint
base_url = "http://api.yummly.com/v1/api/recipes?"
base_metadata_url = "http://api.yummly.com/v1/api/metadata/"
base_url_auth = "?_app_id={}&_app_key={}".format(X_Yummly_App_ID, X_Yummly_App_Key)


def insert_from_metadata_api_to_db(metadata_name, table_name, col_name, file_name):
    file = open(file_name+".json", "w")
    metadata = []
    metadata_url = base_metadata_url + metadata_name + base_url_auth
    print(metadata_url)
    r = requests.get(url=metadata_url)
    res_full_data = r.content
    json_start_idx = res_full_data.find('[')
    json_end_idx = res_full_data.rfind(']')
    data = res_full_data[json_start_idx:(json_end_idx+1)]
    file.write(data)
    file.close()
    search_by = 'name'
    if metadata_name == "ingredient":
        search_by = 'term'
    json_data = json.loads(data)
    for obj in json_data:
        obj_name = obj[search_by]
        metadata.append(obj_name)
        # add ingredient names to DB
        mysql_queries.insert_name_to_db(table_name, obj_name, col_name, conn)
    return metadata


cuisines = insert_from_metadata_api_to_db("cuisine", "Cuisines", "cuisine_name", "cuisine_output")

insert_from_metadata_api_to_db("course", "Courses", "course_name", "course_output")
insert_from_metadata_api_to_db("holiday", "Holidays", "holiday_name", "holiday_output")
insert_from_metadata_api_to_db("ingredient", "Ingredients", "ingredient_name", "ingredient_output")
#
# # defining a params dict for the parameters to be sent to the API
# for cuisine in cuisines:
#     api_url = base_url + base_url_auth + "&requirePictures=true&maxResult=800&start=0&allowedCuisine[]=cuisine^cuisine-" + cuisine
#     # sending get request and saving the response as response object
#     r = requests.get(url=api_url)
#     # extracting data in json format
#     recipes_by_cuisine = r.json()
#     for match in recipes_by_cuisine['matches']:
#         # get expanded data of the current recipe
#         recipe_id = match['id']
#         recipe_cuisines = match['attributes']['cuisine']
#         ingredients = match['ingredients']
#         mysql_queries.insert_multi_data_to_db("ListOfCuisines", recipe_cuisines, recipe_id, "cuisine_name", conn)
#         mysql_queries.insert_multi_data_to_db("ListOfIngredients", ingredients, recipe_id, "ingredient_name", conn)
#         if 'holiday' in match['attributes']:
#             holidays = match['attributes']['holiday']
#             mysql_queries.insert_multi_data_to_db("ListOfHolidays", holidays, recipe_id, "holiday_name" , conn)
#         if 'course' in match['attributes']:
#             courses = match['attributes']['course']
#             mysql_queries.insert_multi_data_to_db("ListOfCourses", courses, recipe_id, "course_name", conn)
#
#         api_by_id_url = base_url + recipe_id + base_url_auth
#         r = requests.get(url=api_by_id_url)
#         recipe_data = r.json()
#         recipe_name = recipe_data['name']
#         recipe_img_url = recipe_data['images']['hostedLargeUrl']
#         recipe_instructions_url = recipe_data['source']['sourceRecipeUrl']
#         prep_time = recipe_data['totalTimeInSeconds']
#         num_of_servings = recipe_data['numberOfServings']
#         rating = recipe_data['rating']

conn.close()

