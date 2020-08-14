import discord, os
from discord.ext import commands

import keep_alive

client = commands.Bot(
    command_prefix="nf!",
    description='NF Discord Bot',
    owner_id=374771579164426240,
    case_insensitive=True)

token = os.environ['TOKEN']
client.remove_command('help')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

keep_alive.keep_alive()
client.run(token, bot=True, reconnect=True)
