import ComtestMonitor as CM
import discord
import os 


OauthToken = os.getenv(TOKEN) 
intents = discord.Intents.default()
client = discord.Client(intents=intents) 

@client.event
async def on_ready():
    print("Running as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower().startswith('results'):            
        await message.channel.send(file = discord.File('contestPoster.png'))
        await message.channel.send(CM.results())


client.run(OauthToken)