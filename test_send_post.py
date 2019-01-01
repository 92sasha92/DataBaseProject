# make a POST request
import requests
dictToSend = {'question': 'what is the answer?'}
res = requests.post('http://127.0.0.1:5000/cocktail', json=dictToSend)
#print('response from server:', res.text)
#dictFromServer = res.json()
