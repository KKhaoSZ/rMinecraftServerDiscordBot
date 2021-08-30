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

class purge(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    guild_ids = [824394116568842290]
    
    @cog_ext.cog_subcommand(base="purge",name = "general", description="Admin Command | Delete overall messages",options=[create_option(name="limit",description="The amount of messages you want to delete",option_type=4,required=True), create_option(name="allmsgs",description="Warning: This deletes all messages from the CHANNEL, not the server.",option_type=5,required=False), create_option(name="user",description="Delete messages from specific user",option_type=6,required=False)])     
    
    async def purge_general(self, ctx: SlashContext, limit=5, allmsgs=False, user:Optional[Member]=None):
        channel = ctx.channel
        messages = []
        counter = 0
        
        await ctx.defer(hidden=True)
        create._guild(ctx.guild.id)
        
        def username(message):
            return message.author == user
        
        with open ("./cogs/json/setup.json", "r") as f:
            setup = json.load(f)
        
        temprole = setup[str(ctx.guild.id)]["admin_role"]
        
        Perms = False
        for x in temprole:
            temp = setup[str(ctx.guild.id)]["admin_role"][x]
            role = discord.utils.get(ctx.guild.roles,id=temp)
            if role in ctx.author.roles:
                Perms = True
        if Perms and temprole != "":
            if user == None:
                if allmsgs == True:
                    messages = await channel.history(limit=None).flatten()
                else:
                    messages = await channel.history(limit=limit).flatten()

                for message in messages:
                    counter += 1
                    await message.delete()
                await ctx.send(f"Successfully deleted {counter} messages")
            else:

                if allmsgs == True:
                    messages = await channel.history(limit=None).filter(username).flatten()
                    for message in messages:
                        counter += 1
                        await message.delete()
                else:

                    messages = await channel.history(limit=None).filter(username).flatten()
                    counter = 0
                    for message in messages:
                        if counter != limit:
                            await message.delete()
                            counter += 1
                        else:
                            break
                await ctx.send(f"Successfully deleted {counter} messages from {user.mention}")
        elif temprole == "":
            await ctx.send("This command has not been set up yet. Please ask the owner of the server to run `/setup adminrole`",hidden=True)
        else:
            await ctx.send("You do not have permissions to use this command.")




    @cog_ext.cog_subcommand(base="purge",name = "detailed", description="Admin Command | Delete specific messages",options=[create_option(name="limit",description="The amount of messages you want to delete",option_type=4,required=True), create_option(name="keywords",description="The keywords you want to be deleted (seperate the words or phrases with commas)",option_type=3,required=True), create_option(name="allmsgs",description="Warning: This deletes all messages from the CHANNEL, not the server.",option_type=5,required=False), create_option(name="user",description="Delete messages from specific user",option_type=6,required=False)])     
    
    async def purge_detailed(self, ctx: SlashContext, limit=5, keywords = "" , allmsgs=False,user:Optional[Member]=None):
        channel = ctx.channel
        messages = []
        counter = 0
        
        await ctx.defer(hidden=True)
        create._guild(ctx.guild.id)
        
        def username(message):
            return message.author == user
        
        with open ("./cogs/json/setup.json", "r") as f:
            setup = json.load(f)
        
        temprole = setup[str(ctx.guild.id)]["admin_role"]


        key = []
        keywords = keywords.lower()
        if keywords != "":
            temp = ""
            for x in keywords:
                if x == ",":
                    if temp == "":
                        pass
                    else:
                        key.append(temp)
                        temp = ""
                else:
                    temp = temp + x
        if len(key) == 0:
            key.append(temp)
        


        Perms = False
        for x in temprole:
            temp = setup[str(ctx.guild.id)]["admin_role"][x]
            role = discord.utils.get(ctx.guild.roles,id=temp)
            if role in ctx.author.roles:
                Perms = True
        if Perms and temprole != "":
            if user == None:
                counter = 0
                messages = await channel.history(limit=None).flatten()

                for message in messages:
                    if counter == limit:
                        break
                    else:
                        for x in key:
                            if x in str(message.content).lower():
                                counter += 1
                                await message.delete()
                                break
                await ctx.send(f"Successfully deleted {counter} messages with the keywords: {keywords}")
            else:
                counter = 0
                if allmsgs == True:
                    messages = await channel.history(limit=None).filter(username).flatten()
                    for message in messages:
                        for x in key:
                            if x in str(message.content).lower():
                                counter += 1
                                await message.delete()
                                break
                    await ctx.send(f"Successfully deleted {counter} messages with the keywords: {keywords}")
                else:

                    messages = await channel.history(limit=None).filter(username).flatten()
                    counter = 0
                    for message in messages:
                        if counter == limit:
                            break
                        else:
                            for x in key:
                                if x in str(message.content).lower():
                                    counter += 1
                                    await message.delete()
                                    break
                    await ctx.send(f"Successfully deleted {counter} messages with the keywords: {keywords}")
        elif temprole == "":
            await ctx.send("This command has not been set up yet. Please ask the owner of the server to run `/setup adminrole`",hidden=True)
        else:
            await ctx.send("You do not have permissions to use this command.")

        
        
            

        
        
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog Purge is ready.")







        
def setup(client):
    client.add_cog(purge(client))