'''
 Send Webhook to discord bot for ever New vote 
'''
import requests
import json

webhook_url = 'http://127.0.0.1:5000/webhook'

data ={ "Contestant":"Kenet",
         "Votes" : "123",
         "Voter Discord": "mango#4322",
         }

r = requests.post(webhook_url, data = json.dumps(data), headers ={"Content-Type":"application/json"})
