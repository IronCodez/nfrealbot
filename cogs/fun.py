import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import sys
import random 
import json
from discord.utils import get
from datetime import datetime

ball = ["As I see it, yes", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don’t count on it", "It is certain", "It is decidedly so", "Most likely", "My reply is no", "My sources say no", "Outlook good", "Outlook not so good", "Reply hazy try again", "Signs point to yes", "Very doubtful", "Without a doubt","Yes","Yes, definitely," "You may rely on it"]
albums = ["Moments", "I'm Free", "NF: EP", "Mansion", "Therapy Session", "Perception", "The Search"]
quotes = ["i don't rap so millions of people will like me, i rap because there's millions of people just like me", "you said you'd be there for me but, you ain't really meant it did you?", "i wish you'd just love me... back...", "this is the real me, wether i'm behind or in front of the curtain", "i don't trust these thoughts that come inside my head", "i write something then i might erase it, like something i gotta take it", "these questions start to fill my head, not again, why?", "most important things to me are things i know i can't buy", "Looking for the map to hope, you seen it?", "sorry but i gotta leave, i don't want to be late for my therapy session", "i'm the one holding the keys", "i can take advice if it's not presented ignorantly", "whoever told you that life would be easy, i promise that person was lying to you", "this might be the last sunset i'll see, so i'll take it in", "don't tell me you're fine, cause i know you're not, so don't even try it", "my therapist told me don't burry my issues, but i'ma be honest man, i'm feeling great!", "anger's a liar he ain't got no respect, i fell in love with my pain and i slept with my regrets, happiness saw it happen maybe that's why she got up and left, joy called me a cheater said she ain't comin back!", "i know the person in the mirror's not a perfect one, i look at him everyday and think he's not enough", "i miss the smiles we had when we were young", "i'm not ashamed to say that we had issues, i'm just ashamed that we never took care of them", "it's confusing, so amusing, how i argue with myself", "i wish that i could help, but it's hard when i hate myself", "i don't care what you think i'm just being myself, so i guess for now, i'll just be the outcast!", "pictures don't change just the people inside of 'em do", "at least if i murder a beat, i'll take the time to go to it's funeral", "y'all just driving around, i know where my lane is!", "people change even satan used to be an angel", "if you want a drink don't wait for people to pour it on you", "my mind is a home i'm trapped in, and it's lonely inside this mansion", "give me my mind back, the one that told me i was worth something when i fall flat", "it's pretty hard when things you used to love turn into things that you wish you forgot", "if you want love you gon' have to go through the pain", "i was only a kid who couldn't understand it!", "music has raised me more than my parents did", "the only person that can judge is the one in the mirror, but lately he ain't doin' it well!", "you call it music, i call it my therapist", "pain is a prison, let me out of my cell!", "if God ain't real, real isn't", "if you made a list of people would you put your name down?"]
songs = ["Escape", "Miss You", "Circles", "Beautiful", "Moments", "Your Grace", "Overdose", "Wrap Me in Your Arms", "Falling Apart", "Reality", "I'm Gonna Fly", "Until I Die", "With Me", "Understand Me", "Alone (Remix) (Ft. Sean Simmonds)", "I've Been There", "Not the Same", "I'm Free","I Got Jesus","That's Alright", "Invisible", "Goodbye", "All I have", "Wake Up", "Hands Up", "Only One", "Thing Called Love", "Just Being Me", "All I Have (remix)", "Intro", "Mansion (Ft. Fleurie)", "All I Have", "Wait", "Wake Up", "Face It" "Motivated", "Notepad", "Turn the Music Up", "Paralyzed", "I'll Keep On (Ft. Jeremiah Carlson)", "Can You Hold Me (Ft. Britt Nicole)", "Intro II", "Therapy Session", "I Just Wanna Know", "How Could You Leave Us", "Breathe", "Real", "Oh Lord", "I Can Feel It", "Got You On My Mind", "Grindin' (Ft. Marty)", "Wish You Wouldn't", "Statement", "All I Do", "Lost in the Moment (Ft. Andreas Moss)", "Intro III", "Outcast", "10 Feet Down (Ft. Ruelle)", "Green Lights", "Dreams", "Let You Down", "Destiny", "My Life", "You're Special", "If You Want Love", "Remember This", "Know", "Lie", "3 A.M.", "One Hundred","Outro", "The Search", "Leave Me Alone", "Change", "My Stress", "Nate", "Time", "Returns", "When I Grow Up", "Only by NF & Sasha Sloan", "Let Me Go", "-Interlude-", "Hate Myself", "I Miss the Days", "No Excuses", "Like This", "Options", "WHY", "Thinking", "Trauma", "Time (Edit)", "Paid My Dues", "No Name"]


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

    @commands.command()
    async def album(self, ctx):
        embed = discord.Embed(color=discord.Color.default())
        embed.set_author(name="NFrealbot - Random Album")
        embed.add_field(name="**Your random album is...**", value=(random.choice(albums)))
        await ctx.send(embed=embed)

    @commands.command()
    async def quote(self, ctx):
        embed = discord.Embed(color=discord.Color.default())
        embed.set_author(name="NFrealbot - Random Quote")
        embed.add_field(name="**Your random quote is...**", value=(random.choice(quotes)))
        await ctx.send(embed=embed)

    @commands.command()
    async def song(self, ctx):
        embed = discord.Embed(color=discord.Color.default())
        embed.set_author(name="NFrealbot - Random Song")
        embed.add_field(name="**Your random song is...**", value=(random.choice(songs)))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(fun(bot))
