# Apollo-Bot
Contest Vote Engine

Test:

1.  main.py :
        This is the flask server it does the following:
            1. Recieves and records voting events
            2. Makes annoucment of a new vote in specified Discord Channel

2.  discord_bot.py:
        Discord bot which can be added to any server, it allows for the following
            1.  Users can check reults at any time in allowed server ( general, army, etc)
            2.  SubDAOs can check for result updates
            
3.  vbot.py 
        Contains all neccessary functions

4.  hooksample.py:
        This throws a simple wwbhook to simulate a vote event


**votes are stored an accessed via a free my sql database **

