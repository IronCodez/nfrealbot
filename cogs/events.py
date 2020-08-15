import discord, time
from discord.ext import commands

class events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(
            f"Succesfully signed in as {self.client.user.name} ({self.client.user.id})."
        )
        print('------')
        #Status
        activity = discord.Activity(
            name=f'Paid My Dues | nf!help',
            type=discord.ActivityType.streaming,
            url="https://twitch.tv/nfmemes")
        await self.client.change_presence(activity=activity)
        print("Succesfully changed the status.")

        for guild in self.client.guilds:
          print(guild.name)

        """channel = self.client.get_channel(720110932910538793)
        await channel.send(f'Booted at {time.ctime()}')"""

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.client.get_channel(719710156576915556)
        await channel.send(f"**{member}** how could you leave us? :cry:")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(706976811065540609)
        await channel.send(f"Hey {member.mention}, welcome to **NFREALMUSIC** discord server:tada:! Make sure to read the <#706977106831343636> and tell us about yourself in <#710367628778274839> and grab some <#711644476627746848>.")

    @commands.command()
    async def fakeleave(self, ctx, member: discord.Member):
        await ctx.send(f"**{member}** how could you leave us? :cry:")
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(events(bot))
