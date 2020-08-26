import discord, os
from discord.ext import commands

class owner(commands.Cog):
    def __init__(self, client):
        self.client = client

# 748215605701902568
    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, *, extension="all"):
      """ Reloads cogs. """     
      if extension == "all":
        msg = await ctx.send("Reloading...")
        for filename in os.listdir('./cogs'):
          if filename.endswith('.py'):
            self.client.reload_extension(f'cogs.{filename[:-3]}')
            embed = discord.Embed(description=f"`{filename[:-3]}` was reloaded by {ctx.author.name}.", color=0x36393e)
            channel = self.client.get_channel(748215605701902568)
            await channel.send(embed=embed)
        embed = discord.Embed(description=f":white_check_mark: Successfully reloaded all of the cogs!", color=0x36393e)
        await msg.delete()
        await ctx.send(embed=embed)
      else:
        self.client.reload_extension(f'cogs.{extension}')
        embed = discord.Embed(description=f"`{extension}` was reloaded by {ctx.author.name}.", color=0x36393e)
        channel = self.client.get_channel(748215605701902568)
        await channel.send(embed=embed)
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
