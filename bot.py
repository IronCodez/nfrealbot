import discord
from discord.ext import commands

import os
import json
import asyncio
import datetime
import time

import keep_alive

client = commands.Bot(command_prefix="nf!", case_insensitive=True)
token = os.environ['TOKEN']
client.remove_command('help')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_ready():
    print(f"Succesfully signed in as {client.user.name} ({client.user.id}).")
    print('------')
    #Status
    activity = discord.Activity(
        name=f'Paid My Dues | nf!help',
        type=discord.ActivityType.streaming,
        url="https://twitch.tv/nfmemes")
    await client.change_presence(activity=activity)
    print("Succesfully changed the status.")
    #Booted?
    channel = client.get_channel(720110932910538793)
    await channel.send(f'Booted at {time.ctime()}')


keep_alive.keep_alive()
client.run(token)
