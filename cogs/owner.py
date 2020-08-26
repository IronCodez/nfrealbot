import discord
from discord.ext import commands

class owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, *, extension="all"):
      """ Reloads cogs. """
      if extension == "all":
        self.client.reload_extension(f'cogs.events')
        self.client.reload_extension(f'cogs.fun')
        self.client.reload_extension(f'cogs.mental')
        self.client.reload_extension(f'cogs.mod')
        self.client.reload_extension(f'cogs.modevents')
        self.client.reload_extension(f'cogs.nf')
        self.client.reload_extension(f'cogs.owner')
        self.client.reload_extension(f'cogs.utilities')
        embed = discord.Embed(description=":white_check_mark: Successfully reloaded all of the cogs!", color=0x36393e)
        await ctx.send(embed=embed)
      else:
        self.client.reload_extension(f'cogs.{extension}')
        embed = discord.Embed(description=f":white_check_mark: Successfully reloaded the cog `{extension}`!", color=0x36393e)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def stop(self, ctx):
        """ Stops the bot. """
        await ctx.send(f'Stopping {self.client.user.name}...')
        await self.client.change_presence(activity=discord.Game(type=0, name='Stopping...'), status=discord.Status.dnd)
        await self.client.logout()

def setup(bot):
    bot.add_cog(owner(bot))
