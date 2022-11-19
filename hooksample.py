'''
 ***Sample Voting Event***
'''
import requests
import json

webhook_url = 'http://127.0.0.1:5000/webhook'

data ={ "Contestant Voted ":"Kenet",                       #infoemation about the vote
        "Voter Discord": "mango#4322",
        "Voter Address": "TERBV2U3B1287WEF234VKK234BV2344645EWRW4",       
        "Date and Time": "4:21 11/18/2022"
         }

r = requests.post(webhook_url, data = json.dumps(data), headers ={"Content-Type":"application/json"})
