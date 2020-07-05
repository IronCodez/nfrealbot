import discord
from discord.ext import commands

class utilities(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(color=discord.Color.green())
        embed.set_author(name="NFrealbot - Commands")
        embed.add_field(name="__Utilities and infomation Commands:__", value="Useful things.")
        embed.add_field(name="> nf!help", value="Sends this message.", inline=False)
        embed.add_field(name="> nf!ping", value="Send the latency of the bot.", inline=False)
        await ctx.send(embed=embed)
        embed = discord.Embed(color=discord.Color.green())
        embed.set_author(name="NFrealbot - Commands")
        embed.add_field(name="__Moderation Commands:__", value="Commands that you can use for moderation", inline=False)
        embed.add_field(name="> nf!svs", value="Song vs Song. (Requries `Manage Messages`)", inline=False)
        embed.add_field(name="> nf!qotd", value="Song vs Song. (Requries `Manage Messages`)", inline=False)
        await ctx.send(embed=embed)
        embed = discord.Embed(color=discord.Color.green())
        embed.set_author(name="NFrealbot - Commands")
        embed.add_field(name="__Fun Commands:__", value="Lists the fun commands of the bot.", inline=False)
        embed.add_field(name="> nf!8ball", value="a magic 8ball.", inline=False)
        embed.add_field(name="> nf!coinflip", value="Flips a coin.", inline=False)
        embed.add_field(name="> nf!rps {r, p, s}", value="It's rock paper scissors.", inline=False)
        await ctx.send(embed=embed)

    @command.commands()
    async def ping(ctx):
    await ctx.send(":ping_pong: Wew, I made it over the ~waves~. `{}ms` is my heartbeat (latency) :heart:.".format(round(self.client.latency * 1000, 3)))

def setup(bot):
    bot.add_cog(utilities(bot))
