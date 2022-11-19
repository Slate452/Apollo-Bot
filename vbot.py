'''
*Vote Server*

*****functions******

  1. SendNewVote:
      This fuctions sends a discord webhook to the announcement channel in the ApolloDAO server

  2. Add Vote:
      This Records new votes to the database 

  3. Results:
      Returns the Top3 Candidates and Votes
 
'''

from discord_webhook import DiscordWebhook, DiscordEmbed
import mysql.connector as connt
#connect votes database

votes = connt.connect(
  host = "sql7.freesqldatabase.com", 
  user = "sql7578616",
  passwd ="EV9nXHHLAM", 
  database = "sql7578616"
  )

#send Webhook to annoncement Channel
def sendNewVote(string):
  webhook = DiscordWebhook(url ='boturl',username = 'Contest Bot', content = string)
  embed = DiscordEmbed(title = "**New Vote**", color = 242424 )
  embed.set_image(url ="https://bafybeidvu3oxafwvop5evgualfysymch3y3lqllcfq6dchhyziu7cuqtt4.ipfs.nftstorage.link/f0dc1e96194e11e4a6a4a8febbefacaa3acfa54c8d439ecf6f4ac577104c9c0c.png")
  webhook.add_embed(embed)  
  reponse = webhook.execute()
  return

#register Vote in DataBase
def Addvote(voters_discord, voters_wallet, Contestant, Date_Time ):
  vote = votes.cursor()
  sql = f"INSERT INTO `Votes` (`Voters_Discord`, `Voters Wallet`, `Contestant`) VALUES ({voters_discord}, {voters_wallet}, {Contestant});"
  vote.execute(sql)
  votes.commit()

#get current Results
def Reults():
  contestants = votes.cursor
  # get Contestants 
  Announce_results = "Current Results \n"
  sql2 = "SELECT `Contestant`, COUNT(*) AS `count` FROM `Votes` GROUP BY `Contestant` ORDER BY `count` DESC LIMIT 3" 
  contestants.execute(sql2)
  for i in contestants:
      print(i)
      votes = str(i[1])
      contestant = str(i[0])
      Announce_results = Announce_results + f" Contestant {contestant} with {votes} votes" +"\n"
  votes.commit()
  
  return Announce_results




    


