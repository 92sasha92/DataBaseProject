# make a POST request
import requests
import sql_drink_queries
#dictToSend = {'question': 'what is the answer?'}
#res = requests.post('http://127.0.0.1:5000/cocktail', json=dictToSend)
#print('response from server:', res.text)
#dictFromServer = res.json()


alcoholic = "Alcoholic"
mainIngredient = ["vodka"]
preferableGlasses = ['Cocktail glass']
rows = sql_drink_queries.get_drinks_from_db(alcoholic, mainIngredient, preferableGlasses, 0)
# redirect to results page instead of just writing "RESULT PAGE"
#results = qry.fetchall()
print(rows)
for row in rows:
    print(row['is_alcoholic'])
#print(qry)