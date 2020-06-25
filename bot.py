import discord
from discord.ext import commands
import os
import json
import asyncio
import time

client = commands.Bot(command_prefix = "nf!")
token = 'token'

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        
@client.event
async def on_ready():
  print(f"Succesfully signed in as {client.user.name} ({client.user.id})")
  print('------')
  #Status
  activity = discord.Activity(name=f'Paid My Dues | nf!help', type=discord.ActivityType.listening)
  await client.change_presence(activity=activity)
  print("Succesfully changed the status.")
  #Booted?
  channel = client.get_channel(720110932910538793)
  await channel.send(f'Booted at {time.ctime()}')
  

@client.command()
async def ping(ctx):
  await ctx.send(":ping_pong: Wew, I made it over the ~waves~. `{}ms` is my heartbeat (latency) :heart:.".format(round(client.latency * 1000, 3)))

client.run(token)
