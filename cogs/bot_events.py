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
from datetime import datetime, timedelta, date
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

class bot_events(commands.Cog):

    def __init__(self, client):
        self.client = client

        
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog Events is ready.")
        
        
    @commands.Cog.listener()
    async def on_guild_join(self, guild): 
        create._guild(guild.id)
        create._counting(str(guild.id))
        
        with open ("./cogs/json/counting.json", "r") as f:
            counting = json.load(f)
        
        counting[str(guild.id)] = guild.member_count
        
        with open ("./cogs/json/counting.json", "w") as f:
            json.dump(counting,f,indent=4)
        
def setup(client):
    client.add_cog(bot_events(client))    