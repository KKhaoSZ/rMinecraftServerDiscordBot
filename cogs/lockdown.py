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

class lockdown(commands.Cog):

    def __init__(self, client):
        self.client = client
        
        
    guild_ids = [824394116568842290]
    
    @cog_ext.cog_slash(name="lockdown",description="Admin Command | Locks / Unlocks the channel from being seen") 
    async def lockdown(self, ctx: SlashContext):
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
        
            
            channel = ctx.channel
            
            overwrite = channel.overwrites_for(ctx.guild.default_role)

            guild = ctx.guild
            print(overwrite.send_messages)
            if overwrite.send_messages == False:
                overwrite.send_messages = True
                await ctx.channel.set_permissions(ctx.guild.default_role, overwrite = overwrite)
                await ctx.send("This channel has been unlocked.")
            else:
                overwrite.send_messages = False
                await ctx.channel.set_permissions(ctx.guild.default_role, overwrite = overwrite)
                await ctx.send("This channel has been locked.")
        elif temprole == "":
            await ctx.send("This command has not been set up yet. Please ask the owner of the server to run `/setup adminrole`",hidden=True)
        else:
            await ctx.send("You do not have permissions to use this command.")
        
        
        
        
        
        
        
        
        

        
        
        
            


        
        
            

        
        
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog lockdown is ready.")







        
def setup(client):
    client.add_cog(lockdown(client))