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

keep_alive.keep_alive()
client.run(token)
