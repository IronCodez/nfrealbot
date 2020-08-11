import discord
from discord.ext import commands

import time


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
        #Booted?
        channel = self.client.get_channel(720110932910538793)
        await channel.send(f'Booted at {time.ctime()}')


def setup(bot):
    bot.add_cog(events(bot))
