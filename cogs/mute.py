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
from time import time, sleep
import pytz
import requests
import asyncpraw
import asyncprawcore
from discord.ext import tasks
import math
from functions import create

class mute(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.mutecheck.start()
    
    def cog_unload(self):
        self.mutecheck.cancel()
        
    def cog_load(self):
        self.mutecheck.start()
    
    
    
    
    guild_ids = [824394116568842290]
    
    @cog_ext.cog_slash(name="mute",description="Admin Command | Mutes the user",options=[create_option(name="user",description="Name of the person",option_type=6,required=True), create_option(name="length",description="How long the user will be muted for?",option_type=3,required=False),create_option(name="reason",description="The reason the user is being muted",option_type=3,required=False)]) 

    async def mute(self, ctx: SlashContext, user:Optional[Member]=None,length ="1d", reason="Not provided"):
        
        await ctx.defer(hidden=True)

        
        try:
        
            create._guild(ctx.guild.id)
            create._punishments(ctx.guild.id, user.id, user)

            with open ("./cogs/json/user_punishments.json", "r") as f:
                users = json.load(f)



            channel = ctx.channel
            guild = ctx.guild    

            with open ("./cogs/json/setup.json", "r") as f:
                setup = json.load(f)

            temprole = setup[str(ctx.guild.id)]["admin_role"]
            mutedrole = setup[str(ctx.guild.id)]["muted_role"]

            Perms = False
            for x in temprole:
                temp = setup[str(ctx.guild.id)]["admin_role"][x]
                role = discord.utils.get(guild.roles,id=temp)
                print(role)
                print(ctx.author.roles)
                if role in ctx.author.roles:
                    Perms = True
            
            time = length.lower()
            Time = length.replace("second", "s")
            Time = length.replace("seconds", "s")
            Time = length.replace(" ", "")
            Time = length.replace("day", "d")
            Time = length.replace("days", "d")
            Time = length.replace("minute", "m")
            Time = length.replace("minutes", "m")
            Time = length.replace("hour", "h")
            Time = length.replace("hours", "h")
            Time = length.replace("week", "w")
            Time = length.replace("weeks", "w")
            
            
            Test = False
            alphabet = ['a', 'b', 'c', 'e', 'f', 'g', 'i', 'j', 'k', 'l', 'n', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'x', 'y', 'z']
            alphabet2 = ['s', 'm', 'h', 'd', 'w']
            Test = any(ele in Time for ele in alphabet)
            Test2 = any(ele in Time for ele in alphabet2)
            if Test2 == False:
                Test = True






            if Perms and temprole != "" and mutedrole != "" and Test == False:
                with open ("./cogs/json/user_punishments.json", "r") as f:
                    users = json.load(f)

                role = discord.utils.get(guild.roles,id=mutedrole)


                if role in user.roles:
                    await ctx.send("User is already muted", hidden=True)
                else:

                    try:


                        
                        
                        


                        

                        temp = ""
                        difftimes = []
                        for x in Time:
                            if "s" in x:
                                temp = temp + "s"
                                difftimes.append(temp)
                                temp = ""
                            elif "d" in x:
                                temp = temp + "d"
                                difftimes.append(temp)
                                temp = ""
                            elif "m" in x:
                                temp = temp + "m"
                                difftimes.append(temp)
                                temp = ""
                            elif "h" in x:
                                temp = temp + "h"
                                difftimes.append(temp)
                                temp = ""
                            elif "w" in x:
                                temp = temp + "w"
                                difftimes.append(temp)
                                temp = ""
                            else:
                                temp = temp + x






                        OriginalTime = ""
                        TrueTime = 0

                        i_seconds = 0
                        i_minutes = 0
                        i_hours = 0
                        i_days = 0
                        i_weeks = 0


                        for x in difftimes:
                            temp = ""
                            Seconds = 0



                            if "s" in x:
                                temp = x.replace("s","")
                                i_seconds += int(temp)
                                Seconds += int(temp)
                            elif "d" in x:

                                temp = x.replace("d","")
                                i_days += int(temp)
                                Seconds += int(temp) * 86400
                            elif "h" in x:

                                temp = x.replace("h","") 
                                i_hours += int(temp)
                                Seconds += int(temp) * 3600
                            elif "m" in x:

                                temp = x.replace("m","")
                                i_minutes += int(temp)
                                Seconds += int(temp) * 60
                            elif "w" in x:

                                temp = x.replace("w","")
                                i_weeks += int(temp)
                                Seconds += int(temp) * 86400 * 7
                            
                            
                            
                            OriginalTime = ""
                            if i_weeks != 0:
                                if i_days != 0 and i_hours != 0 and i_minutes != 0 and i_seconds != 0:
                                    OriginalTime = OriginalTime + f"{i_weeks} week(s), "
                                else:
                                    OriginalTime = OriginalTime + f"{i_weeks} week(s)"
                            if i_days != 0:
                                if i_weeks != 0 and i_hours != 0 and i_minutes != 0 and i_seconds != 0:
                                    OriginalTime = OriginalTime + f"{i_days} day(s), "
                                else:
                                    OriginalTime = OriginalTime + f"{i_days} day(s)"
                            if i_hours != 0:
                                if i_weeks != 0 and i_days != 0 and i_minutes != 0 and i_seconds != 0:
                                    OriginalTime = OriginalTime + f"{i_hours} hour(s), "
                                else:
                                    OriginalTime = OriginalTime + f"{i_hours} hour(s)"
                            if i_minutes != 0:
                                if i_weeks != 0 and i_days != 0 and i_hours != 0 and i_seconds != 0:
                                    OriginalTime = OriginalTime + f"{i_minutes} minute(s), "
                                else:
                                    OriginalTime = OriginalTime + f"{i_minutes} minute(s)"
                            if i_seconds != 0:

                                OriginalTime = OriginalTime + f"{i_seconds} second(s)"
                            TrueTime += Seconds










                        await user.add_roles(role)
                        print()
                        Number = int(len(users[str(ctx.guild.id)][str(user.id)]['mutes']))
                        Number += 1

                        reason = reason.capitalize()
                        reason = ' '.join(reason.split())




                        await ctx.send(f"{user.mention} is now muted.", hidden=True)
                        await channel.send(f"{user.mention} has been muted for {OriginalTime} by {ctx.author}. Reason: {reason}")
                        #try:
                            #await user.send(f"You have muted for {OriginalTime} by {ctx.author}. Reason: {reason}")
                        #except Exception:
                            #pass
                        reason = str(reason) + f" | Muted by {ctx.author}"
                        users[str(ctx.guild.id)][str(user.id)]['mutes'][Number] = reason

                        with open ("./cogs/json/user_punishments.json", "w") as f:
                            json.dump(users, f, indent=4)





                        with open ("./cogs/json/mute_list.json", "r") as f:
                            muted_list = json.load(f)
                        if not str(ctx.guild.id) in muted_list:
                            muted_list[str(ctx.guild.id)] = {}

                        DateTime = datetime.now()
                        DateTime = DateTime.timestamp()
                        muted_list[str(ctx.guild.id)][str(user.id)] = {}
                        muted_list[str(ctx.guild.id)][str(user.id)]["date_muted"] = DateTime

                        muted_list[str(ctx.guild.id)][str(user.id)]["seconds"] = TrueTime





                        with open ("./cogs/json/mute_list.json", "w") as f:
                            json.dump(muted_list, f, indent = 4)


                    except Exception as e:
                        print(f"Mute Command failed. Exception at {e}")
                        
            elif Test == True:
                await ctx.send("Formatting is incorrect. Did you put the time format correctly? Ex: 1d or 1weeks2days?")
            elif temprole == "":
                await ctx.send("This command has not been set up yet. Please ask the owner of the server to run `/setup adminrole`",hidden=True)
            else:
                await ctx.send("You do not have permissions to use this command.")
        except Exception as e:
            print(f"Mute Command failed. Exception at {e}")
    @tasks.loop(seconds=5.0)
    async def mutecheck(self):
        
        with open ("./cogs/json/mute_list.json", "r") as f:
            PeopleMuted = json.load(f)
        try:
            counter = 0
            for x in PeopleMuted.keys():
                for y in PeopleMuted[str(x)]:
                    CurrentTime = datetime.now()
                    CurrentTime = CurrentTime.timestamp()
                    OldDate = PeopleMuted[str(x)][str(y)]["date_muted"]
                    OldDate = int(math.floor(float(OldDate)))
                    OldTime = PeopleMuted[str(x)][str(y)]["seconds"]
                    OldTime = int(OldTime)

                    guild = x
                    guildtest = x

                    guild = self.client.get_guild(int(guild))
                    
                    with open ("./cogs/json/setup.json", "r") as f:
                        setup = json.load(f)
                        


                    temprole = setup[x]["muted_role"]




                    if CurrentTime <= (OldDate + OldTime):
                        
                        user = await guild.fetch_member(int(y))
                        try:
                            
                            role = discord.utils.get(guild.roles,id=temprole)
                            if not role in user.roles:
                                await user.add_roles(role)

                        except Exception:
                            print("Code Failed")
                    else:

                        user = await guild.fetch_member(int(y))
                        try:
                            role = discord.utils.get(guild.roles,id=temprole)
                            await user.remove_roles(role)
                            print(f"Role has been removed from {user}")
                            await user.send(f"You are now unmuted from {guild}")
                        except Exception:
                            pass

                        PeopleMuted[x].pop(y, None)
                        with open ("./cogs/json/mute_list.json", "w") as f:
                            json.dump(PeopleMuted, f, indent=4)
        except RuntimeError as e:        
            pass

        except Exception as e:
            has_guild = False
            for x in self.client.guilds:
                if x.id == int(guildtest):
                    has_guild = True
            if has_guild == True:
                print(f"MuteCheck went wrong somewhere, Exception: {f}")
            else:
                with open ("./cogs/json/mute_list.json", "r") as f:
                    PeopleMuted = json.load(f)
                PeopleMuted.pop(guildtest, None)
                with open ("./cogs/json/mute_list.json", "w") as f:
                    json.dump(PeopleMuted, f, indent=4)
            
            
            
        
        
        

        
        
    @cog_ext.cog_slash(name="unmute",description="Admin Command | Unmutes the user",options=[create_option(name="user",description="Name of the person",option_type=6,required=True)]) 

    async def unmute(self, ctx: SlashContext, user:Optional[Member]=None):
        await ctx.defer(hidden=True)
        
        with open ("./cogs/json/user_punishments.json", "r") as f:
            users = json.load(f)
                
        guild = ctx.guild 
        with open ("./cogs/json/setup.json", "r") as f:
            setup = json.load(f)

        create._guild(ctx.guild.id)
        
        mutedrole = setup[str(ctx.guild.id)]["muted_role"]
        
        muted_role = discord.utils.get(guild.roles,id=mutedrole)
        
        temprole = setup[str(ctx.guild.id)]["admin_role"]
        
        Perms = False
        for x in temprole:
            temp = setup[str(ctx.guild.id)]["admin_role"][x]
            role = discord.utils.get(guild.roles,id=temp)
            if role in ctx.author.roles:
                Perms = True
        
        if Perms and temprole != "":
            if muted_role in user.roles:
                await user.remove_roles(muted_role)

                await ctx.send("User has been successfully unmuted", hidden=True)
            else:
                await ctx.send("User is already unmuted", hidden=True)
        elif temprole == "":
            await ctx.send("This command has not been set up yet. Please ask the owner of the server to run `/setup adminrole`",hidden=True)
        else:
            await ctx.send("You do not have permissions to use this command.")
            
        
            

        
        
        
        
        
        
            


        
        
            

        
        
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog Mute is ready.")







        
def setup(client):
    client.add_cog(mute(client))