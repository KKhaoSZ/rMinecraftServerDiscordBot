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
from functions import create


class ban(commands.Cog):

    def __init__(self, client):
        self.client = client
    
   
    
    
    guild_ids = [824394116568842290]
    
    @cog_ext.cog_slash(name="ban",description="Admin Command | Bans the user",options=[create_option(name="user",description="Name of the person",option_type=6,required=False), create_option(name="reason",description="The reason the user is being banned",option_type=3,required=False)]) 
    async def ban(self, ctx: SlashContext, user:Optional[Member]=None, reason="Not provided"):
        await ctx.defer(hidden=True)
        
        
        create._guild(ctx.guild.id)
        
        with open ("./cogs/json/setup.json", "r") as f:
            setup = json.load(f)
        
        
        temprole = setup[str(ctx.guild.id)]["admin_role"]
        
        role = discord.utils.get(ctx.guild.roles,id=temprole)
        
        Perms = False
        for x in temprole:
            temp = setup[str(ctx.guild.id)]["admin_role"][x]
            role = discord.utils.get(ctx.guild.roles,id=temp)
            if role in ctx.author.roles:
                Perms = True
        
        if Perms and temprole != "":

            with open ("./cogs/json/user_punishments.json", "r") as f:
                    users = json.load(f)



            channel = ctx.channel
            guild = ctx.guild    
            if user == None:
                counter = 1
                _text = ""
                for x in users[str(ctx.guild.id)]:
                    if len(users[str(ctx.guild.id)][x]["bans"]) == 0:
                        counter += 1
                    else:
                        _username = users[str(ctx.guild.id)][x]["username"]
                        _text = _text + f"`{counter}. {_username}`"
                        counter += 1
                if _text == "":
                    text = f"No one has banned yet."
                else:
                	text = f"People who are currently banned:\n{_text}"
                await ctx.send(text)
            elif role in user.roles or ctx.author.top_role <= user.top_role:
                ctx.send("This person cannot be banned.")
            else:
                
                create._punishments(ctx.guild.id, user.id, user)
                
                Number = len(users[str(ctx.guild.id)][str(user.id)]['bans'])
                Number += 1

                reason = reason.capitalize()
                reason = ' '.join(reason.split())

                await ctx.send(f"{user} is now banned.", hidden=True)
                await channel.send(f"{user} has been banned by {ctx.author}. Reason: {reason}")


                await user.send(f"You have been banned by {ctx.author}. Reason: {reason}")
                await ctx.guild.ban(user, reason=reason)
                reason = str(reason) + f" | Banned by {ctx.author}"
                users[str(ctx.guild.id)][str(user.id)]['bans'][Number] = reason

                with open ("./cogs/json/user_punishments.json", "w") as f:
                    json.dump(users, f, indent=4)
        elif temprole == "":
            await ctx.send("This command has not been set up yet. Please ask the owner of the server to run `/setup adminrole`",hidden=True)
        else:
            await ctx.send("You do not have permissions to use this command.")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    @cog_ext.cog_slash(name="unban",description="Admin Command | Unbans the user",options=[create_option(name="number",description="The number of the person (do /unban to refer to the list)",option_type=3,required=False)]) 

    async def unban(self, ctx: SlashContext, number = 0):
        await ctx.defer(hidden=True)
        try:
            number = int(number)
        except:
            pass
        
        with open ("./cogs/json/setup.json", "r") as f:
                setup = json.load(f)
        

        
        temprole = setup[str(ctx.guild.id)]["admin_role"]
        role = discord.utils.get(ctx.guild.roles,name=temprole)
        
        
            
        with open ("./cogs/json/user_punishments.json", "r") as f:
                users = json.load(f)
                
        guild = ctx.guild 
        
        Perms = False
        for x in temprole:
            temp = setup[str(ctx.guild.id)]["admin_role"][x]
            role = discord.utils.get(guild.roles,id=temp)
            if role in ctx.author.roles:
                Perms = True

        if Perms and temprole != "":
            counter = 1
            if number != 0:
                try:
                	user = await self.client.fetch_user(number)
                except Exception:
                    user = None
                if user == None:
                    for x in users[str(ctx.guild.id)]:
                        if counter == number:
                            trueuser = x
                            break
                        else:
                            counter += 1 
                    _trueuser = await self.client.fetch_user(trueuser)
                    await ctx.guild.unban(_trueuser)
                    await ctx.send("User has been successfully unbanned", hidden=True)
                else:
                    await ctx.guild.unban(user)
                    await ctx.send("User has been successfully unbanned", hidden=True)
            else:
                counter = 1
                _text = ""
                for x in users[str(ctx.guild.id)]:
                    if len(users[str(ctx.guild.id)][x]["bans"]) == 0:
                        counter += 1
                    else:
                        _username = users[str(ctx.guild.id)][x]["username"]
                        _text = _text + f"`{counter}. {_username}`"
                        counter += 1
                if _text == "":
                    text = f"No one has banned yet."
                else:
                	text = f"People who are currently banned:\n{_text}"
                await ctx.send(text)
                      
                    
                        
                
            	
        elif temprole == "":
            await ctx.send("This command has not been set up yet. Please ask the owner of the server to run `/setup adminrole`",hidden=True)
        else:
            await ctx.send("You do not have permissions to use this command.")
            
        
            

        
        
        
        
        
        
            


        
        
            

        
        
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog Ban is ready.")







        
def setup(client):
    client.add_cog(ban(client))