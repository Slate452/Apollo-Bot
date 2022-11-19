'''
 ***Sample Voting Event***
'''
import requests
import json

webhook_url = 'http://127.0.0.1:5000/webhook'

data ={ "Contestant Voted":"Tfab",                       #infoemation about the vote
        "Voter Discord": "manda#4432",
        "Voter Address": "TE4E57768HT4556234VKK234BV2344645EWRW4",       
        "Date and Time": "4:21 11/18/2022"
         }

r = requests.post(webhook_url, data = json.dumps(data), headers ={"Content-Type":"application/json"})
