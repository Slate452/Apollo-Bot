import ContestMonitor as CM
import discord
import os 

def run_discord_bot():
    OauthToken = '<TOKEN>'
    intents = discord.Intents.all()
    client = discord.Client(intents=intents) 

    @client.event
    async def on_ready():
        print("Running as {0.user}".format(client))

    

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
    
        if message.content.lower().startswith('$results'):            
            user_name= str(message.author)
            user_message = str(message.content)
            channel = str(message.channel)
            print(f"{user_name} said: '{user_message}' in ({channel}) ")
            await message.channel.send(file = discord.File('contestPoster.png'))
            await message.channel.send(CM.results())
            

    client.run(OauthToken) 



    