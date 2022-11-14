import vbot
from flask import Flask, request, abort



app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
  if request.method == 'POST':
    data = request.json
    contestant = data['Contestant']
    NoofVotes = data['Votes']
    Voter = data['Voter Discord']
    message= "$New Vote \n" + Voter + " voted for "+ contestant +"\n" + "Total votes for " + contestant +"\n" + NoofVotes
    vbot.sendNewVote(message)
    return 'sucess', 200
  else:
    abort(400)


if __name__ == "__main__":
  app.run()
