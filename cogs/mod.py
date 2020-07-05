import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import random 

quotes = ["I don't rap so millions of people will like me, I rap because there's millions of people just like me", "you said you'd be there for me but, you ain't really meant it did you?", "I wish you'd just love me... back...", "this is the real me, whether I'm behind or in front of the curtain", "I don't trust these thoughts that come inside my head", "I write something then I might erase it, like something I gotta take it", "these questions start to fill my head, not again, why?", "most important things to me are things I know I can't buy", "Looking for the map to hope, you seen it?", "Sorry but I gotta leave, I don't want to be late for my therapy session", "I'm the one holding the keys", "I can take advice if it's not presented ignorantly", "whoever told you that life would be easy, I promise that person was lying to you", "this might be the last sunset I'll see, so I'll take it in", "don't tell me you're fine, cause I know you're not, so don't even try it", "my therapist told me don't bury my issues, but I 'ma be honest man, I'm feeling great!", "anger's a liar he ain't got no respect, I fell in love with my pain and I slept with my regrets, happiness saw it happen maybe that's why she got up and left, joy called me a cheater said she ain't comin' back!", "I know the person in the mirror's not a perfect one, I look at him every day and think he's not enough", "I miss the smiles we had when we were young", "I'm not ashamed to say that we had issues, I'm just ashamed that we never took care of them", "it's confusing, so amusing, how I argue with myself", "I wish that I could help, but it's hard when I hate myself", "I don't care what you think I'm just being myself, so I guess, for now, I'll just be the outcast!", "pictures don't change just the people inside of 'em do", "at least if I murder a beat, I'll take the time to go to its funeral", "y'all just driving around, I know where my lane is!", "people change even satan used to be an angel", "if you want a drink don't wait for people to pour it on you", "my mind is a home I'm trapped in, and it's lonely inside this mansion", "give me my mind back, the one that told me I was worth something when I fall flat", "it's pretty hard when things you used to love turn into things that you wish you forgot", "if you want love you gon' have to go through the pain", "I was only a kid who couldn't understand it!", "music has raised me more than my parents did", "the only person that can judge is the one in the mirror, but lately he ain't doin' it well!", "you call it music, I call it my therapist", "pain is a prison, let me out of my cell!", "if God ain't real, real isn't", "if you made a list of people would you put your name down?"]
songs = ["Escape", "Miss You", "Circles", "Beautiful", "Moments", "Your Grace", "Overdose", "Wrap Me in Your Arms", "Falling Apart", "Reality", "I'm Gonna Fly", "Until I Die", "With Me", "Understand Me", "Alone (Remix) (Ft. Sean Simmonds)", "I've Been There", "Not the Same", "I'm Free","I Got Jesus","That's Alright", "Invisible", "Goodbye", "All I have", "Wake Up", "Hands Up", "Only One", "Thing Called Love", "Just Being Me", "All I Have (remix)", "Intro", "Mansion (Ft. Fleurie)", "All I Have", "Wait", "Wake Up", "Face It", "Motivated", "Notepad", "Turn the Music Up", "Paralyzed", "I'll Keep On (Ft. Jeremiah Carlson)", "Can You Hold Me (Ft. Britt Nicole)", "Intro II", "Therapy Session", "I Just Wanna Know", "How Could You Leave Us", "Breathe", "Real", "Oh Lord", "I Can Feel It", "Got You On My Mind", "Grindin' (Ft. Marty)", "Wish You Wouldn't", "Statement", "All I Do", "Lost in the Moment (Ft. Andreas Moss)", "Intro III", "Outcast", "10 Feet Down (Ft. Ruelle)", "Green Lights", "Dreams", "Let You Down", "Destiny", "My Life", "You're Special", "If You Want Love", "Remember This", "Know", "Lie", "3 A.M.", "One Hundred","Outro", "The Search", "Leave Me Alone", "Change", "My Stress", "Nate", "Time", "Returns", "When I Grow Up", "Only by NF & Sasha Sloan", "Let Me Go", "-Interlude-", "Hate Myself", "I Miss the Days", "No Excuses", "Like This", "Options", "WHY", "Thinking", "Trauma", "Time (Edit)", "Paid My Dues", "No Name"]


class mod(commands.Cog):
    mod_role = None 

    def __init__(self, client):
        self.client = client

    @commands.command()
    @has_permissions(manage_messages=True)
    async def svs(self, ctx):
        await ctx.send("<@&728677564943695943>")
        embed = discord.Embed(color=discord.Color.default())
        embed.set_author(name="NFrealbot - Song vs Song")
        embed.add_field(name="Songs:", value=f"{(random.choice(songs))} - 🗝️ \n{(random.choice(songs))} - 🛒 ", inline=False)
        msg = await ctx.send(embed=embed)
        reactions = ['🗝️', '🛒']
        for emoji in reactions[:len(reactions)]: 
            await msg.add_reaction(emoji)

    @commands.command()
    @has_permissions(manage_messages=True)
    async def qotd(self, ctx):
        await ctx.send("<@&727892627399245906>")
        embed = discord.Embed(color=discord.Color.default())
        embed.set_author(name="NFrealbot - Qoute of the Day")
        embed.add_field(name="Quote:", value=(random.choice(quotes)))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(mod(bot))
