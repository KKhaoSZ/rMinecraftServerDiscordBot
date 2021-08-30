from __future__ import unicode_literals
import discord
from discord import Member
from typing import Optional
from discord.ext import commands
from discord.ext.commands import Cog, Greedy
from discord_slash import cog_ext, SlashContext, SlashCommand
import discord_slash
from discord_slash.utils.manage_commands import create_option, create_choice
import random
from discord.voice_client import VoiceClient
from datetime import datetime, timedelta
import asyncio
import json
import os
import time
import pytz
import requests
import asyncpraw
import asyncprawcore
from discord.ext import tasks
from functions import create
import traceback


class reddit(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.reddit.start()
    
    def cog_unload(self):
        self.reddit.cancel()
        
    def cog_load(self):
        self.reddit.start()
    
    @tasks.loop(seconds=10.0)
    async def reddit(self):
        

        client_secret = "HDPvTUXsl49arDNbEDzVR5psXwjpUQ"
        client_id = "Jiqhgy61svzX9g"    
        user_agent = "r/MinecraftServer_by_KKhaoSZ"

        
        

        try:
            
            with open ("./cogs/json/setup.json", "r") as f:
                setup = json.load(f)
            
            with open ("./cogs/json/reddit.json", "r") as f:
                last_post = json.load(f)
            

            guildtest = None
        
            for x in setup:
                guild = x
                guildtest = x
                reddit_channel = setup[x]["reddit_channel"]
                try:
                    reddit_channel = int(redditchannel)
                except Exception:
                    pass
                
                
                
            
            
            
                reddit = asyncpraw.Reddit(client_id=client_id, client_secret=client_secret,user_agent=user_agent)
                subreddit = await reddit.subreddit("minecraftserver", fetch=True)
                new = subreddit.new(limit=1)

                with open ("./cogs/json/reddit.json", "r") as f:
                    last_post = json.load(f)

                if not x in last_post:
                    last_post[x] = ""




                async for submission in subreddit.new(limit=1):
                    subid = submission.id
                    url = submission.url
                    author = submission.author
                    flair = submission.link_flair_text
                    title = submission.title
                    description = submission.selftext
                    time = submission.created_utc
                    Time = submission.created
                    description = description[0:2047]
                    title = title[0:250]



                if last_post[x] == subid:
                    pass
                else:
                    parsed_date = datetime.utcfromtimestamp(time)
                    year = parsed_date.year
                    month = parsed_date.month
                    day = parsed_date.day

                    last_post[x] = subid

                    TimeZone = datetime.now(pytz.timezone('UTC')) 
                    TimeZone = TimeZone.astimezone(pytz.timezone('US/Pacific'))
                    dt_string = TimeZone.strftime("%m/%d/%Y | %I:%M:%S %p")
                    
                    if not "http" in url:
                        url = "https://www.reddit.com/r/MinecraftServer/new/"

                    embed = discord.Embed(title=f"**{title}**",url=f"{url}",description=f"{description}",color=0x00ff00, timestamp = datetime.utcnow())
                    embed.set_author(name="New Post on r/MinecraftServer")


                    embed.set_footer(text=f"Author: u/{author} • Flair: {flair}")

                    channel = self.client.get_channel(reddit_channel)
                    if channel != None:
                        await channel.send(embed=embed)

                    with open ("./cogs/json/reddit.json", "w") as f:
                        json.dump(last_post, f, indent=4)

                await reddit.close()
                await asyncio.sleep(10)
        except (requests.exceptions.RequestException, requests.exceptions.TooManyRedirects, requests.exceptions.Timeout) as exception:
            
            
            try:
                await reddit.close()
            except Exception:
                pass
        except Exception as e:
            
            try:
                if type(guildtest) == "str":
                    guildtest = int(guildtest)
            except Exception:
                guildtest = ""
            
            has_guild = False
            if guildtest != "":
                for x in self.client.guilds:
                    if x.id == int(guildtest):
                        has_guild = True
                if has_guild == True:
                    print(f"RedditCheck went wrong somewhere, Name: {type(e).__name__} | Exception: {e} | Traceback: {traceback.format_exc()}")
                else:
                    with open ("./cogs/json/setup.json", "r") as f:
                        setup = json.load(f)
                    print(setup)
                    print(guildtest)
                    setup.pop(guildtest, None)
                    print(setup)
                    with open ("./cogs/json/setup.json", "w") as f:
                        json.dump(setup, f, indent=4)
              
                    
                    
                    with open ("./cogs/json/reddit.json", "r") as f:
                        last_post = json.load(f)
                    last_post.pop(guildtest, None)
                    with open ("./cogs/json/reddit.json", "w") as f:
                        json.dump(last_post, f, indent=4)
            else:
                print(f"RedditCheck went wrong somewhere, Name: {type(e).__name__} | Exception: {e} | Traceback: {traceback.format_exc()}")
            
            
            try:
                await reddit.close()
            except Exception:
                pass
        

        
        
        
            
        
    
    

        
        
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog Reddit is ready.")







        
def setup(client):
    client.add_cog(reddit(client))