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

class kick(commands.Cog):

    def __init__(self, client):
        self.client = client
    
   
    
    
    guild_ids = [824394116568842290]
    
    @cog_ext.cog_slash(name="kick",description="Admin Command | Kicks the user",options=[create_option(name="user",description="Name of the person",option_type=6,required=True), create_option(name="reason",description="The reason the user is being kicked",option_type=3,required=False)]) 
    async def kick(self, ctx: SlashContext, user:Optional[Member]=None, reason="Not provided"):
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
            if role in user.roles or ctx.author.top_role < user.top_role:
                await ctx.send("This person cannot be kicked.")
            else:

                create._punishments(ctx.guild.id, user.id, user)

                Number = int(len(users[str(ctx.guild.id)][str(user.id)]['kicks']))
                Number += 1

                reason = reason.capitalize()
                reason = ' '.join(reason.split())

                await ctx.send(f"{user.mention} is now kicked.", hidden=True)
                await channel.send(f"{user.mention} has been kicked by {ctx.author}. Reason: {reason}")
                await user.send(f"You have been kicked by {ctx.author}. Reason: {reason}")
                reason = str(reason) + f" | Kicked by {ctx.author}"
                users[str(ctx.guild.id)][str(user.id)]['kicks'][Number] = reason
                await ctx.guild.kick(user, reason=reason)


                with open ("./cogs/json/user_punishments.json", "w") as f:
                    json.dump(users, f, indent=4)
        elif temprole == "":
            await ctx.send("This command has not been set up yet. Please ask the owner of the server to run `/setup adminrole`",hidden=True)
        else:
            await ctx.send("You do not have permissions to use this command.")
        
        
        
        
        
        
        
        
        

        
        
        
            


        
        
            

        
        
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog Kick is ready.")







        
def setup(client):
    client.add_cog(kick(client))