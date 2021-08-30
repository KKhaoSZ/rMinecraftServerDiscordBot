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


class userinfo(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    
    
    
    
    guild_ids = [824394116568842290]
    
    @cog_ext.cog_slash(name="members",description="Admin Command | Gives information about the punished members on this server",options=[create_option(name="number",description="The number of the user (refer to the general list) you want information on",option_type=4,required=False)])
     
    async def members(self, ctx: SlashContext, number=0):
        await ctx.defer(hidden=True)
        
        with open ("./cogs/json/user_punishments.json", "r") as f:
                users = json.load(f)
        

        
        if number == 0:
            counter = 1
            text = ""
            for x in users[str(ctx.guild.id)]:
                _username = users[str(ctx.guild.id)][x]["username"]
                _numofmutes = len(users[str(ctx.guild.id)][x]["mutes"])
                _numofkicks = len(users[str(ctx.guild.id)][x]["kicks"])
                _numofbans = len(users[str(ctx.guild.id)][x]["bans"])
                _numofwarns = len(users[str(ctx.guild.id)][x]["warns"])
                text = text + f"`{counter}. {_username} - W: {_numofwarns}, M: {_numofmutes}, K: {_numofkicks}, B: {_numofbans}`\n"
                counter += 1
            channel = ctx.channel
            await ctx.send(text)
        else: 
            text = ""
            counter = 1
            for x in users[str(ctx.guild.id)]:
                if counter == number:
                    trueuser = x
                    break
                else:
                    counter += 1
            
            _mutes = ""
            _kicks = ""
            _bans = ""
            _username = ""
            
            if len(users[str(ctx.guild.id)][trueuser]['mutes']) != 0:
                for x in users[str(ctx.guild.id)][trueuser]['mutes']:
                    _mutes = _mutes + f"\n- {users[str(ctx.guild.id)][trueuser]['mutes'][str(x)]}"
            else:
                _mutes = "\nNo mutes have been given"
            
            
            if len(users[str(ctx.guild.id)][trueuser]['kicks']) != 0:    
                for x in users[str(ctx.guild.id)][trueuser]['kicks']:
                    _kicks = _kicks + f"\n- {users[str(ctx.guild.id)][trueuser]['kicks'][str(x)]}"
            else:
                _kicks = "\nNo kicks have been given"
                
                
            if len(users[str(ctx.guild.id)][trueuser]['bans']) != 0:
                for x in users[str(ctx.guild.id)][trueuser]['bans']:
                    _bans = _bans + f"\n- {users[str(ctx.guild.id)][trueuser]['bans'][str(x)]}"
            else:
                _bans = "\nNo bans have been given"
                
                
            _username = users[str(ctx.guild.id)][trueuser]['username']
            if counter == number:
                text = text + f"```All punishments for {_username}:\n\nMutes: {_mutes}\n\nKicks: {_kicks}\n\nBans: {_bans}```"
            else:
                text = "The number you provided is not in the database. A player must have been warned, muted, kicked, or banned in order to be on the list."
              
            await ctx.send(text)
                                                                                                            
                                                                                                            
                                                                                                            
      
        
       
        

        
        
            

        
        
        
        
        
        
            


        
        
            

        
        
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog User Info is ready.")







        
def setup(client):
    client.add_cog(userinfo(client))