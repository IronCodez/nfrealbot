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
        channel = self.client.get_channel(720110932910538793)
        await channel.send(f'Booted at {time.ctime()}')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.client.get_channel(719710156576915556)
        await channel.send(f"**{member}** how could you leave us? :cry:")

    @commands.command()
    async def fakeleave(self, ctx, member: discord.Member):
        await ctx.send(f"**{member}** how could you leave us? :cry:")

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        embed = discord.Embed(
            color=discord.Color.red(),
            timestamp=message.created_at,
            description=
            f"**Message sent by {message.author.mention} deleted in {message.channel.mention}** \n{message.content}"
        )
        embed.set_author(
            name=f"{message.author}", icon_url=message.author.avatar_url)
        embed.set_footer(
            text=f"Author: {message.author.id} | Message ID: {message.id}")
        channel = self.client.get_channel(707619715903914084)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(events(bot))
