import discord, os, datetime, time
from discord.ext import commands

import keep_alive

start_time = time.time()

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

@client.command()
async def info(ctx):
  """ The bot's info. """
  current_time = time.time()
  difference = int(round(current_time - start_time))
  text = str(datetime.timedelta(seconds=difference))
  embed = discord.Embed(color=discord.Color.green())
  embed.set_author(name=f"{client.user.name}'s Info")
  embed.set_footer(text=f"Ping: {round(client.latency * 1000)}ms | Uptime: {text}")
  embed.add_field(name="Version", value="2020.25.8", inline=True)
  embed.add_field(name="Libary", value=f"discord.py {discord.__version__}", inline=True)        
  embed.add_field(name="Language", value="Python 3.8.3")
  embed.add_field(name="Developer", value="bread#7620", inline=True)
  embed.add_field(name="Users", value=f"`{len(set(client.get_all_members()))}`", inline=True)
  embed.add_field(name="Github", value=f"(https://github.com/IronCodez/nfrealbot/)[Click Here]")
  embed.add_field(name="Donate", value=f"**Coming soon.**")
  await ctx.send(embed=embed)

keep_alive.keep_alive()
client.run(token, bot=True, reconnect=True)
