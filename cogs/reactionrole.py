import discord
from discord.ext import commands

class reactionrole(commands.Cog):

    def __init__(self, client):
        self.client = client

def setup(bot):
    bot.add_cog(reactionrole(bot))