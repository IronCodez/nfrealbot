import discord
from discord.ext import commands

class events(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def on_message(self, message):
        if(message.channel.id == "709150055881375776"):
            await self.client.add_reaction(message, "👍")
            await self.client.add_reaction(message, "👎")
        ctx = await self.get_context(message)
        if ctx.prefix is not None:
            ctx.command = self.commands.get(ctx.invoked_with.lower())
            await self.invoke(ctx)

def setup(bot):
    bot.add_cog(events(bot))