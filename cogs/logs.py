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
from dateutil import relativedelta

class logs(commands.Cog):

    def __init__(self, client):
        self.client = client

        
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog Logs is ready.")
    
    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        with open ("./cogs/json/setup.json", "r") as f:
                setup = json.load(f)
        channelid = None
        try:
            channelid = setup[str(after.id)]["server_update_channel"]
            channelid = int(channelid)
        except Exception:
            pass
        channel = self.client.get_channel(channelid)
        
        prev = []
        notprev = []
        if before.icon_url != after.icon_url:
            embed = discord.Embed(title=f"Server updated", description = "**New Icon:**", color = 0x4286F4, timestamp = datetime.utcnow())
            embed.set_image(url=after.icon_url)
            if channelid != None:
                await channel.send(embed=embed)
        embed = discord.Embed(title=f"Server updated", color = 0x4286F4, timestamp = datetime.utcnow())        
        if before.name != after.name:
            prev.append(f"**Name:** {before.name}")
            notprev.append(f"**Name:** {after.name}")
        if before.afk_channel != after.afk_channel:
            prev.append(f"**AFK Channel:** {before.afk_channel}")
            notprev.append(f"**AFK Channel:** {after.afk_channel}")
        if before.afk_timeout != after.afk_timeout:
            prev.append(f"**AFK Timeout:** {before.afk_timeout}")
            notprev.append(f"**AFK Timeout:** {after.afk_timeout}")
        if before.system_channel != after.system_channel:
            prev.append(f"**System Channel:** {before.system_channel}")
            notprev.append(f"**System Channel:** {after.system_channel}")
        if before.default_notifications != after.default_notifications:
            if str(before.default_notifications) == "NotificationLevel.all_messages":
                bnotf = "All Messages"
            else:
                bnotf = "Mentions Only"
            if str(after.default_notifications) == "NotificationLevel.all_messages":
                anotf = "All Messages"
            else:
                anotf = "Mentions Only"
            prev.append(f"**Default Notifications:** {bnotf}")
            notprev.append(f"**Default Notifications:** {anotf}")
        temp = "\n".join(prev)
        temp2 = "\n".join(notprev)
        embed.add_field(name="**Before:**", value = temp, inline = True)
        embed.add_field(name="**After:**", value = temp2, inline = True)
        embed.set_footer(text = f"Guild ID: {after.id}")
        if channel != None:
            await channel.send(embed=embed)
        
            
        
        
        
        
        
    
    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        with open ("./cogs/json/setup.json", "r") as f:
                setup = json.load(f)
        channelid = None
        try:
            channelid = setup[str(after.guild.id)]["server_update_channel"]
            channelid = int(channelid)
        except Exception:
            pass
        channel = self.client.get_channel(channelid)
        embed = discord.Embed(title=f"\"{before.name}\" role updated", color = 0x4286F4, timestamp = datetime.utcnow())
        prev = []
        notprev = []
        if before.name != after.name:
            prev.append(f"**Name:** {before.name}")
            notprev.append(f"**Name:** {after.name}")
        if before.color != after.color:
            prev.append(f"**Color:** {before.color}")
            notprev.append(f"**Color:** {after.color}")
        if before.hoist != after.hoist:
            prev.append(f"**Separated:** {before.hoist}")
            notprev.append(f"**Separated:** {after.hoist}")
        if before.mentionable != after.mentionable:
            prev.append(f"**Mentionable:** {before.mentionable}")
            notprev.append(f"**Mentionable:** {after.mentionable}")
        if before.position != after.position:
            prev.append(f"**Position:** {before.position}")
            notprev.append(f"**Position:** {after.position}")
        temp11 = '\n'.join(prev)
        temp22 = '\n'.join(notprev)
        
        
        def check(overwrite):
            if overwrite == False:
                return ":x:"
            elif overwrite == True:
                return ":white_check_mark:"
            else: 
                return ":white_large_square:"
        perms = []
        perms1 = []
        perms2 = []
        perms3 = []
        
        if before.permissions.administrator != after.permissions.administrator:
            perms.append(f"**Administrator:** {check(before.permissions.administrator)} ➜ {check(after.permissions.administrator)}")
        if before.permissions.view_channel != after.permissions.view_channel:
            perms.append(f"**View Channel:** {check(before.permissions.view_channel)} ➜ {check(after.permissions.view_channel)}")
        if before.permissions.manage_channels != after.permissions.manage_channels:
            perms.append(f"**Manage Channels:** {check(before.permissions.manage_channels)} ➜ {check(after.permissions.manage_channels)}")    
        if before.permissions.manage_roles != after.permissions.manage_roles:
            perms.append(f"**Manage Roles:** {check(before.permissions.manage_roles)} ➜ {check(after.permissions.manage_roles)}")
        if before.permissions.manage_emojis != after.permissions.manage_emojis:
            perms.append(f"**Manage Emojis:** {check(before.permissions.manage_emojis)} ➜ {check(after.permissions.manage_emojis)}")
        if before.permissions.view_audit_log != after.permissions.view_audit_log:
            perms.append(f"**View Audit Log:** {check(before.permissions.view_audit_log)} ➜ {check(after.permissions.view_audit_log)}")
        if before.permissions.manage_webhooks != after.permissions.manage_webhooks:
            perms.append(f"**Manage Webhooks:** {check(before.permissions.manage_webhooks)} ➜ {check(after.permissions.manage_webhooks)}")
        if before.permissions.manage_webhooks != after.permissions.manage_webhooks:
            perms.append(f"**Manage Webhooks:** {check(before.permissions.manage_webhooks)} ➜ {check(after.permissions.manage_webhooks)}")
        if before.permissions.manage_guild != after.permissions.manage_guild:
            perms.append(f"**Manage Server:** {check(before.permissions.manage_guild)} ➜ {check(after.permissions.manage_guild)}")
        if before.permissions.create_instant_invite != after.permissions.create_instant_invite:
            perms1.append(f"**Create Invite:** {check(before.permissions.create_instant_invite)} ➜ {check(after.permissions.create_instant_invite)}")
        if before.permissions.change_nickname != after.permissions.change_nickname:
            perms1.append(f"**Change Nickname:** {check(before.permissions.change_nickname)} ➜ {check(after.permissions.change_nickname)}")
        if before.permissions.manage_nicknames != after.permissions.manage_nicknames:
            perms1.append(f"**Manage Nicknames:** {check(before.permissions.manage_nicknames)} ➜ {check(after.permissions.manage_nicknames)}")
        if before.permissions.kick_members != after.permissions.kick_members:
            perms1.append(f"**Kick Members:**{check(before.permissions.kick_members)} ➜ {check(after.permissions.kick_members)}")
        if before.permissions.ban_members != after.permissions.ban_members:
            perms1.append(f"**Ban Members:** {check(before.permissions.ban_members)} ➜ {check(after.permissions.ban_members)}")
        if before.permissions.send_messages != after.permissions.send_messages:
            perms2.append(f"**Send Messages:** {check(before.permissions.send_messages)} ➜ {check(after.permissions.send_messages)}")
        if before.permissions.embed_links != after.permissions.embed_links:
            perms2.append(f"**Embed Links:** {check(before.permissions.embed_links)} ➜ {check(after.permissions.embed_links)}")
        if before.permissions.attach_files != after.permissions.attach_files:
            perms2.append(f"**Attach Files:** {check(before.permissions.attach_files)} ➜ {check(after.permissions.attach_files)}")
        if before.permissions.add_reactions != after.permissions.add_reactions:
            perms2.append(f"**Add Reactions:** {check(before.permissions.add_reactions)} ➜ {check(after.permissions.add_reactions)}")
        if before.permissions.use_external_emojis != after.permissions.use_external_emojis:
            perms2.append(f"**Use External Emojis:** {check(before.permissions.use_external_emojis)} ➜ {check(after.permissions.use_external_emojis)}")
        if before.permissions.mention_everyone != after.permissions.mention_everyone:
            perms2.append(f"**Mention Everyone:** {check(before.permissions.mention_everyone)} ➜ {check(after.permissions.mention_everyone)}")
        if before.permissions.manage_messages != after.permissions.manage_messages:
            perms2.append(f"**Manage Messages:** {check(before.permissions.manage_messages)} ➜ {check(after.permissions.manage_messages)}")
        if before.permissions.read_message_history != after.permissions.read_message_history:
            perms2.append(f"**Read Message History:** {check(before.permissions.read_message_history)} ➜ {check(after.permissions.read_message_history)}")
        if before.permissions.send_tts_messages != after.permissions.send_tts_messages:
            perms2.append(f"**Send Text-to-Speech Messages:** {check(before.permissions.send_tts_messages)} ➜ {check(after.permissions.send_tts_messages)}")
        if before.permissions.use_slash_commands != after.permissions.use_slash_commands:
            perms2.append(f"**Use Slash Commands:** {check(before.permissions.use_slash_commands)} ➜ {check(after.permissions.use_slash_commands)}")
        if before.permissions.connect != after.permissions.connect:
            perms3.append(f"**Connect:** {check(before.permissions.connect)} ➜ {check(after.permissions.connect)}")
        if before.permissions.speak != after.permissions.speak:
            perms3.append(f"**Speak:** {check(before.permissions.speak)} ➜ {check(after.permissions.speak)}")
        if before.permissions.stream != after.permissions.stream:
            perms3.append(f"**Video:** {check(before.permissions.stream)} ➜ {check(after.permissions.stream)}")
        if before.permissions.use_voice_activation != after.permissions.use_voice_activation:
            perms3.append(f"**Priority Speaker:** {check(before.permissions.use_voice_activation)} ➜ {check(after.permissions.use_voice_activation)}")
        if before.permissions.mute_members != after.permissions.mute_members:
            perms3.append(f"**Mute Members:** {check(before.permissions.mute_members)} ➜ {check(after.permissions.mute_members)}")
        if before.permissions.deafen_members != after.permissions.deafen_members:
            perms3.append(f"**Deafen Members:** {check(before.permissions.deafen_members)} ➜ {check(after.permissions.deafen_members)}")
        if before.permissions.move_members != after.permissions.move_members:
            perms3.append(f"**Move Members:** {check(before.permissions.move_members)} ➜ {check(after.permissions.move_members)}")
        temp = '\n'.join(perms)
        temp1 = '\n'.join(perms1)
        temp2 = '\n'.join(perms2)
        temp3 = '\n'.join(perms3)
        
            
        
        if len(prev) != 0:
            embed.add_field(name=f"Before:", value=f"{temp11}", inline=True)
            embed.add_field(name=f"After:", value=f"{temp22}", inline=True)
            if len(perms) != 0 or len(perms1) != 0 or len(perms2) != 0 or len(perms3) != 0:
                embed.add_field(name=f"___________________________", value=f"\u200b", inline=False)
        if len(perms) != 0:
            embed.add_field(name=f"Updated General Permissions:", value=f"{temp}", inline=True)
            if ( len(perms2) != 0 or len(perms3) != 0 ) and len (perms1) == 0:
                embed.add_field(name=f"___________________________", value=f"\u200b", inline=False)
        if len(perms1) != 0:
            embed.add_field(name=f"Updated Membership Permissions:", value=f"{temp1}", inline=True)
            if ( len(perms2) != 0 or len(perms3) != 0 ):
                embed.add_field(name=f"___________________________", value=f"\u200b", inline=False)
        if len(perms2) != 0:
            embed.add_field(name=f"Updated Text Channel Permissions:", value=f"{temp2}", inline=True)
        if len(perms3) != 0:
            embed.add_field(name=f"Updated Voice Channel Permissions:", value=f"{temp3}", inline=True)
            
        embed.set_footer(text = f"Role ID: {after.id}")
        if channel != None:
            await channel.send(embed=embed)
            
        
        
            
            
            
    
    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        with open ("./cogs/json/setup.json", "r") as f:
                setup = json.load(f)
        channelid = None
        try:
            channelid = setup[str(role.guild.id)]["server_update_channel"]
            channelid = int(channelid)
        except Exception:
            pass
        channel = self.client.get_channel(channelid)
        
        before = role.created_at
        current = datetime.utcnow()
        duration = current - before
        duration_in_s = duration.total_seconds()  
        diff = relativedelta.relativedelta(current, before)
        
        try:
            created_months = diff.months
        except Exception:
            created_months = 0
        try:
            created_days = diff.days
        except Exception:
            created_days = 0
        try:
            created_years = diff.years
        except Exception:
            created_years = 0
        try:
            hours = divmod(duration_in_s, 3600)
            created_hours = int(round(hours[0]))
            while created_hours > 23:
                created_hours -= 24
        except Exception:
            created_hours = 0
        try:
            minutes = divmod(duration_in_s, 60)
            created_minutes = int(round(minutes[0]))
            while created_minutes > 60:
                created_minutes -= 60
        except Exception:
            created_minutes = 0
        try:
            seconds = divmod(duration_in_s, 60)
            created_seconds = int(round(seconds[1]))
        except Exception:
            created_seconds = 0
            
        totaltime = []
        if created_years != 0:
            totaltime.append(f"{created_years} year(s)")
        if created_months != 0:
            totaltime.append(f"{created_months} month(s)")
        if created_days != 0:
            totaltime.append(f"{created_days} day(s)")
        if created_hours != 0:
            totaltime.append(f"{created_hours} hour(s)")
        if created_minutes != 0:
            totaltime.append(f"{created_minutes} minute(s)") 
        if created_minutes != 0:
            totaltime.append(f"{created_seconds} second(s)")
        totaltime = ", ".join(totaltime)
        
        embed = discord.Embed(title = f"\"{role.name}\" role deleted", description = f"**Name**: {role.name}\n**Color:** #{role.color}\n**Mentionable:** {role.mentionable}\n**Displayed Seperately:** {role.hoist}\n**Position:** {role.position}\nCreated {totaltime} ago ",color = 0xDD5F53 ,timestamp = datetime.utcnow())
        embed.set_footer(text = f"Role ID: {role.id}")
        if channelid != None:
            await channel.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        with open ("./cogs/json/setup.json", "r") as f:
                setup = json.load(f)
        channelid = None
        try:
            channelid = setup[str(role.guild.id)]["server_update_channel"]
            channelid = int(channelid)
        except Exception:
            pass
        channel = self.client.get_channel(channelid)
        embed = discord.Embed(title = f"\"{role.name}\" role created", description = f"**Name**: {role.name}\n**Color:** #{role.color}\n**Mentionable:** {role.mentionable}\n**Displayed Seperately:** {role.hoist}",color = 0x53DDAC ,timestamp = datetime.utcnow())
        embed.set_footer(text = f"Role ID: {role.id}")
        
        if channel != None:
            await channel.send(embed=embed)
        
        
    
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        with open ("./cogs/json/setup.json", "r") as f:
                setup = json.load(f)
        channelid = None
        for guild in self.client.guilds:
            if guild.get_member(before.id) is not None:
                try:
                    channelid = setup[str(guild.id)]["user_update_channel"]
                    channelid = int(channelid)
                except Exception:
                    pass

                channel = self.client.get_channel(channelid)
                if before.roles != after.roles:
                    
                    removed = []
                    added = []
                    if len(before.roles) > len(after.roles):
                        allroles = before.roles

                    else:
                        allroles = after.roles
                    for role in allroles:
                        if role in before.roles:
                            if not role in after.roles:
                                removed.append(role.mention)
                        elif role in after.roles:
                            if not role in before.roles:
                                added.append(role.mention)
                    if len(removed) != 0 and len(added) != 0:
                        
                        embed = discord.Embed(title = f"Role(s) Updated", color = 0x4286F4,timestamp = datetime.utcnow())
                        merged = ", ".join(added)
                        embed.add_field(name="Added:", value=f"{merged}", inline=True)
                        merged = ", ".join(removed)
                        embed.add_field(name="Removed:", value=f"{merged}", inline=True)
                    else:
                        
                        if len(removed) != 0:
                            merged = ",".join(removed)
                            embed = discord.Embed(title = f"Role(s) Removed", description = f"{merged}",color = 0xDD5F53,timestamp = datetime.utcnow())
                        if len(added) != 0:
                            merged = ",".join(added)
                            embed = discord.Embed(title = f"Role(s) Added", description = f"{merged}",color = 0x53DDAC,timestamp = datetime.utcnow())
                    embed.set_footer(text = f"Member ID: {before.id}")
                    embed.set_author(name = str(before), icon_url = str(after.avatar_url))
                    if channelid != None:
                        await channel.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        embed = discord.Embed(title = f"{str(after.type).capitalize()} channel updated",description = f"**Updated channel:** {after.mention}", timestamp = datetime.utcnow(), color=0x4286F4)
        if str(before.type) == "voice" or str(before.type) == "stage_voice":
            prev = []
            notprev = []
            if before.name != after.name:
                prev.append(f"**Name:** {before.name}")
                notprev.append(f" **Name:**{after.name}")
                
            if before.rtc_region != after.rtc_region:
                if after.rtc_region == None:
                    if before.rtc_region == None:
                        prev.append("**Region:** Automatic")
                    else:
                        prev.append(f"**Region:** {before.rtc_region}")
                    notprev.append("**Region:** Automatic")
                else:
                    if before.rtc_region == None:
                        prev.append("**Region:** Automatic")
                    else:
                        prev.append(f"**Region:** {before.rtc_region}")
                    notprev.append(f"**Region:** {after.rtc_region}")
            if before.user_limit != after.user_limit:
                if after.user_limit == 0:
                    if before.user_limit == 0:
                        prev.append("**User Limit:** None")
                    else:
                        prev.append(f"**User Limit:** {before.user_limit}")
                    
                    notprev.append("**User Limit:** None")

                else:
                    if before.user_limit == 0:
                        prev.append("**User Limit:** None")
                    else:
                        prev.append(f"**User Limit:** {before.user_limit}")
                    notprev.append(f"**User Limit:** {after.user_limit}")
            if before.bitrate != after.bitrate:
                prev.append(f"Bitrate: {before.bitrate}")
                notprev.append(f"Bitrate: {after.bitrate}")
            if before.position != after.position:
                prev.append(f"Position: {before.position}")
                notprev.append(f"Position: {after.position}")
                
            temp1 = '\n'.join(prev)
            temp2 = '\n'.join(notprev)
            if len(prev) != 0:
                embed.add_field(name=f"Before:", value=f"{temp1}\u2800", inline=True)
                embed.add_field(name=f"After:", value=f"{temp2}\u2800", inline=True)
                
            def check(overwrite):
                if overwrite == False:
                    return ":x:"
                elif overwrite == True:
                    return ":white_check_mark:"
                else: 
                    return ":white_large_square:"
            
            if len(after.overwrites) > len(before.overwrites):
                testlist = after.overwrites
            else:
                testlist = before.overwrites
            for x in testlist:
                over = []
                if x in before.overwrites and x in after.overwrites:
                    
                    if before.overwrites[x].view_channel != after.overwrites[x].view_channel:
                        over.append(f"**View messages:** {check(before.overwrites[x].view_channel)} ➜ {check(after.overwrites[x].view_channel)}")
                    if before.overwrites[x].manage_channels != after.overwrites[x].manage_channels:
                        over.append(f"**Manage Channels:** {check(before.overwrites[x].manage_channels)} ➜ {check(after.overwrites[x].manage_channels)}")
                    if before.overwrites[x].manage_permissions != after.overwrites[x].manage_permissions:
                        over.append(f"**Manage Permissions:** {check(before.overwrites[x].manage_permissions)} ➜ {check(after.overwrites[x].manage_permissions)}")
                    if before.overwrites[x].create_instant_invite != after.overwrites[x].create_instant_invite:
                        over.append(f"**Create Instant Invites:** {check(before.overwrites[x].create_instant_invite)} ➜ {check(after.overwrites[x].create_instant_invite)}")
                    if before.overwrites[x].connect != after.overwrites[x].connect:
                        over.append(f"**Connect:** {check(before.overwrites[x].connect)} ➜ {check(after.overwrites[x].connect)}")    
                    if before.overwrites[x].speak != after.overwrites[x].speak:
                        over.append(f"**Speak:** {check(before.overwrites[x].speak)} ➜ {check(after.overwrites[x].speak)}")   
                    if before.overwrites[x].stream != after.overwrites[x].stream:
                        over.append(f"**Video / Stream:** {check(before.overwrites[x].stream)} ➜ {check(after.overwrites[x].stream)}")   
                    if before.overwrites[x].use_voice_activation != after.overwrites[x].use_voice_activation:
                        over.append(f"**Voice Activity:** {check(before.overwrites[x].use_voice_activation)} ➜ {check(after.overwrites[x].use_voice_activation)}")   
                    if before.overwrites[x].priority_speaker != after.overwrites[x].priority_speaker:
                        over.append(f"**Priority Speaker:** {check(before.overwrites[x].priority_speaker)} ➜ {check(after.overwrites[x].priority_speaker)}") 
                    if before.overwrites[x].mute_members != after.overwrites[x].mute_members:
                        over.append(f"**Mute Members:** {check(before.overwrites[x].mute_members)} ➜ {check(after.overwrites[x].mute_members)}") 
                    if before.overwrites[x].deafen_members != after.overwrites[x].deafen_members:
                        over.append(f"**Deafen Members:** {check(before.overwrites[x].deafen_members)} ➜ {check(after.overwrites[x].deafen_members)}") 
                    if before.overwrites[x].move_members != after.overwrites[x].move_members:
                        over.append(f"**Move Members:** {check(before.overwrites[x].move_members)} ➜ {check(after.overwrites[x].move_members)}") 
                elif x in before.overwrites:
                    over.append(f"**Removed {x.mention} from overwrites**") 
                elif x in after.overwrites:
                    over.append(f"**Added {x.mention} to overwrites**") 
                    
                    
                temp = '\n'.join(over)
                if len(over) != 0:
                	embed.add_field(name=f"Updated override(s) for {x}", value=f"{temp}\u2800", inline=False)
            embed.set_footer(text = f"Channel ID: {after.id}")
        elif str(before.type) == "text" or str(before.type) == "private" or str(before.type) == "group" or str(before.type) == "news":
            prev = []
            notprev = []
            if before.name != after.name:
                prev.append(f"**Name:** {before.name}")
                notprev.append(f"**Name:** {after.name}")
            if before.topic != after.topic:
                prev.append(f"**Topic:** {before.topic}")
                notprev.append(f" **Topic:** {after.topic}")
            if before.category != after.category:
                prev.append(f"**Category:** {before.category}")
                notprev.append(f"**Category:** {after.category}")
            if before.slowmode_delay != after.slowmode_delay:
                prev.append(f"**Slowmode Delay:** {before.slowmode_delay}")
                notprev.append(f"**Slowmode Delay:** {after.slowmode_delay}")
            if before.is_nsfw() != after.is_nsfw():
                prev.append(f"**NSFW:** {before.is_nsfw()}")
                notprev.append(f"**NSFW:** {after.is_nsfw()}")
            if before.position != after.position:
                prev.append(f"Position: {before.position}")
                notprev.append(f"Position: {after.position}")
            
            temp1 = '\n'.join(prev)
            temp2 = '\n'.join(notprev)
            if len(prev) != 0:
                embed.add_field(name=f"Before:", value=f"{temp1}\u2800", inline=True)
                embed.add_field(name=f"After:", value=f"{temp2}\u2800", inline=True)
            
            def check(overwrite):
                if overwrite == False:
                    return ":x:"
                elif overwrite == True:
                    return ":white_check_mark:"
                else: 
                    return ":white_large_square:"
            if len(after.overwrites) > len(before.overwrites):
                testlist = after.overwrites
            else:
                testlist = before.overwrites
            for x in testlist:
                over = []
                if x in before.overwrites and x in after.overwrites:
                    if before.overwrites[x].view_channel != after.overwrites[x].view_channel:
                        over.append(f"**View messages:** {check(before.overwrites[x].view_channel)} ➜ {check(after.overwrites[x].view_channel)}")
                    if before.overwrites[x].manage_channels != after.overwrites[x].manage_channels:
                        over.append(f"**Manage Channels:** {check(before.overwrites[x].manage_channels)} ➜ {check(after.overwrites[x].manage_channels)}")
                    if before.overwrites[x].manage_permissions != after.overwrites[x].manage_permissions:
                        over.append(f"**Manage Permissions:** {check(before.overwrites[x].manage_permissions)} ➜ {check(after.overwrites[x].manage_permissions)}")
                    if before.overwrites[x].manage_webhooks != after.overwrites[x].manage_webhooks:
                        over.append(f"**Manage Webhooks:** {check(before.overwrites[x].manage_webhooks)} ➜ {check(after.overwrites[x].manage_webhooks)}")
                    if before.overwrites[x].create_instant_invite != after.overwrites[x].create_instant_invite:
                        over.append(f"**Create Instant Invites:** {check(before.overwrites[x].create_instant_invite)} ➜ {check(after.overwrites[x].create_instant_invite)}")
                    if before.overwrites[x].send_messages != after.overwrites[x].send_messages:
                        over.append(f"**Send messages:** {check(before.overwrites[x].send_messages)} ➜ {check(after.overwrites[x].send_messages)}")
                    if before.overwrites[x].embed_links != after.overwrites[x].embed_links:
                        over.append(f"**Embed Links:** {check(before.overwrites[x].embed_links)} ➜ {check(after.overwrites[x].embed_links)}")
                    if before.overwrites[x].attach_files != after.overwrites[x].attach_files:
                        over.append(f"**Attach Files:** {check(before.overwrites[x].attach_files)} ➜ {check(after.overwrites[x].attach_files)}")
                    if before.overwrites[x].add_reactions != after.overwrites[x].add_reactions:
                        over.append(f"**Add Reactions:** {check(before.overwrites[x].add_reactions)} ➜ {check(after.overwrites[x].add_reactions)}")
                    if before.overwrites[x].external_emojis != after.overwrites[x].external_emojis:
                        over.append(f"**Use External Emojis:** {check(before.overwrites[x].external_emojis)} ➜ {check(after.overwrites[x].external_emojis)}")  
                    if before.overwrites[x].mention_everyone != after.overwrites[x].mention_everyone:
                        over.append(f"**Mention Everyone:** {check(before.overwrites[x].mention_everyone)} ➜ {check(after.overwrites[x].mention_everyone)}")     
                    if before.overwrites[x].manage_messages != after.overwrites[x].manage_messages:
                        over.append(f"**Manage Messages:** {check(before.overwrites[x].manage_messages)} ➜ {check(after.overwrites[x].manage_messages)}") 
                    if before.overwrites[x].read_message_history != after.overwrites[x].read_message_history:
                        over.append(f"**Read Message History:** {check(before.overwrites[x].read_message_history)} ➜ {check(after.overwrites[x].read_message_history)}") 
                    if before.overwrites[x].send_tts_messages != after.overwrites[x].send_tts_messages:
                        over.append(f"**Send Text-To-Speech Messagges:** {check(before.overwrites[x].send_tts_messages)} ➜ {check(after.overwrites[x].send_tts_messages)}")   
                    if before.overwrites[x].use_slash_commands != after.overwrites[x].use_slash_commands:
                        over.append(f"**Use Slash Commands:** {check(before.overwrites[x].use_slash_commands)} ➜ {check(after.overwrites[x].use_slash_commands)}") 
                elif x in before.overwrites:
                    over.append(f"**Removed {x.mention} from overwrites**") 
                elif x in after.overwrites:
                    over.append(f"**Added {x.mention} to overwrites**") 
                    
                
                
                temp = '\n'.join(over)
                print(temp)
                if len(over) != 0:
                	embed.add_field(name=f"Updated override(s) for {x}", value=f"{temp}\u2800", inline=False)
            embed.set_footer(text = f"Channel ID: {after.id}")
        elif str(before.type) == "category":
            prev = []
            notprev = []
            if before.name != after.name:
                prev.append(f"**Name:** {before.name}")
                notprev.append(f"**Name:** {after.name}")
            if before.position != after.position:
                prev.append(f"Position: {before.position}")
                notprev.append(f"Position: {after.position}")
            temp1 = '\n'.join(prev)
            temp2 = '\n'.join(notprev)
            if len(prev) != 0:
                embed.add_field(name=f"Before:", value=f"{temp1}\u2800", inline=True)
                embed.add_field(name=f"After:", value=f"{temp2}\u2800", inline=True)
            def check(overwrite):
                if overwrite == False:
                    return ":x:"
                elif overwrite == True:
                    return ":white_check_mark:"
                else: 
                    return ":white_large_square:"
            if len(after.overwrites) > len(before.overwrites):
                testlist = after.overwrites
            else:
                testlist = before.overwrites
            for x in testlist:
                over = []
                if x in before.overwrites and x in after.overwrites:
                        
                    if before.overwrites[x].view_channel != after.overwrites[x].view_channel:
                        over.append(f"**View messages:** {check(before.overwrites[x].view_channel)} ➜ {check(after.overwrites[x].view_channel)}")
                    if before.overwrites[x].manage_channels != after.overwrites[x].manage_channels:
                        over.append(f"**Manage Channels:** {check(before.overwrites[x].manage_channels)} ➜ {check(after.overwrites[x].manage_channels)}")
                    if before.overwrites[x].manage_permissions != after.overwrites[x].manage_permissions:
                        over.append(f"**Manage Permissions:** {check(before.overwrites[x].manage_permissions)} ➜ {check(after.overwrites[x].manage_permissions)}")
                    if before.overwrites[x].manage_webhooks != after.overwrites[x].manage_webhooks:
                        over.append(f"**Manage Webhooks:** {check(before.overwrites[x].manage_webhooks)} ➜ {check(after.overwrites[x].manage_webhooks)}")
                    if before.overwrites[x].create_instant_invite != after.overwrites[x].create_instant_invite:
                        over.append(f"**Create Instant Invites:** {check(before.overwrites[x].create_instant_invite)} ➜ {check(after.overwrites[x].create_instant_invite)}")
                    if before.overwrites[x].send_messages != after.overwrites[x].send_messages:
                        over.append(f"**Send messages:** {check(before.overwrites[x].send_messages)} ➜ {check(after.overwrites[x].send_messages)}")
                    if before.overwrites[x].embed_links != after.overwrites[x].embed_links:
                        over.append(f"**Embed Links:** {check(before.overwrites[x].embed_links)} ➜ {check(after.overwrites[x].embed_links)}")
                    if before.overwrites[x].attach_files != after.overwrites[x].attach_files:
                        over.append(f"**Attach Files:** {check(before.overwrites[x].attach_files)} ➜ {check(after.overwrites[x].attach_files)}")
                    if before.overwrites[x].add_reactions != after.overwrites[x].add_reactions:
                        over.append(f"**Add Reactions:** {check(before.overwrites[x].add_reactions)} ➜ {check(after.overwrites[x].add_reactions)}")
                    if before.overwrites[x].external_emojis != after.overwrites[x].external_emojis:
                        over.append(f"**Use External Emojis:** {check(before.overwrites[x].external_emojis)} ➜ {check(after.overwrites[x].external_emojis)}")  
                    if before.overwrites[x].mention_everyone != after.overwrites[x].mention_everyone:
                        over.append(f"**Mention Everyone:** {check(before.overwrites[x].mention_everyone)} ➜ {check(after.overwrites[x].mention_everyone)}")     
                    if before.overwrites[x].manage_messages != after.overwrites[x].manage_messages:
                        over.append(f"**Manage Messages:** {check(before.overwrites[x].manage_messages)} ➜ {check(after.overwrites[x].manage_messages)}") 
                    if before.overwrites[x].read_message_history != after.overwrites[x].read_message_history:
                        over.append(f"**Read Message History:** {check(before.overwrites[x].read_message_history)} ➜ {check(after.overwrites[x].read_message_history)}") 
                    if before.overwrites[x].send_tts_messages != after.overwrites[x].send_tts_messages:
                        over.append(f"**Send Text-To-Speech Messagges:** {check(before.overwrites[x].send_tts_messages)} ➜ {check(after.overwrites[x].send_tts_messages)}")   
                    if before.overwrites[x].use_slash_commands != after.overwrites[x].use_slash_commands:
                        over.append(f"**Use Slash Commands:** {check(before.overwrites[x].use_slash_commands)} ➜ {check(after.overwrites[x].use_slash_commands)}") 
                    if before.overwrites[x].connect != after.overwrites[x].connect:
                        over.append(f"**Connect:** {check(before.overwrites[x].connect)} ➜ {check(after.overwrites[x].connect)}")    
                    if before.overwrites[x].speak != after.overwrites[x].speak:
                        over.append(f"**Speak:** {check(before.overwrites[x].speak)} ➜ {check(after.overwrites[x].speak)}")   
                    if before.overwrites[x].stream != after.overwrites[x].stream:
                        over.append(f"**Video / Stream:** {check(before.overwrites[x].stream)} ➜ {check(after.overwrites[x].stream)}")   
                    if before.overwrites[x].use_voice_activation != after.overwrites[x].use_voice_activation:
                        over.append(f"**Voice Activity:** {check(before.overwrites[x].use_voice_activation)} ➜ {check(after.overwrites[x].use_voice_activation)}")   
                    if before.overwrites[x].priority_speaker != after.overwrites[x].priority_speaker:
                        over.append(f"**Priority Speaker:** {check(before.overwrites[x].priority_speaker)} ➜ {check(after.overwrites[x].priority_speaker)}") 
                    if before.overwrites[x].mute_members != after.overwrites[x].mute_members:
                        over.append(f"**Mute Members:** {check(before.overwrites[x].mute_members)} ➜ {check(after.overwrites[x].mute_members)}") 
                    if before.overwrites[x].deafen_members != after.overwrites[x].deafen_members:
                        over.append(f"**Deafen Members:** {check(before.overwrites[x].deafen_members)} ➜ {check(after.overwrites[x].deafen_members)}") 
                    if before.overwrites[x].move_members != after.overwrites[x].move_members:
                        over.append(f"**Move Members:** {check(before.overwrites[x].move_members)} ➜ {check(after.overwrites[x].move_members)}") 
                        
                elif x in before.overwrites:
                    over.append(f"**Removed {x.mention} from overwrites**") 
                elif x in after.overwrites:
                    over.append(f"**Added {x.mention} to overwrites**") 
                temp = '\n'.join(over)
                if len(over) != 0:
                	embed.add_field(name=f"Updated override(s) for {x}", value=f"{temp}\u2800", inline=False)
            embed.set_footer(text = f"Category ID: {after.id}")
            
            
        with open ("./cogs/json/setup.json", "r") as f:
            setup = json.load(f)
        channelid = None
        try:
            channelid = setup[str(after.guild.id)]["server_update_channel"]
            channelid = int(channelid)
        except Exception:
            pass
        channel = self.client.get_channel(channelid)
        if channelid != None:
            await channel.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        
        if channel.type == "category":
            embed = discord.Embed(title = f"{str(channel.type).capitalize()} channel deleted", description = f"**Name:** {channel.name}", timestamp = datetime.utcnow(), color=0xDD5F53)
            embed.set_footer(text = f"Category ID: {channel.id}")
        else:
            embed = discord.Embed(title = f"{str(channel.type).capitalize()} channel deleted", description = f"**Name:** {channel.name}\n**Category:** {channel.category}", timestamp = datetime.utcnow(), color=0xDD5F53)
            embed.set_footer(text = f"Channel ID: {channel.id}")
        
        with open ("./cogs/json/setup.json", "r") as f:
            setup = json.load(f)
        channelid = None
        try:
            channelid = setup[str(channel.guild.id)]["server_update_channel"]
            channelid = int(channelid)
        except Exception:
            pass
        channel = self.client.get_channel(channelid)
        if channelid != None:
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        if str(channel.type) == "voice" or str(channel.type) == "stage_voice":
            region = channel.rtc_region
            if region == None:
                region = "Automatic"
            userlimit = channel.user_limit
            if userlimit == 0:
                userlimit = "None"
            embed = discord.Embed(title = f"{str(channel.type).capitalize()} channel created", description = f"**Name:** {channel.name}\n**Category:** {channel.category}\n**User Limit:** {userlimit}\n**Bitrate:** {channel.bitrate}\n**Region:** {region}", timestamp = datetime.utcnow(), color=0x53DDAC)
            for x in channel.overwrites:
                over = []
                try:
                    if channel.overwrites[x].view_channel == False:
                        over.append("**View Channel:** :x:")
                    elif channel.overwrites[x].view_channel == True:
                        over.append("**View Channel:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].manage_channels == False:
                        over.append("**Manage Channels:** :x:")
                    elif channel.overwrites[x].manage_channels == True:
                        over.append("**Manage Channels:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].manage_permissions == False:
                        over.append("**Manage Permissions:** :x:")
                    elif channel.overwrites[x].manage_permissions == True:
                        over.append("**Manage Permissions:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].create_instant_invite == False:
                        over.append("**Create Instant Invites:** :x:")
                    elif channel.overwrites[x].create_instant_invite == True:
                        over.append("**Create Instant Invites:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].connect == False:
                        over.append("**Connect:** :x:")
                    elif channel.overwrites[x].connect == True:
                        over.append("**Connect:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].speak == False:
                        over.append("**Speak:** :x:")
                    elif channel.overwrites[x].speak == True:
                        over.append("**Speak:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].stream == False:
                        over.append("**Video / Stream:** :x:")
                    elif channel.overwrites[x].stream == True:
                        over.append("**Video / Stream:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].use_voice_activation == False:
                        over.append("**Voice Activity:** :x:")
                    elif channel.overwrites[x].use_voice_activation == True:
                        over.append("**Voice Activity:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].priority_speaker == False:
                        over.append("**Priority Speaker:** :x:")
                    elif channel.overwrites[x].priority_speaker == True:
                        over.append("**Priority Speaker:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].mute_members == False:
                        over.append("**Mute Members:** :x:")
                    elif channel.overwrites[x].mute_members == True:
                        over.append("**Mute Members:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].deafen_members == False:
                        over.append("**Deafen Members:** :x:")
                    elif channel.overwrites[x].deafen_members == True:
                        over.append("**Deafen Members:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].move_members == False:
                        over.append("**Move Members:** :x:")
                    elif channel.overwrites[x].move_members == True:
                        over.append("**Move Members:** :white_check_mark:")
                except Exception:
                    pass
                temp = '\n'.join(over)
                if len(over) != 0:
                    embed.add_field(name=f"Override(s) for {x}", value=f"{temp}", inline=False)
                embed.set_footer(text = f"Channel ID: {channel.id}")


        elif str(channel.type) == "text" or str(channel.type) == "private" or str(channel.type) == "group" or str(channel.type) == "news":



            embed = discord.Embed(title = f"{str(channel.type).capitalize()} channel created", description = f"**Name:** {channel.name}\n**Category:** {channel.category}\n**Topic:** {channel.topic}\n**Slowmode:** {channel.slowmode_delay}\n**NSFW:** {channel.is_nsfw()}", timestamp = datetime.utcnow(), color=0x39ea9d)

            for x in channel.overwrites:
                over = []
                try:
                    if channel.overwrites[x].view_channel == False:
                        over.append("**View Channel:** :x:")
                    elif channel.overwrites[x].view_channel == True:
                        over.append("**View Channel:** :white_check_mark:")
                except Exception:
                    pass
                
                try:
                    if channel.overwrites[x].manage_channels == False:
                        over.append("**Manage Channels:** :x:")
                    elif channel.overwrites[x].manage_channels == True:
                        over.append("**Manage Channels:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].manage_permissions == False:
                        over.append("**Manage Permissions:** :x:")
                    elif channel.overwrites[x].manage_permissions == True:
                        over.append("**Manage Permissions:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].manage_webhooks == False:
                        over.append("**Manage Webhooks:** :x:")
                    elif channel.overwrites[x].manage_webhooks == True:
                        over.append("**Manage Webhooks:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].create_instant_invite == False:
                        over.append("**Create Instant Invites:** :x:")
                    elif channel.overwrites[x].create_instant_invite == True:
                        over.append("**Create Instant Invites:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].embed_links == False:
                        over.append("**Embed Links:** :x:")
                    elif channel.overwrites[x].embed_links == True:
                        over.append("**Embed Links:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].attach_files == False:
                        over.append("**Attach Files:** :x:")
                    elif channel.overwrites[x].attach_files == True:
                        over.append("**Attach Files:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].add_reactions == False:
                        over.append("**Add Reactions:** :x:")
                    elif channel.overwrites[x].add_reactions == True:
                        over.append("**Add Reactions:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].external_emojis == False:
                        over.append("**Use External Emojis:** :x:")
                    elif channel.overwrites[x].external_emojis == True:
                        over.append("**Use External Emojis:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].mention_everyone == False:
                        over.append("**Mention Everyone:** :x:")
                    elif channel.overwrites[x].mention_everyone == True:
                        over.append("**Mention Everyone:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].manage_messages == False:
                        over.append("**Manage Messages:** :x:")
                    elif channel.overwrites[x].manage_messages == True:
                        over.append("**Manage Messages:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].read_message_history == False:
                        over.append("**Read Message History:** :x:")
                    elif channel.overwrites[x].read_message_history == True:
                        over.append("**Read Message History:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].send_tts_messages == False:
                        over.append("**Send Text-to-Speech Messages:** :x:")
                    elif channel.overwrites[x].send_tts_messages == True:
                        over.append("**Send Text-to-Speech Messages:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].use_slash_commands == False:
                        over.append("**Use Slash Commands** :x:")
                    elif channel.overwrites[x].use_slash_commands == True:
                        over.append("**Use Slash Commands** :white_check_mark:")
                except Exception:
                    pass
                temp = '\n'.join(over)
                if len(over) != 0:
                    embed.add_field(name=f"Role Override for {x}", value=f"{temp}", inline=False)
                embed.set_footer(text = f"Channel ID: {channel.id}")
            
        elif str(channel.type) == "category":
            embed = discord.Embed(title = f"{str(channel.type).capitalize()} channel created", description = f"**Name:** {channel.name}\n", timestamp = datetime.utcnow(), color=0x39ea9d)
            for x in channel.overwrites:
                over = []
                try:
                    if channel.overwrites[x].view_channel == False:
                        over.append("**View Channel:** :x:")
                    elif channel.overwrites[x].view_channel == True:
                        over.append("**View Channel:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].manage_channels == False:
                        over.append("**Manage Channels:** :x:")
                    elif channel.overwrites[x].manage_channels == True:
                        over.append("**Manage Channels:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].manage_permissions == False:
                        over.append("**Manage Permissions:** :x:")
                    elif channel.overwrites[x].manage_permissions == True:
                        over.append("**Manage Permissions:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].manage_webhooks == False:
                        over.append("**Manage Webhooks:** :x:")
                    elif channel.overwrites[x].manage_webhooks == True:
                        over.append("**Manage Webhooks:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].create_instant_invite == False:
                        over.append("**Create Instant Invites:** :x:")
                    elif channel.overwrites[x].create_instant_invite == True:
                        over.append("**Create Instant Invites:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].embed_links == False:
                        over.append("**Embed Links:** :x:")
                    elif channel.overwrites[x].embed_links == True:
                        over.append("**Embed Links:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].attach_files == False:
                        over.append("**Attach Files:** :x:")
                    elif channel.overwrites[x].attach_files == True:
                        over.append("**Attach Files:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].add_reactions == False:
                        over.append("**Add Reactions:** :x:")
                    elif channel.overwrites[x].add_reactions == True:
                        over.append("**Add Reactions:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].external_emojis == False:
                        over.append("**Use External Emojis:** :x:")
                    elif channel.overwrites[x].external_emojis == True:
                        over.append("**Use External Emojis:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].mention_everyone == False:
                        over.append("**Mention Everyone:** :x:")
                    elif channel.overwrites[x].mention_everyone == True:
                        over.append("**Mention Everyone:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].manage_messages == False:
                        over.append("**Manage Messages:** :x:")
                    elif channel.overwrites[x].manage_messages == True:
                        over.append("**Manage Messages:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].read_message_history == False:
                        over.append("**Read Message History:** :x:")
                    elif channel.overwrites[x].read_message_history == True:
                        over.append("**Read Message History:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].send_tts_messages == False:
                        over.append("**Send Text-to-Speech Messages:** :x:")
                    elif channel.overwrites[x].send_tts_messages == True:
                        over.append("**Send Text-to-Speech Messages:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].use_slash_commands == False:
                        over.append("**Use Slash Commands** :x:")
                    elif channel.overwrites[x].use_slash_commands == True:
                        over.append("**Use Slash Commands** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].connect == False:
                        over.append("**Connect:** :x:")
                    elif channel.overwrites[x].connect == True:
                        over.append("**Connect:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].speak == False:
                        over.append("**Speak:** :x:")
                    elif channel.overwrites[x].speak == True:
                        over.append("**Speak:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].stream == False:
                        over.append("**Video / Stream:** :x:")
                    elif channel.overwrites[x].stream == True:
                        over.append("**Video / Stream:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].use_voice_activation == False:
                        over.append("**Voice Activity:** :x:")
                    elif channel.overwrites[x].use_voice_activation == True:
                        over.append("**Voice Activity:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].priority_speaker == False:
                        over.append("**Priority Speaker:** :x:")
                    elif channel.overwrites[x].priority_speaker == True:
                        over.append("**Priority Speaker:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].mute_members == False:
                        over.append("**Mute Members:** :x:")
                    elif channel.overwrites[x].mute_members == True:
                        over.append("**Mute Members:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].deafen_members == False:
                        over.append("**Deafen Members:** :x:")
                    elif channel.overwrites[x].deafen_members == True:
                        over.append("**Deafen Members:** :white_check_mark:")
                except Exception:
                    pass
                try:
                    if channel.overwrites[x].move_members == False:
                        over.append("**Move Members:** :x:")
                    elif channel.overwrites[x].move_members == True:
                        over.append("**Move Members:** :white_check_mark:")
                except Exception:
                    pass
                temp = '\n'.join(over)
                if len(over) != 0:
                    embed.add_field(name=f"Role Override for {x}", value=f"{temp}", inline=False)
                embed.set_footer(text = f"Category ID: {channel.id}")
        
        
       
        
        with open ("./cogs/json/setup.json", "r") as f:
            setup = json.load(f)
        channelid = None
        try:
            channelid = setup[str(channel.guild.id)]["server_update_channel"]
            channelid = int(channelid)
        except Exception:
            pass
        channel = self.client.get_channel(channelid)
        if channelid != None:
            await channel.send(embed=embed)



    @commands.Cog.listener()
    async def on_user_update(self, before, after):
        with open ("./cogs/json/setup.json", "r") as f:
                setup = json.load(f)
        channelid = None
        for guild in self.client.guilds:
            if guild.get_member(before.id) is not None:
                try:
                    channelid = setup[str(guild.id)]["user_update_channel"]
                    channelid = int(channelid)
                except Exception:
                    pass

                channel = self.client.get_channel(channelid)

                if before.display_name != after.display_name:
                    embed = discord.Embed(title = f"Name Change", description = f"**Before:** {before.name}\n**After:** {after.name}\nUser: {after.mention}", color = 0x4286F4,timestamp = datetime.utcnow())
                    embed.set_author(name = str(after), icon_url = str(before.avatar_url))
                    embed.set_footer(text = f"ID: {before.id}")
                    await channel.send(embed=embed)
                if before.discriminator != after.discriminator:
                    embed = discord.Embed(title = f"Discriminator Change", description = f"**Before:** {before.discriminator}\n**After:** {after.discriminator}.\nUser: {after.mention}", color = after.color,timestamp = datetime.utcnow())
                    embed.set_author(name = str(before), icon_url = str(before.avatar_url))
                    embed.set_footer(text = f"ID: {before.id}")
                    await channel.send(embed=embed)
                if before.avatar_url != after.avatar_url:
                    embed = discord.Embed(title = f"Avatar Change", description = f"New image is below, old to the right.\n{after.mention}", color = after.color,timestamp = datetime.utcnow())
                    embed.set_thumbnail(url=before.avatar_url)
                    embed.set_image(url=after.avatar_url)
                    embed.set_footer(text = f"Member ID: {before.id}")
                    embed.set_author(name = str(before), icon_url = str(after.avatar_url))
                    if channel != None:
                        await channel.send(embed=embed)

        
        
        
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        create._guild(before.guild.id)
        with open ("./cogs/json/setup.json", "r") as f:
                setup = json.load(f)
        channelid = None
        try:
            channelid = setup[str(before.guild.id)]["message_update_channel"]
            channelid = int(channelid)
        except Exception:
            pass    
        channel = self.client.get_channel(channelid)
        
        if not after.author.bot:
            
            if len(before.content) > 1020:
                blength = 1020
            else:
                blength = len(before.content)
                
            if len(after.content) > 1020:
                alength = 1020
            else:
                alength = len(after.content)
            
            embed = discord.Embed(title = f"Message edited in #{before.channel}", description = f"Click [here]({before.jump_url}) to jump to the message", color = 0x4286F4,timestamp = datetime.utcnow())

            embed.add_field(name="**Before:**", value = f"{before.content[0:blength]}",inline=False)
            embed.add_field(name="**After:**", value = f"{after.content[0:alength]}",inline=False)
            embed.set_author(name = str(after.author), icon_url = str(before.author.avatar_url))
            embed.set_footer(text = f"Message ID: {before.id}")
            if channel != None:
                await channel.send(embed=embed)
                
                
    
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        create._guild(message.guild.id)
        with open ("./cogs/json/setup.json", "r") as f:
                setup = json.load(f)
        channelid = None
        try:
            channelid = setup[str(message.guild.id)]["message_update_channel"]
            channelid = int(channelid)
        except Exception:
            pass    
        channel = self.client.get_channel(channelid)
        
        if not message.author.bot:
            embed = discord.Embed(title = f"Message deleted in #{message.channel}:", description = f"{message.content[0:2046]}", color = 0xDD5F53, timestamp = datetime.utcnow())
            embed.set_author(name = str(message.author), icon_url = str(message.author.avatar_url))
            embed.set_footer(text = f"Message ID: {message.id}")
            print(channelid)
            if channelid != None:
                await channel.send(embed=embed)
        
        
    @commands.Cog.listener()
    async def on_member_join(self, member): 
        create._guild(member.guild.id)
        with open ("./cogs/json/setup.json", "r") as f:
            setup = json.load(f)
        channelid = None
        try:
            channelid = setup[str(member.guild.id)]["join_leave_channel"]
            channelid = int(channelid)
        except Exception:
            pass    
        channel = self.client.get_channel(channelid)
        #strftime("%A, %B %d %Y @ %H:%M:%S %p")
        before = member.created_at
        current = datetime.utcnow()
        duration = current - before
        duration_in_s = duration.total_seconds()  
        diff = relativedelta.relativedelta(current, before)
        
        try:
            created_months = diff.months
        except Exception:
            created_months = 0
        try:
            created_days = diff.days
        except Exception:
            created_days = 0
        try:
            created_years = diff.years
        except Exception:
            created_years = 0
        try:
            hours = divmod(duration_in_s, 3600)
            created_hours = int(round(hours[0]))
            while created_hours > 23:
                created_hours -= 24
        except Exception:
            created_hours = 0
        try:
            minutes = divmod(duration_in_s, 60)
            created_minutes = int(round(minutes[0]))
            while created_minutes > 60:
                created_minutes -= 60
        except Exception:
            created_minutes = 0
        try:
            seconds = divmod(duration_in_s, 60)
            created_seconds = int(round(seconds[1]))
        except Exception:
            created_seconds = 0
        totaltime = ""
        
        if created_months == 0 and created_days == 0 and created_years == 0:
            totaltime = f"This account was created {created_hours} hour(s), {created_minutes} minute(s), and {created_seconds} second(s) ago"
        else:
            totaltime = f"This account was created {created_months} month(s), {created_days} day(s), and {created_years} year(s) ago"
        
            
            
            
        with open ("./cogs/json/counting.json", "r") as f:
            counting = json.load(f)
        if not str(member.guild.id) in counting:
            counting[str(member.guild.id)] = {}
            counting[str(member.guild.id)]["total_users"] = len(member.guild.members)
        user_count = counting[str(member.guild.id)]["total_users"]
        user_count = int(user_count) + 1
        counting[str(member.guild.id)]["total_users"] = str(user_count)
        
        if user_count == 2:
            user_count = f"{user_count}nd"
        elif user_count == 3:
            user_count = f"{user_count}rd"
        else:
            user_count = f"{user_count}th"
        
        embed = discord.Embed(title="Member Joined", description=f"{member.mention} was the {user_count} to join.\n{totaltime}", timestamp = datetime.utcnow(), color = 0x53DDAC)
        embed.set_author(name = str(member), icon_url = str(member.avatar_url))
        embed.set_footer(text = f"Member ID: {member.id}")
        if channel != None:
            await channel.send(embed=embed)
        
        with open ("./cogs/json/counting.json", "w") as f:
            json.dump(counting, f, indent=4)
            
    @commands.Cog.listener()
    async def on_member_remove(self, member): 
        create._guild(member.guild.id)
        with open ("./cogs/json/setup.json", "r") as f:
            setup = json.load(f)
        channelid = None
        try:
            channelid = setup[str(member.guild.id)]["join_leave_channel"]
            channelid = int(channelid)
        except Exception:
            pass    
        channel = self.client.get_channel(channelid)
        
        before = member.joined_at 
        current = datetime.utcnow()
        duration = current - before
        duration_in_s = duration.total_seconds()  
        diff = relativedelta.relativedelta(current, before)
        
        try:
            created_months = diff.months
        except Exception:
            created_months = 0
        try:
            created_days = diff.days
        except Exception:
            created_days = 0
        try:
            created_years = diff.years
        except Exception:
            created_years = 0
        try:
            hours = divmod(duration_in_s, 3600)
            created_hours = int(round(hours[0]))
            while created_hours > 23:
                created_hours -= 24
        except Exception:
            created_hours = 0
        try:
            minutes = divmod(duration_in_s, 60)
            created_minutes = int(round(minutes[0]))
            while created_minutes > 60:
                created_minutes -= 60
        except Exception:
            created_minutes = 0
        try:
            seconds = divmod(duration_in_s, 60)
            created_seconds = int(round(seconds[1]))
        except Exception:
            created_seconds = 0
        totaltime = []
        if created_years != 0:
            totaltime.append(f"{created_years} year(s)")
        if created_months != 0:
            totaltime.append(f"{created_months} month(s)")
        if created_days != 0:
            totaltime.append(f"{created_days} day(s)")
        if created_hours != 0:
            totaltime.append(f"{created_hours} hour(s)")
        if created_minutes != 0:
            totaltime.append(f"{created_minutes} minute(s)") 
        if created_minutes != 0:
            totaltime.append(f"{created_seconds} second(s)")
        totaltime = ", ".join(totaltime)
        
        if len(member.roles) != 0:
            temp = []
            roles = member.roles
            roles.pop(0)
            for x in roles:
                temp.append(x.mention)
            mergedroles = ", ".join(temp) 
            embed = discord.Embed(title="Member Left", description=f"{member.mention} joined {totaltime} ago\n**Roles:** {mergedroles}", timestamp = datetime.utcnow(), color = 0xDD5F53)
        else:
            
            embed = discord.Embed(title="Member Left", description=f"{member.mention} joined {totaltime} ago", timestamp = datetime.utcnow(), color = 0xDD5F53)
        embed.set_author(name = str(member), icon_url = str(member.avatar_url))
        embed.set_footer(text = f"Member ID: {member.id}")
        

        if channel != None:
            await channel.send(embed=embed)
        
        
        
def setup(client):
    client.add_cog(logs(client))    