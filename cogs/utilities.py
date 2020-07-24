import discord
from discord.ext import commands

class utilities(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(":ping_pong: Wew, I made it over the ~waves~. `{}ms` is my heartbeat (latency) :heart:.".format(round(self.client.latency * 1000, 3)))

    @commands.command()
    @commands.has_permissions(add_reactions=True,embed_links=True)
    async def help(self, ctx):
        embed = discord.Embed(color=discord.Color.green(), timestamp=ctx.message.created_at)
        embed.set_author(name=f"Help - NFrealbot \nPrefix: nf!")
        embed.add_field(name="Infomation", value='General and Infomational commands.', inline=False)
        embed.add_field(name="> nf!help", value="```Sends the help command.```", inline=True)
        embed.add_field(name="> nf!ping", value="```Sends the latency of the bot.```", inline=True)
        embed.add_field(name="> nf!serversuggestion", value="```Suggest something to be added to the server.```", inline=True)
        embed.add_field(name="> nf!serverinfo", value="```Sends infomation about the serer.```", inline=True)
        embed.add_field(name="> nf!membercount", value="Sends the member count of the server.", inline=True)
        embed.add_field(name="NF", value="NF commands.", inline=False)
        embed.add_field(name="> nf!song", value="Send a random song made by NF.", inline=True)
        embed.add_field(name="> nf!quote", value="Send a random quote said by NF.", inline=True)
        embed.add_field(name="> nf!album", value="Sends a random album made by NF.", inline=True)
        embed.add_field(name="> nf!social", value="```Sends all of NF's socials.```", inline=True)
        embed.add_field(name="Fun", value="Fun commands.", inline=False)
        embed.add_field(name="> nf!rps", value="```Rock, paper, scissors.```", inline=True)
        embed.add_field(name="> nf!8ball", value="```Magic 8ball.```", inline=True)
        embed.add_field(name="> nf!coinflip", value="```Flips a coin.```", inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def serversuggestion(self, ctx, *, content:str):
        embed = discord.Embed(color=discord.Color.green(), timestamp=ctx.message.created_at)
        embed.set_author(name="Server Suggestion - NFrealbot")
        embed.set_footer(text=f"Suggested by {ctx.author.name} ({ctx.author.id}) | Suggested on ")
        embed.add_field(name="Suggestion", value=content)
        channel = self.client.get_channel(709150055881375776)
        msg = await channel.send(embed=embed)
        reactions = ['👍', '👎']
        for emoji in reactions[:len(reactions)]: 
            await msg.add_reaction(emoji)
        await ctx.send('✅ Sent the suggestion.')

    @commands.command()
    async def serverinfo(self, ctx, guild: discord.Guild = None):
        guild = ctx.author.guild
        embed = discord.Embed(color=guild.owner.color, timestamp=guild.created_at)
        embed.set_author(name=f"{guild.name}", icon_url=guild.icon_url)
        embed.set_footer(text=f"ID: {guild.id} | Server Created")
        embed.add_field(name="Owner", value=guild.owner)
        embed.add_field(name="Region", value=guild.region)
        embed.add_field(name="Channel Catergories", value=len(guild.categories))
        embed.add_field(name="Text Channels", value=len(guild.text_channels))
        embed.add_field(name="Voice Channels", value=len(guild.voice_channels))
        embed.add_field(name="Members", value=len(guild.members))
        embed.add_field(name="Roles", value=len(guild.roles))
        await ctx.send(embed=embed)

    @commands.command()
    async def membercount(self, ctx, guild:discord.Guild=None):
        guild = ctx.author.guild
        embed = discord.Embed(color=guild.owner.color, timestamp=ctx.message.created_at)
        embed.set_footer(text="Member count at")
        embed.set_author(name=f"{guild.name}'s Member Count - NFrealbot", icon_url=guild.icon_url)
        embed.add_field(name="All Members", value=len(guild.members))
        embed.add_field(name="Humans", value=len(list(filter(lambda m: not m.bot, ctx.guild.members))))
        embed.add_field(name="Bots", value=len(list(filter(lambda m: m.bot, ctx.guild.members))))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(utilities(bot))
