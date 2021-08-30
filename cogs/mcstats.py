from __future__ import unicode_literals
from mcstatus import MinecraftServer
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
import socket
from mcipc.query import Client
from PIL import Image
from io import BytesIO

class mcstats(commands.Cog):

    def __init__(self, client):
        self.client = client


    guild_ids= [824394116568842290]
        
        
    @cog_ext.cog_slash(name="status",description="Gives the status of a Minecraft Server",options=[create_option(name="ip",description="The IP of the server",option_type=3,required=True), create_option(name="port",description="The port of the IP",option_type=4,required=False)])
    async def status(self, ctx:SlashContext, ip, port=25565):
        if port != 25565:  
            website = f"https://api.mcsrvstat.us/2/{ip}:{port}"
            img = f"https://api.mcsrvstat.us/icon/{ip}:{port}"
        else:
            website = f"https://api.mcsrvstat.us/2/{ip}"
            img = f"https://api.mcsrvstat.us/icon/{ip}"
        response = requests.get(website)
        online = response.json()["online"]
        
        TimeZone = datetime.now(pytz.timezone('UTC')) 
        TimeZone = TimeZone.astimezone(pytz.timezone('US/Pacific'))
        dt_string = TimeZone.strftime("%m/%d/%Y | %I:%M:%S %p")
        
        if online == True:
            OriginalIP = response.json()["ip"]
            OriginalPort = response.json()["port"]
            Players = response.json()["players"]
            PlayersOnline = Players["online"]
            PlayersMax = Players["max"]
            MOTD = response.json()["motd"]
            motd = MOTD["clean"]
            
            
            
            motd = [x.strip(' ') for x in motd]
            motd = str('\n'.join(motd))
            motdmodify = ["§0", "§1", "§2", "§3", '§4', '§5', '§6', '§7', '§8', '§9', '§10', '§l', '§r', '§k', '§m', '§n', '§o', '§b', '§i', '§c', '§e', '§a', '§b', '§f', '§e', '§f', '\u00A70', '\u00A71', '\u00A72', '\u00A73', '\u00A74', '\u00A75', '\u00A76', '\u00A77', '\u00A78', '\u00A79','\u00A7a','\u00A7b','\u00A7c','\u00A7d','\u00A7e','\u00A7f','\u00A7k','\u00A7l','\u00A7m','\u00A7n','\u00A7o','\u00A7r']
            while "§" in motd:
                for x in motdmodify:
                    if x in motd:
                        motd = motd.replace(x, "")
            
            
            
            try:
                ListPlayers = response.json()["players"][0]["list"]
                Temp = ListPlayers
                ListPlayers = ""
                for x in Temp:
                    ListPlayers = ListPlayers + f"{x}\n"
            except Exception:
                ListPlayers = "Player names could not be detected"
            try:
                ServerType = response.json()["software"]
            except Exception:
                ServerType = "Server type could not be detected"
            try:
                Plugins = response.json()["plugins"]
                Temp = Plugins["names"]
                Plugins = ""
                for x in Temp:
                    Plugins = Plugins + f"{x}\n"
            except Exception:
                Plugins = "Plugins could not be detected"

            try:
                Mods = response.json()["mods"]
                Temp = Mods["names"]
                Plugins = ""
                for x in Temp:
                    Mods = Mods + f"{x}\n"
            except Exception:
                Mods = "Mods could not be detected"
            
            Version = response.json()["version"]
            
            
            
            embed = discord.Embed(color = 0x28ca07)
            embed.add_field(name=f"Server Status for {ip.upper()}", value=f"**Status:** Online \n**Version:** {Version} \n **Server Type:** {ServerType}\n**Motd:** *{motd}*\n**Original IP:** {OriginalIP}\n**Port:** {OriginalPort} \n**Player Count:** {PlayersOnline}/{PlayersMax} \n**Players in server:** \n*{ListPlayers}*", inline=False)
            embed.set_footer(text=f"In Beta | Last checked: {dt_string} PST | Requested by {ctx.author}")
            embed.set_thumbnail(url=img)
            print(embed)
            await ctx.send(embeds=[embed])
            
            
        
            
            
            
            
        else:
            embed = discord.Embed(color = 0xff0000)
            embed.add_field(name=f"Server Status for {ip.upper()}", value=f"Status: Offline \n• Did you the server's numerical IP? If so, please try using the domain name instead.\n• If you put in a number for the Port option, you may have entered in the wrong port. Leaving it blank should be fine.\n", inline=False)
            embed.set_footer(text=f"In Beta | Last checked: {dt_string} PST | Requested by {ctx.author}")
            embed.set_thumbnail(url=img)
            await ctx.send(embeds=[embed])
        
        
        
        
        
        
        
        
        
        
        
        
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog MCStats is ready.")







        
def setup(client):
    client.add_cog(mcstats(client))