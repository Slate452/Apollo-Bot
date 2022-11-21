'''
 ***Sample Voting Event***
'''
import requests
import json

webhook_url = 'https://kene452.pythonanywhere.com/webhook'

data ={ "Contestant Voted":"Tfab",                       #infoemation about the vote
        "Voter Discord": "MEchww#3161",
        "Voter Address": "her23F556234VKK234BV2344645qweF16",       
        "Date and Time": "4:21 11/18/2022"
         }

r = requests.post(webhook_url, data = json.dumps(data), headers ={"Content-Type":"application/json"})
