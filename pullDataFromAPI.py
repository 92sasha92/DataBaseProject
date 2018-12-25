# importing the requests library
import requests
import json
# authentication
X_Yummly_App_ID = "e5eade25"
X_Yummly_App_Key = "b3c6badec10eed98cb5e2580a4bbffdc"

# api-endpoint
URL = "http://api.yummly.com/v1/api/recipes?_app_id={}&_app_key={}".format(X_Yummly_App_ID, X_Yummly_App_Key)

# location given here

URL += "&q=cake"

# defining a params dict for the parameters to be sent to the API
#PARAMS = {'address': location}

URL += "&maxResult=400&start=0"

#URL += "&allowedCuisine[]=cuisine^cuisine-american"
# sending get request and saving the response as response object
r = requests.get(url=URL)

print(r.url)
# extracting data in json format
data = r.json()

print(data)

with open('million_cakes_100_plus_400_no_american.json', 'w') as file:
    json.dump(data, file)
# extracting latitude, longitude and formatted address
# of the first matching location


# latitude = data['results'][0]['geometry']['location']['lat']
# longitude = data['results'][0]['geometry']['location']['lng']
# formatted_address = data['results'][0]['formatted_address']
print("DONE")
# printing the output
#print("Latitude:%s\nLongitude:%s\nFormatted Address:%s" % (latitude, longitude,formatted_address))
