
import json
# Logic

def results():
    #Get results

    #Format Curent Reults
    string= 'Current Results \n 1st Contestant_Name  No_of_Votes \n  2nd Contestant_Name  No_of_Votes \n 3rd Contestant_Name  No_of_Votes' 
    return string

#create event Trigger for New Votes
def NewVote():
    #Get Newvote

    voted = " New Vote for\n Contestant_Name \n Total: No_of_Votes"
    return voted

