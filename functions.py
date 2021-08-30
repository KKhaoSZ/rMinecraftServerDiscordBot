from __future__ import unicode_literals
import discord
from discord import Member
from typing import Optional
from discord.ext import commands
from discord.ext.commands import Cog, Greedy
from discord.utils import get
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

class create():
    
    def __init__(self, client):
        self.client = client
 

    def _guild(guildid):
        guildid = str(guildid)

        items = ["admin_role", "muted_role", "reddit_channel", "punishments_channel", "message_update_channel", "join_leave_channel", "user_update_channel", "server_update_channel"]
        
        with open ("./cogs/json/setup.json", "r") as f:
            setup = json.load(f)

        if not guildid in setup:
            setup[guildid] = {}
        
        for x in items:
            if not x in setup[guildid]:
                if x == "admin_role":
                    setup[guildid][x] = {}
                else:
                	setup[guildid][x] = ""

        with open ("./cogs/json/setup.json", "w") as f:
            json.dump(setup,f,indent=4)







    def _punishments(guildid, userid, username):
        guildid = str(guildid)
        userid = str(userid)
        items = ["warns", "mutes", "kicks", "bans", "username"]

        with open ("./cogs/json/user_punishments.json", "r") as f:
            users = json.load(f)
        
        if not str(userid) in users:
            users[guildid] = {}
            users[guildid][userid] = {}
        
        for x in items:
            if x == "username":
                users[guildid][userid]['username'] = str(username)
            else:
                users[guildid][userid][x]= {}
                
                

        with open ("./cogs/json/user_punishments.json", "w") as f:
            json.dump(users,f,indent=4)
        
    
    
    
    async def _sendpunishlog(self, module, user, guild, author, reason="Not Provided",time=""):
        with open ("./cogs/json/stored_logs.json", "r") as f:
            logs = json.load(f)
        
        with open ("./cogs/json/setup.json", "r") as f:
            setup = json.load(f)
        
        guildid = guild
        
        if not str(guildid) in logs:
            logs[str(guildid)] = {}
        if not "cases" in logs[str(guildid)]:
            logs[str(guildid)]["cases"] = {}
            
        guild = self.client.get_guild(int(guildid))
        channel = self.client.get_channel(str(setup[str(guildid)]["punishments_channel"]))
        
        
        counter = len(logs[str(guildid)]["cases"]) + 1
        logs[str(guildid)]["cases"][counter] = {}
        
        text = ""
        
        if reason == "Not Provided":
            combinedreason = f"Not Provided, use `/log reason {counter} <text>` to specify a reason."
        else:
            combinedreason = reason
        
        if module == "mute":
            mod = "Mute"
            text = f"**Offender:** {user} aka {user.mention}\n**Duration:** {time}\n**Reason:** {combinedreason}\n**Muted by:** {user}"
            
        elif module =="ban":
            mod = "Ban"
        elif module == "kick":
        	mod = "Kick"
        elif module == "unmute":
            mod = "Unmute"
        
        embed = discord.Embed(title = f"{mod} | Case #{counter}", description = text)
        await channel.send(embed)
        
    def _counting(guildid):
        guildid = str(guildid)

        items = ["total_users"]
        
        with open ("./cogs/json/counting.json", "r") as f:
            counting = json.load(f)

        if not str(guildid) in counting:
            counting[guildid] = {}
        
        for x in items:
            if not x in setup[guildid]:
                counting[guildid][x] = 0

        with open ("./cogs/json/counting.json", "w") as f:
            json.dump(counting,f,indent=4)
    