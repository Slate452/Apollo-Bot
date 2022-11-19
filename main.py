import vbot
from flask import Flask, request, abort



app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
  if request.method == 'POST':
    data = request.json
    Voter = data['Voter Discord'] 
    VoteTime = data['Date and Time']
    Contestant_Voted = data['Contestant Voted']
    Voters_wallet = data['Voter Address']
    
    vbot.Addvote(Voter,Voters_wallet, Contestant_Voted,VoteTime)
    Current_Results = "Top 3\n" + vbot.Results()

    message= "$New Vote \n" + Voter + " voted for "+ Contestant_Voted +"\n"

    vbot.sendNewVote(message)
    vbot.sendNewVote(Current_Results)
    return 'sucess', 200
  else:
    abort(400)


if __name__ == "__main__":
  app.run()
