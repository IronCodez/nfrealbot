import discord, random
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

quotes = [
    "I don't rap so millions of people will like me, I rap because there's millions of people just like me",
    "this is the real me, whether I'm behind or in front of the curtain",
    "I write something then I might erase it, like something I gotta take it",
    "these questions start to fill my head, not again, why?",
    "Sorry but I gotta leave, I don't want to be late for my therapy session",
    "don't tell me you're fine, cause I know you're not, so don't even try it",
    "y'all just driving around, I know where my lane is!",
    "people change even satan used to be an angel",
    "my mind is a home I'm trapped in, and it's lonely inside this mansion",
    "you call it music, I call it my therapist",
    "if you made a list of people would you put your name down?",
    "woo",
    "pick at the bars you gotta be smart if you wanna get to the root of it",
    "Yeah, I said I was coming, I warned you",
    "All I spit is real life",
    "you dont like me that makes two of us",
    "Take my chances, I just roll the dice, do what I like",
    "LIES LIES LIES",
    "WHY",
    "When I grow up",
    "I hold my issues up for all to see, like show and tell; A lot of people know me, but not a lot know me well",
]
songs = [
    "Escape", "Miss You", "Circles", "Beautiful", "Moments", "Your Grace",
    "Overdose", "Wrap Me in Your Arms", "Falling Apart", "Reality",
    "I'm Gonna Fly", "Until I Die", "With Me", "Understand Me",
    "Alone (Remix) (Ft. Sean Simmonds)", "I've Been There", "Not the Same",
    "I'm Free", "I Got Jesus", "That's Alright", "Invisible", "Goodbye",
    "All I have", "Wake Up", "Hands Up", "Only One", "Thing Called Love",
    "Just Being Me", "All I Have (remix)", "Intro", "Mansion (Ft. Fleurie)",
    "All I Have", "Wait", "Wake Up", "Face It", "Motivated", "Notepad",
    "Turn the Music Up", "Paralyzed", "I'll Keep On (Ft. Jeremiah Carlson)",
    "Can You Hold Me (Ft. Britt Nicole)", "Intro II", "Therapy Session",
    "I Just Wanna Know", "How Could You Leave Us", "Breathe", "Real",
    "Oh Lord", "I Can Feel It", "Got You On My Mind", "Grindin' (Ft. Marty)",
    "Wish You Wouldn't", "Statement", "All I Do",
    "Lost in the Moment (Ft. Andreas Moss)", "Intro III", "Outcast",
    "10 Feet Down (Ft. Ruelle)", "Green Lights", "Dreams", "Let You Down",
    "Destiny", "My Life", "You're Special", "If You Want Love",
    "Remember This", "Know", "Lie", "3 A.M.", "One Hundred", "Outro",
    "The Search", "Leave Me Alone", "Change", "My Stress", "Nate", "Time",
    "Returns", "When I Grow Up", "Only by NF & Sasha Sloan", "Let Me Go",
    "-Interlude-", "Hate Myself", "I Miss the Days", "No Excuses", "Like This",
    "Options", "WHY", "Thinking", "Trauma", "Time (Edit)", "Paid My Dues",
    "No Name"
]


class mod(commands.Cog):
    mod_role = None

    def __init__(self, client):
        self.client = client

    @commands.command()
    @has_permissions(manage_messages=True)
    async def svs(self, ctx):
        await ctx.send("<@&728677564943695943>")
        embed = discord.Embed(title="Song vs Song", description=f"{(random.choice(songs))} - 🗝️ \n{(random.choice(songs))} - 🛒", color=0x36393e)
        msg = await ctx.send(embed=embed)
        reactions = ['🗝️', '🛒']
        for emoji in reactions[:len(reactions)]:
            await msg.add_reaction(emoji)
        await ctx.message.delete()

        embed = discord.Embed(color=discord.Color.blue(), description=f"Used `nf!svs` in {ctx.channel.mention}")
        embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar_url)
        channel = self.client.get_channel(736051087412559954)
        await channel.send(embed=embed)

    @commands.command()
    @has_permissions(manage_messages=True)
    async def qotd(self, ctx):
        await ctx.send("<@&727892627399245906>")
        embed = discord.Embed(title="Quote of the Day", description=f"{(random.choice(quotes))}", color=0x36393e)
        await ctx.send(embed=embed)
        await ctx.message.delete()
        embed = discord.Embed(color=discord.Color.blue(), description=f"Used `nf!qotd` in {ctx.channel.mention}")
        embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar_url)
        channel = self.client.get_channel(736051087412559954)
        await channel.send(embed=embed)

    @commands.command()
    @has_permissions(ban_members=True)
    async def kick(self, ctx, member: discord.Member = None, *,reason=f"No reason given."):
        if not member:
            embed = discord.Embed(color=discord.Color.default())
            embed.set_author(name="nf!kick - NFrealbot")
            embed.add_field(
                name="Description:",
                value="Kicks the specifed user.",
                inline=False)
            embed.add_field(
                name="Usage:", value="nf!kick {member} (reason)", inline=False)
            embed.add_field(
                name="Example:",
                value=
                "nf!kick bread#7620 3 warnings \nnf!kick 374771579164426240 3 warnings\nnf!kick @bread 3 warnings"
            )
            await ctx.send(embed=embed)
            return
        else:
            await member.kick(reason=reason)
            await ctx.send(f"Kicked {member} for {reason}")

            embed = discord.Embed(color=discord.Color.blue(), description=f"Used `nf!kick` in {ctx.channel.mention} \nnf!kick {member} {reason}")
            embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar_url)
            channel = self.client.get_channel(736051087412559954)
            await channel.send(embed=embed)
            #dms user
            embed = discord.Embed(color=discord.Color.default())
            embed.set_author(name=f"Kicked in {ctx.guild} - NFrealbot")
            embed.add_field(name="Reason:", value=reason, inline=False)
            await member.send(embed=embed)

    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason=f"No reason given."):
        if not member:
            embed = discord.Embed(color=discord.Color.default())
            embed.set_author(name="nf!ban - NFrealbot")
            embed.add_field(
                name="Description:",
                value="Bans the specifed user.",
                inline=False)
            embed.add_field(
                name="Usage:", value="nf!ban {member} (reason)", inline=False)
            embed.add_field(
                name="Example:",
                value=
                "nf!ban bread#7620 3 warnings \nnf!ban 374771579164426240 3 warnings\nnf!ban @bread 3 warnings"
            )
            await ctx.send(embed=embed)
            return
        else:
            await member.ban(reason=reason)
            await ctx.send(f"Banned {member} for {reason}")
            embed = discord.Embed(color=discord.Color.blue(), description=f"Used `nf!ban` in {ctx.channel.mention} \nnf!ban {member} {reason}")
            embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar_url)
            channel = self.client.get_channel(736051087412559954)
            await channel.send(embed=embed)
            #dms user
            embed = discord.Embed(color=discord.Color.default())
            embed.set_author(name=f"Banned in {ctx.guild} - NFrealbot")
            embed.add_field(name="Reason:", value=reason, inline=False)
            embed.add_field(
                name="Appeal here:",
                value=
                "[Click here](https://forms.gle/af871S1EJvr4m9pE6) *Note: If you have appiled in the past you will not get accepted*"
            )
            await member.send(embed=embed)
            #sends in logs

    @commands.command()
    async def staff(self, ctx):
        embed = discord.Embed(color=0x36393e)
        embed.set_author(name="Staff list")
        embed.add_field(
            name="Founders",
            value="<@456981595694563368>\n<@487057466476199949>",
            inline=False)
        embed.add_field(
            name="Managers",
            value=
            "<@374771579164426240>\n<@559859899274887169>\n<@623200653426032682>",
            inline=False)
        embed.add_field(
            name="Supervisors",
            value=
            "<@527186281134817281> \n<@411200029253042186> \n<@707075298251898991>",
            inline=False)
        embed.add_field(
            name="Admins",
            value="<@591108193703428097>\n<@688059678663377084> ",
            inline=False)
        embed.add_field(
            name="Mods",
            value="<@700248807971094579>\n<@626898896878174220>",
            inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(mod(bot))
