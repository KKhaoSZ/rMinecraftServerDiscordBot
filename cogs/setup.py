from __future__ import unicode_literals
import discord
from discord import Member
from typing import Optional
from discord.ext import commands
from discord.ext.commands import Cog, Greedy, CheckFailure
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
from time import time, sleep
import pytz
import requests
import asyncpraw
import asyncprawcore
from discord.ext import tasks
import math
from functions import create

class botsetup(commands.Cog):

    def __init__(self, client):
        self.client = client

    

    @cog_ext.cog_subcommand(base="setup", name="adminrole", description="Server Owner Command | Adds/Removes an Admin role to manage bot commands", options = [create_option(name="choice",description="Add of remove roles for the bot",option_type=3,required=True,choices= [create_choice(name="add",value="add"),create_choice(name="remove",value="remove")]), create_option(name="role",description="The role you want to add / remove",option_type=8,required=True)])
    async def setup_adminrole(self, ctx: SlashContext, choice, role):
        await ctx.defer(hidden=True)
        create._guild(ctx.guild.id)
        if ctx.author == ctx.guild.owner or ctx.author.id == 268221711344730115:
            with open ("./cogs/json/setup.json", "r") as f:
                    setup = json.load(f)

            
            
            
            
            counter = len(setup[str(ctx.guild.id)]["admin_role"])
            check = False
            if choice == "add":
                for x in setup[str(ctx.guild.id)]["admin_role"]:
                    if role.id == setup[str(ctx.guild.id)]["admin_role"][x]:
                        check = True
                
                if check == True:
                    await ctx.send(f"{role.mention} is already added!")
                else:
                    setup[str(ctx.guild.id)]["admin_role"][str(counter + 1)] = role.id
                    await ctx.send(f"{role.mention} can now use my bot commands!")
            else:
                
                for x in setup[str(ctx.guild.id)]["admin_role"]:
                    if role.id == setup[str(ctx.guild.id)]["admin_role"][x]:
                        check = True
                
                if check == True:
                    setup[str(ctx.guild.id)]["admin_role"].pop(str(role.id), None)
                    await ctx.send(f"{role.mention} can no longer use my bot commands!")
                else:
                    await ctx.send(f"{role.mention} never had access!")
                    
                
                
                

            with open ("./cogs/json/setup.json", "w") as f:
                json.dump(setup, f, indent=4)
            
        else:
            await ctx.send("You do not have permissions to run this command.")

    @cog_ext.cog_subcommand(base="setup", name="mutedrole", description="Server Owner Command | Sets up the Muted role", options=[create_option(name="role",description="The role you want to set as the Muted Role",option_type=8,required=True)])
    async def setup_mutedrole(self, ctx: SlashContext, role):
        await ctx.defer(hidden=True)
        create._guild(ctx.guild.id)
        if ctx.author == ctx.guild.owner or ctx.author.id == 268221711344730115:
            with open ("./cogs/json/setup.json", "r") as f:
                    setup = json.load(f)

            
            setup[str(ctx.guild.id)]["muted_role"] = role.id

            with open ("./cogs/json/setup.json", "w") as f:
                json.dump(setup, f, indent=4)
            await ctx.send(f"Muted Role has been set to {role.mention}!")
            
        else:
            await ctx.send("You do not have permissions to run this command.")
            
            
    @cog_ext.cog_subcommand(base="setup", name="reddit_channel", description="Server Owner Command | Sets up the subreddit feed", options=[create_option(name="channel",description="The channel you want the bot to post to",option_type=7,required=True)])
    async def setup_redditchannel(self, ctx: SlashContext, channel):
        await ctx.defer(hidden=True)
        
        if ctx.author == ctx.guild.owner or ctx.author.id == 268221711344730115:
            create._guild(ctx.guild.id)
            with open ("./cogs/json/setup.json", "r") as f:
                setup = json.load(f)

            
            setup[str(ctx.guild.id)]["reddit_channel"] = channel.id

            await ctx.send(f"Reddit Channel has been set to {channel.mention}!")

            with open ("./cogs/json/setup.json", "w") as f:
                json.dump(setup, f, indent=4)
        else:
            await ctx.send("You do not have permissions to run this command.")
            

    @cog_ext.cog_subcommand(base="setup", name="logs", description="Server Owner Command | Sets up the logs", options=[create_option(name="log_type",description="The type of log you want to have",option_type=3,choices=[create_choice(name="punishments",value="punishments"),create_choice(name="message_update",value="message_update"),create_choice(name="join/leave",value="join/leave"),create_choice(name="user_updates",value="user_updates"),create_choice(name="server_updates",value="server_updates")],required=True), create_option(name="channel",description="The channel you want the bot to post to",option_type=7,required=True)])
    async def setup_logs(self, ctx: SlashContext, log_type="", channel=""):
        await ctx.defer(hidden=True)
        if ctx.author == ctx.guild.owner or ctx.author.id == 268221711344730115:
            create._guild(ctx.guild.id)
            with open ("./cogs/json/setup.json", "r") as f:
                setup = json.load(f)

            
            if log_type == "punishments":
                setup[str(ctx.guild.id)]["punishments_channel"] = channel.id
                await ctx.send(f"Punishments logs has been set to channel: {channel.mention}")
            elif log_type == "message_update":
                setup[str(ctx.guild.id)]["message_update_channel"] = channel.id
                await ctx.send(f"Message Update logs has been set to channel: {channel.mention}")
            elif log_type == "join/leave":
                setup[str(ctx.guild.id)]["join_leave_channel"] = channel.id
                await ctx.send(f"Join / Leave logs has been set to channel: {channel.mention}")
            elif log_type == "user_updates":
                setup[str(ctx.guild.id)]["user_update_channel"] = channel.id
                await ctx.send(f"User Update logs has been set to channel: {channel.mention}")
            elif log_type == "server_updates":
                setup[str(ctx.guild.id)]["server_update_channel"] = channel.id
                await ctx.send(f"Server Update logs has been set to channel: {channel.mention}")
                
            with open ("./cogs/json/setup.json", "w") as f:
                json.dump(setup, f, indent=4)
        else:
            await ctx.send("You do not have permissions to run this command.")            
            
            
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog Setup is ready.")







        
def setup(client):
    client.add_cog(botsetup(client))