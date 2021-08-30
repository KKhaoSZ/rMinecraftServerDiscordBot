from __future__ import unicode_literals
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from discord.ext import commands
import discord
import random
import asyncio
import json
import os
import time
import asyncio
from numbers import Number
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option


intents = discord.Intents.all()
intents.members = True
intents.presences = True
bot_token = "Put Token here"
bot = commands.Bot(command_prefix= '/', intents = intents)
bot.remove_command('help')  
slash = SlashCommand(bot, override_type = True, sync_commands=True, sync_on_cog_reload=True)


excluded_files = ["functions.py"]

@slash.slash(name="reload",description="Developer Command", options=[create_option(name="extension",description="The name of the extension", option_type= 3,required=True)])
async def reload (ctx, extension):
    if ctx.author.id == 268221711344730115:
        if extension == "all":
            for filename in os.listdir('./cogs'):
                if filename.endswith('.py') and not filename in excluded_files:
                    try:
                        bot.load_extension(f'cogs.{filename[:-3]}')
                    except Exception:
                        pass
            for filename in os.listdir('./cogs'):
                if filename.endswith('.py') and not filename in excluded_files:
                    try:
                        bot.unload_extension(f'cogs.{filename[:-3]}')
                    except Exception:
                        pass


        else:
            try:
                bot.unload_extension(f'cogs.{extension}')
            except Exception:
                pass
            bot.load_extension(f'cogs.{extension}')
            await ctx.send('The cog **{}** has been reloaded'.format(extension))

@bot.command()
async def disable (ctx, extension):
    if ctx.author.id == 268221711344730115:
        bot.load_extension(f'cogs.{extension}')
        await ctx.send('The cog **{}** is now disabled'.format(extension))

@bot.command()
async def enable (ctx, extension):
    if ctx.author.id == 268221711344730115:
        bot.load_extension(f'cogs.{extension}')
        await ctx.send('The cog **{}** is now enabled'.format(extension))

@bot.command()
async def list (ctx, type=""):
    if ctx.author.id == 268221711344730115:
        files = []
        if type == "cogs":
            for filename in os.listdir('./cogs'):
                if filename.endswith('.py')and not filename in excluded_files:

                    files.append(str(filename))
        else:
            for filename in os.listdir('./cogs'):
                files.append(str(filename))

        for x in files:
            files_string = ""
            for x in files:
                files_string = files_string + x + "\n"
        embed = discord.Embed(color=0x85caff)
        embed.add_field(name="Listing requested files:", value=f"{files_string}", inline=False)
        await ctx.send(embed=embed)

while True:
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py') and not filename in excluded_files:
            bot.load_extension(f'cogs.{filename[:-3]}')
        #print(bot.slash.commands)
    break

def get_status():
    with open("bot_status.json", "r") as f:
        status = json.load(f)
    return status["status"]
    
    
@slash.slash(name="botstatus",description="Change the status of the bot", options=[create_option(name="status",description="Developer Command | The status you want the bot to have", option_type= 3,required=True )])
async def botstatus (ctx, status:str):
    if ctx.author.id == authorid:
        with open ("bot_status.json", "r") as f:
            _status = json.load(f)

        _status["status"] = status

        with open ("bot_status.json", "w") as f:
            json.dump(_status, f, indent=4)

        await bot.change_presence(activity=discord.Game(name=get_status()))
        await ctx.send(f"Status has been successfully changed to: \"{status}\"")

@bot.command()
async def quit (ctx):
    if ctx.author.id == 268221711344730115:
    	await bot.close()
    
    

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=get_status()))
bot.run(bot_token)