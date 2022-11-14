
from discord_webhook import DiscordWebhook, DiscordEmbed

def sendNewVote(string):
  webhook = DiscordWebhook(url ='boturl',username = 'Contest Bot', content = string)
  embed = DiscordEmbed(title = "**New Vote**", color = 242424 )
  embed.set_image(url ="https://bafybeidvu3oxafwvop5evgualfysymch3y3lqllcfq6dchhyziu7cuqtt4.ipfs.nftstorage.link/f0dc1e96194e11e4a6a4a8febbefacaa3acfa54c8d439ecf6f4ac577104c9c0c.png")
  webhook.add_embed(embed)  
  reponse = webhook.execute()


    


