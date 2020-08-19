import discord, random, asyncio
from discord.ext import commands

ball = [
    "Leave me alone", "WHY?", "LIES LIES LIES",
    "Should I throw that in the trash?", "No!"
    "Where'd the beat go?", "It is certain", "It is decidedly so",
    "Most likely", "My reply is no", "My sources say no", "Outlook good",
    "Outlook not so good", "Reply hazy try again", "Signs point to yes",
    "Very doubtful", "Without a doubt", "Yes", "You may rely on it"
]


class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rps(self, ctx, mode=None):
        if mode == None:
            embed = discord.Embed(color=0x36393e)
            embed.set_author(name="nf!rps - NFrealbot")
            embed.add_field(name="Description:",value="Rock Paper Scissors.",inline=False)
            embed.add_field(name="Useage:", value="nf!rps {choice}", inline=False)
            embed.add_field(name="Example:",value="nf!rps rock \nnf!rps paper\nnf!rps scissors")
            await ctx.send(embed=embed)

        elif mode == 'rock':
          embed = discord.Embed(color=0x36393e)
          embed.add_field(name="Your Choice", value="Rock", inline=False)
          embed.add_field(name="My Choice", value=random.choice(["Rock, we tied.", "Paper, you lost.", "Scissors, I lose."]))
          await ctx.send(embed=embed)

        elif mode == 'paper':
          embed = discord.Embed(color=0x36393e)
          embed.add_field(name="Your Choice", value="Paper", inline=False)
          embed.add_field(name="My Choice", value=random.choice(["Rock, you lose.", "Paper, we tied.", "Scissors, I win."]))
          await ctx.send(embed=embed)

        elif mode == 'scissors':
          embed = discord.Embed(color=0x36393e)
          embed.add_field(name="Your Choice", value="Scissors", inline=False)
          embed.add_field(name="My Choice", value=random.choice(["Rock, you win.", "Paper, you lost.", "Scissors, we tied."]))
          await ctx.send(embed=embed)

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, content: str = None):
        if content == None:
            embed = discord.Embed(color=discord.Color.default())
            embed.set_author(name="nf!8ball - NFrealbot")
            embed.add_field(
                name="Description:", value="Magic 8ball", inline=False)
            embed.add_field(
                name="Useage:", value="nf!8ball {question}", inline=False)
            embed.add_field(name="Example:", value="nf!8ball is nfbot good?")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=discord.Color.default())
            embed.set_author(name="nf!8ball - NFrealbot")
            embed.add_field(name="Question", value=content, inline=False)
            embed.add_field(
                name="Answer", value=random.choice(ball), inline=False)
            await ctx.send(embed=embed)

    @commands.command(aliases=['cflip'])
    async def coinflip(self, ctx):
        await ctx.send(random.choice(["Heads", "Tails", "Sideways"]))

    @commands.command(aliases=['rnumber'])
    async def randomnumber(self, ctx):
        embed = discord.Embed(color=discord.Color.default())
        embed.set_author(name="nf!randomnumber - NFrealbot")
        embed.add_field(name="Random Number", value=random.randint(0, 101))
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(fun(bot))
