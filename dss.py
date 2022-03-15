# Discord Server Scanner - Server's Data Gathering , Check Permissions On Channels/Roles And Detect Bugs
# Author: DociTeam - https://github.com/DociTeam
# March 15rd, 2022
# Copyright 2022, Doctor

import discord
from discord.ext import commands , tasks
from discord.utils import get
import os
import time
import datetime
import discum

def clear_console():
    if os.name in ('nt', 'dos'): #Check OS name for using correct command
        try:
            os.system("cls")
        except:
            pass
    else:
        try:
            os.system("clear")
        except:
            pass

def change_title():
    if os.name in ('nt', 'dos'):
        try:
            os.system('title "DociTeam | Discord Server Scanner"')
        except:
            pass
    else:
            pass


clear_console()
change_title()

class color : 
    Red = '\033[91m'
    Green = '\033[92m'
    Blue = '\033[94m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Yellow = '\033[93m'
    Magenta = '\033[95m'
    Grey = '\033[90m'
    Black = '\033[90m'
    Default = '\033[99m'



dociteam = color.Cyan+"""
                                     ____             _ _____                    
                                    |  _ \  ___   ___(_)_   _|__  __ _ _ __ ___  
                                    | | | |/ _ \ / __| | | |/ _ \/ _` | '_ ` _ \ 
                                    | |_| | (_) | (__| | | |  __/ (_| | | | | | |
                                    |____/ \___/ \___|_| |_|\___|\__,_|_| |_| |_|
"""

banner =color.Magenta+ f"""
            ______              
         .-'      `-.           
       .'            `.         
      /                \        
     ;                 ;`       
     |     {color.Blue}Discord{color.Magenta}     | ;       
     ;                 ; |
     '\               / ;       
      \`.           .' /        
       `.`-._____.-' .'         
         / /`_____.-'           
        / / /                   
       / / /
      / / /
     / / /
    / / /
   / / /
  / / /
 / / /
/ / /
\/_/
"""


def slowprint(text: str, speed: float, newLine=True):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(speed)
    if newLine:
        print()

print(dociteam)
time.sleep(2)
clear_console()
print(banner)
time.sleep(1)
slowprint(color.Yellow+"\n\n|---------- Welcome to Discord Server Scanner ----------|\n",0.07)
slowprint(color.Yellow+"[!] This Project is Education Purpose Only!\n",0.07)
while True:
    TOKEN = str(input(color.Cyan+f"[+] Enter Your Discord Account Token : {color.White}")).strip()
    if len(TOKEN.strip()) == 0:
        print(color.Red+"\n[-] You Should Enter Your Discord Account Token!\n")
    else:
        break
while True:
    CMD_PREFIX = str(input(color.Cyan+f"[+] Enter Command Prefix (Example : !) : {color.White}")).strip()
    if len(CMD_PREFIX.strip()) == 0:
        print(color.Red+"\n[-] You Should Enter Command Prefix!\n")
    if len(CMD_PREFIX) > 6:
        print(color.Red+"\n[-] Invalid Command Prefix! (Max Length = 6)\n")
    else:
        break

bot = discum.Client(token=TOKEN)

clear_console()
print(banner)
slowprint(color.Yellow+f"\n\n[!] For more information use {color.Red}{CMD_PREFIX}help\n",0.07)
time.sleep(1)

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix= CMD_PREFIX , self_bot=True , intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print(color.Cyan+"|Username : "+color.Green+str(client.user))
    print(color.Cyan+"|Created On  : "+color.Green+str(client.user.created_at))
    print(color.Cyan+"|Servers Joined : "+color.Green+str(len(client.guilds)))
    print(color.Green+"\n[+] Discord Server Scanner Is Ready....\n")


@client.command() #Show information of server
async def info(ctx):
    await ctx.message.delete()
    def close_after_fetching(resp, guild_id):
        if bot.gateway.finishedMemberFetching(guild_id):
            bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
            bot.gateway.close()
    def get_owner(guild_id, channel_id):
        bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=1) #Get all user attributes, wait 1 second between requests
        bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.run()
        bot.gateway.resetSession() #Saves 10 seconds when gateway is run again
        return bot.gateway.session.guild(guild_id).owner
    name = str(ctx.guild.name)
    guild_owner = str(get_owner(str(ctx.guild.id) , str(ctx.channel.id)))
    boost = str(ctx.guild.premium_subscription_count)
    if int(boost) < 2:
        guild_level = "No Level"
    if 2 <= int(boost) < 7:
        guild_level = "Level 1"
    if 7 <= int(boost) < 14:
        guild_level = "Level 2"
    if int(boost) >= 14:
        guild_level = "Level 3"
    memberCount = str(ctx.guild.member_count)
    text_channels = len(ctx.guild.text_channels)
    voice_channels = len(ctx.guild.voice_channels)
    categories = len(ctx.guild.categories)
    guild_creation_date = ctx.guild.created_at
    vc = 0;
    for member in ctx.guild.members:
        voice_state = member.voice
        if voice_state is None:
            continue
        else:
            vc += 1
    rl = 0;
    for role in ctx.guild.roles:
        rl += 1
    clear_console()
    print(banner+"\n")
    print(color.Yellow+"\n"+name + " Server Information :\n")
    print(color.Cyan+"|Owner ID : "+color.Green+guild_owner)
    print(color.Cyan+"|Boost Count : "+color.Green+boost)
    print(color.Cyan+"|Level : "+color.Green+guild_level)
    print(color.Cyan+"|Member Count : "+color.Green+memberCount)
    print(color.Cyan+"|Text Channels : "+color.Green+str(text_channels))
    print(color.Cyan+"|Voice Channels : "+color.Green+str(voice_channels))
    print(color.Cyan+"|Categories : "+color.Green+str(categories))
    print(color.Cyan+"|Alive Voice : "+color.Green+str(vc))
    print(color.Cyan+"|Verification Level : "+color.Green+str(ctx.guild.verification_level))
    print(color.Cyan+'|Creation Date : '+color.Green+str(guild_creation_date))
    print(color.Cyan+"|Total Roles : "+color.Green+str(rl-1)) #rl-1 because of @everyone role
    print(color.Grey+"\n|---------End---------|\n")

@client.command()
async def roles(ctx): #Show server's roles
    await ctx.message.delete()
    a = 0;
    for role in ctx.guild.roles[::-1][:-1]:
        a += 1
        print(color.Green+str(a)+ "-"+ str(role))
    print(color.Grey+"\n|---------End---------|\n")

@client.command()
async def tchannels(ctx): #Check roles high permissions on text channels
    await ctx.message.delete()
    a = 0;
    b = 0;
    for tchannel in ctx.guild.text_channels:
        for role in ctx.guild.roles:
            overwrite = tchannel.overwrites_for(role)
            if overwrite.manage_channels == True:
                print(color.Yellow+"|Channel : "+str(tchannel)+"\n"+"|Role : "+str(role)+"\n"+"|Manage Channels Permission Detected!")
                print(color.Grey+"---------------------------------------------------------------------------------")
            if tchannel.overwrites_for(ctx.guild.default_role).manage_permissions != False and a == 0:
                print(color.Yellow+"|Channel : "+str(tchannel)+"\n"+"|Role : "+str(ctx.guild.default_role)+"\n"+"|Manage Permissions Permission Detected!")
                print(color.Grey+"---------------------------------------------------------------------------------")
                a += 1
            if overwrite.manage_permissions == True:
                print(color.Yellow+"|Channel : "+str(tchannel)+"\n"+"|Role : "+str(role)+"\n"+"|Manage Permissions Permission Detected!")
                print(color.Grey+"---------------------------------------------------------------------------------")
            if tchannel.overwrites_for(ctx.guild.default_role).manage_webhooks != False and b == 0:
                print(color.Yellow+"|Channel : "+str(tchannel)+"\n"+"|Role : "+str(ctx.guild.default_role)+"\n"+"|Manage Webhooks Permission Detected!")
                print(color.Red+"Note : If You Do Not Have Manage Webhooks In Notified Channel You Should Have Manage Webhook Permission On Your Roles To Use That!")
                print(color.Grey+"---------------------------------------------------------------------------------")
                b += 1
            if overwrite.manage_webhooks == True:
                print(color.Yellow+"|Channel : "+str(tchannel)+"\n"+"|Role : "+str(role)+"\n"+"|Manage Webhooks Permission Detected!")
                print(color.Grey+"---------------------------------------------------------------------------------")
            if overwrite.add_reactions == True:
                print(color.Yellow+"|Channel : "+str(tchannel)+"\n"+"|Role : "+str(role)+"\n"+"|Add Reactions Permission Detected!")
                print(color.Grey+"---------------------------------------------------------------------------------")
            if overwrite.mention_everyone == True:
                print(color.Yellow+"|Channel : "+str(tchannel)+"\n"+"|Role : "+str(role)+"\n"+"|Mention Everyone Permission Detected!")
                print(color.Grey+"---------------------------------------------------------------------------------")
            if overwrite.manage_messages == True:
                print(color.Yellow+"|Channel : "+str(tchannel)+"\n"+"|Role : "+str(role)+"\n"+"|Manage Messages Permission Detected!")
                print(color.Grey+"---------------------------------------------------------------------------------")
    print(color.Green+"\n.: |Done! :.\n")

@client.command()
async def vchannels(ctx): #Check roles high permissions on voice channels
    await ctx.message.delete()
    a = 0;
    for vchannel in ctx.guild.voice_channels:
        for role in ctx.guild.roles:
            overwrite = vchannel.overwrites_for(role)
            if overwrite.manage_channels == True:
                print(color.Yellow+"|Channel : "+str(vchannel)+"\n"+"|Role : **"+str(role)+"\n"+"|Manage Channels Permission Detected!")
                print(color.Grey+"---------------------------------------------------------------------------------")
            if vchannel.overwrites_for(ctx.guild.default_role).manage_permissions != False and a == 0:
                print(color.Yellow+"|Channel : "+str(vchannel)+"\n"+"|Role : "+str(ctx.guild.default_role)+"\n"+"|Manage Permissions Permission Detected!")
                print(color.Red+"Note : If You Do Not Have Manage Permissions In Notified Channel You Should Have Manage Roles To Use That!")
                print(color.Grey+"---------------------------------------------------------------------------------")
                a += 1
            if overwrite.manage_permissions == True:
                print(color.Yellow+"|Channel : "+str(vchannel)+"\n"+"|Role : "+str(role)+"\n"+"|Manage Permissions Permission Detected!")
                print(color.Grey+"---------------------------------------------------------------------------------")
            if overwrite.mute_members == True:
                print(color.Yellow+"|Channel : "+str(vchannel)+"\n"+"|Role : "+str(role)+"\n"+"|Mute Permission Detected!")
                print(color.Grey+"---------------------------------------------------------------------------------")
    print(color.Green+"\n.: |Done! :.\n")

@client.command()
async def access(ctx): #Show roles permissions
    await ctx.message.delete()
    a = 0;
    print(color.Yellow+"|Administratori Roles:\n")
    for role1 in ctx.guild.roles[::-1]:
        if role1.permissions.administrator is True:
            a += 1
            print(color.Green+str(a)+"-"+str(role1))
        print(color.Grey+"---------------------------------------------------------------------------------")
        a = 0;
        print(color.Yellow+"|Manage Channels Roles:\n")
        for role2 in ctx.guild.roles[::-1]:
            if role2.permissions.manage_channels is True:
                a += 1
                print(color.Green+str(a)+"-"+str(role2))
        print(color.Grey+"---------------------------------------------------------------------------------")
        a = 0;
        print(color.Yellow+"|Manage Roles Roles:\n")
        for role3 in ctx.guild.roles[::-1]:
            if role3.permissions.manage_roles is True:
                a += 1
                print(color.Green+str(a)+"-"+str(role3))
        print(color.Grey+"---------------------------------------------------------------------------------")
        a = 0;
        print(color.Yellow+"|Manage Emojis Roles:\n")
        for role4 in ctx.guild.roles[::-1]:
            if role4.permissions.manage_emojis is True:
                a += 1
                print(color.Green+str(a)+"-"+str(role4))
        print(color.Grey+"---------------------------------------------------------------------------------")
        a = 0;
        print(color.Yellow+"|View Audit Log Roles:\n")
        for role5 in ctx.guild.roles[::-1]:
            if role5.permissions.view_audit_log is True:
                a += 1
                print(color.Green+str(a)+"-"+str(role5))
        print(color.Grey+"---------------------------------------------------------------------------------")
        a = 0;
        print(color.Yellow+"|Manage Webhooks Roles:\n")
        for role6 in ctx.guild.roles[::-1]:
            if role6.permissions.manage_webhooks is True:
                a += 1
                print(color.Green+str(a)+"-"+str(role6))
        print(color.Grey+"---------------------------------------------------------------------------------")
        a = 0;
        print(color.Yellow+"|Manage Nicknames Roles:\n")
        for role7 in ctx.guild.roles[::-1]:
            if role7.permissions.manage_nicknames is True:
                a += 1
                print(color.Green+str(a)+"-"+str(role7))
        print(color.Grey+"---------------------------------------------------------------------------------")
        a = 0;
        print(color.Yellow+"|Have Kick Permission Roles:\n")
        for role8 in ctx.guild.roles[::-1]:
            if role8.permissions.kick_members is True:
                a += 1
                print(color.Green+str(a)+"-"+str(role8))
        print(color.Grey+"---------------------------------------------------------------------------------")
        a = 0;
        print(color.Yellow+"|Have Ban Permission Roles:\n")
        for role9 in ctx.guild.roles[::-1]:
            if role9.permissions.ban_members is True:
                a += 1
                print(color.Green+str(a)+"-"+str(role9))
        print(color.Grey+"---------------------------------------------------------------------------------")
        a = 0;
        print(color.Yellow+"|Add Reactions Roles:\n")
        for role10 in ctx.guild.roles[::-1]:
            if role10.permissions.add_reactions is True:
                a += 1
                print(color.Green+str(a)+"-"+str(role10))
        print(color.Grey+"---------------------------------------------------------------------------------")
        a = 0;
        print(color.Yellow+"|Mention Everyone Roles:\n")
        for role11 in ctx.guild.roles[::-1]:
            if role11.permissions.mention_everyone is True:
                a += 1
                print(color.Green+str(a)+"-"+str(role11))
        print(color.Grey+"---------------------------------------------------------------------------------")
        a = 0;
        print(color.Yellow+"|Manage Messages Roles:\n")
        for role12 in ctx.guild.roles[::-1]:
            if role12.permissions.manage_messages is True:
                a += 1
                print(color.Green+str(a)+"-"+str(role12))
        print(color.Grey+"---------------------------------------------------------------------------------")


@client.command()
async def mid(ctx): #Returns all members ID (If server's members are more than 1K , It returens just online members!)
    await ctx.message.delete()
    with open(f'{str(ctx.guild.name)}_memebrs_ID.txt','a', encoding='UTF-8') as members_ID:
        def close_after_fetching(resp, guild_id):
            if bot.gateway.finishedMemberFetching(guild_id):
                bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.close()
        def get_members_ID(guild_id, channel_id):
            bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=1) #Get all user attributes, wait 1 second between requests
            bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
            bot.gateway.run()
            bot.gateway.resetSession() #Saves 10 seconds when gateway is run again
            return bot.gateway.session.guild(guild_id).memberIDs
        for i in get_members_ID(str(ctx.guild.id) , str(ctx.channel.id)):
            members_ID.writelines(i+"\n")
    clear_console()
    print(banner+"\n")
    print(color.Green+f"[+] Members ID has been saved in this path as {color.Red}'{str(ctx.guild.name)}_memebrs_ID.txt'")
    print(color.Green+"\n.: |Done! :.\n")

@client.command()
async def wbh(ctx): #Get all server's webhooks link (Needs Webhook Permission!)
    await ctx.message.delete()
    for channel in ctx.guild.text_channels:
        try:
            webhooks = await channel.webhooks()
            for webhook in webhooks:
                print(color.Green+str(channel)+" ============>> "+webhook.name+" | "+webhook.url)
                print(color.Grey+"---------------------------------------------------------------------------------")
        except:
            continue
    print(color.Green+"\n.: |Done! :.\n")

@client.command()
async def help(ctx):
    await ctx.message.delete()
    print(color.Cyan+f"| {CMD_PREFIX}info : "+color.Green+"Show information of server")
    print(color.Cyan+f"| {CMD_PREFIX}roles : "+color.Green+"Show server's roles")
    print(color.Cyan+f"| {CMD_PREFIX}tchannels : "+color.Green+"Check roles high permissions on text channels")
    print(color.Cyan+f"| {CMD_PREFIX}vchannels : "+color.Green+"Check roles high permissions on voice channels")
    print(color.Cyan+f"| {CMD_PREFIX}access : "+color.Green+"Show roles permissions")
    print(color.Cyan+f"| {CMD_PREFIX}mid: "+color.Green+"Save all server's members ID in txt file (If server's members are more than 1K , It returens just online members!)")
    print(color.Cyan+f"| {CMD_PREFIX}wbh : "+color.Green+"Get all server's webhooks link (Needs Webhook Permission!)")
    print(color.Grey+"---------------------------------------------------------------------------------\n")
    
try:
    client.run(TOKEN , bot=False)
except:
    print(color.Red+"\n[-] Error! There is problem with your discord account token or network connection!")
    time.sleep(1)
    input(color.Cyan+"\n[+] Press any key to exit..... ")
    exit()