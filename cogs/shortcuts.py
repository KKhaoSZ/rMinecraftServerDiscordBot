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

class shortcuts(commands.Cog):


    def __init__(self, bot):
        self.bot = bot
    
    guild_ids = [824394116568842290]

    

    #{"error":1,"msg":"That alias is taken. Please choose another one."}

    @cog_ext.cog_slash(name="portforward",description="Information on Port Forwarding!")
    async def portfordward(self, ctx: SlashContext):
        await ctx.send("Quick tutorial how to Portforward so your friends can join! \nhttps://youtu.be/X75GbRaGzu8")
        
    @cog_ext.cog_slash(name="spigot",description="Information on how to set up a spigot server!")
    async def spigot(self, ctx: SlashContext):
        await ctx.send("Quick tutorial how to set up a Spigot Minecraft Server! \nhttps://youtu.be/lNp4I-600wo \nIt is recommended you set up a paper server! You can run the command /paper!")
        
    @cog_ext.cog_slash(name="paper",description="Information on how to set up a paper server!")
    async def paper(self, ctx: SlashContext):
        await ctx.send("Quick tutorial how to set up a Paper Minecraft Server! \nhttps://youtu.be/o3vZx0l8y_U \n")

    @cog_ext.cog_slash(name="bungeecord",description="Information on how to set up a bungeecord server!")
    async def bungeecord(self, ctx: SlashContext):
        await ctx.send("Quick tutorial how to set up a Bungeecord Minecraft Server! \nhttps://youtu.be/rhv-W6_y5nI \n")
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(self.bot.slash.commands)
        print("Cog Shortcuts is ready.")
    

    
def setup(bot):
    
    bot.add_cog(shortcuts(bot))
