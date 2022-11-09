import requests
import json
def results():
    #send Curent Reults
    string= 'Current Results \n 1st Contestant_Name  No_of_Votes \n  2nd Contestant_Name  No_of_Votes \n 3rd Contestant_Name  No_of_Votes' 
    return string

def NewVote():
    #new vote has been cast
    voted = " New Vote for\n Contestant_Name \n Total: No_of_Votes"
    return voted 

#create event Trigger for New Votes