import requests
import json

# X_Yummly_App_ID = "e5eade25"
# X_Yummly_App_Key = "b3c6badec10eed98cb5e2580a4bbffdc"
#
#
# #url = "http://api.yummly.com/v1/api/recipe/French-Onion-Soup-The-Pioneer-Woman-Cooks-_-Ree-Drummond-41364?_app_id=" + X_Yummly_App_ID + "&_app_key=" + X_Yummly_App_Key
# # r.content[28:-3] cuisine + holiday name
# # r.content[27:-3] course name
# #
# url = "http://api.yummly.com/v1/api/metadata/course?_app_id="+X_Yummly_App_ID+"&_app_key=" + X_Yummly_App_Key
#
# r = requests.get(url=url)
#
# print(r.content)

arr = {"h":1,"g":2}
if "a" not in arr:
    print("error")
else:
    print(arr["a"])

