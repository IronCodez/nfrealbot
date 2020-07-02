import discord
from discord.ext import commands
import random 

ball = ["As I see it, yes", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don’t count on it", "It is certain", "It is decidedly so", "Most likely", "My reply is no", "My sources say no", "Outlook good", "Outlook not so good", "Reply hazy try again", "Signs point to yes", "Very doubtful", "Without a doubt","Yes","Yes, definitely," "You may rely on it"]

class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rps(self, ctx, mode):
        if mode == 'rock':
            await ctx.send(random.choice(["You picked ROCK, I picked ROCK. We tied", "You picked ROCK, I picked PAPER. I win.", "You picked ROCK, I picked scissors. You win."]))
        elif mode == 'paper':
            await ctx.send(random.choice(["You picked PAPER, I picked ROCK. You win.", "You picked PAPER, I picked PAPER, We tied.", "You picked PAPER, I picked scissors. I win."]))
        elif mode == 'scissors':
            await ctx.send(random.choice(["You picked SCISSORS, I picked ROCK. I win.", "You picked SCISSORS, I picked PAPER, You win.", "You picked SCISSORS, I picked scissors. We tied."]))
        elif mode == 'r':
            await ctx.send(random.choice(["You picked ROCK, I picked ROCK. We tied", "You picked ROCK, I picked PAPER. I win.", "You picked ROCK, I picked scissors. You win."]))
        elif mode == 'p':
            await ctx.send(random.choice(["You picked PAPER, I picked ROCK. You win.", "You picked PAPER, I picked PAPER, We tied.", "You picked PAPER, I picked scissors. I win."]))
        elif mode == 's':
            await ctx.send(random.choice(["You picked SCISSORS, I picked ROCK. I win.", "You picked SCISSORS, I picked PAPER, You win.", "You picked SCISSORS, I picked scissors. We tied."]))

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx):
        await ctx.send(random.choice(ball))

    @commands.command(aliases=['cflip'])
    async def coinflip(self, ctx):
        await ctx.send(random.choice(["Heads", "Tails", "Sideways"]))   

def setup(bot):
    bot.add_cog(fun(bot))
