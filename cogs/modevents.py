import discord, time
from discord.ext import commands


class modevents(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message_delete(self, message):
      embed = discord.Embed(color=discord.Color.red(), timestamp=message.created_at,description=f"**Message sent by {message.author.mention} deleted in {message.channel.mention}** \n{message.content}")
      embed.set_author(name=f"{message.author}", icon_url=message.author.avatar_url)
      embed.set_footer(text=f"Author: {message.author.id} | Message ID: {message.id}")
      channel = self.client.get_channel(707619715903914084)
      await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_ban(self, guild, member):
      embed = discord.Embed(description=f"{member.mention} {member}", color=discord.Color.red())
      embed.set_thumbnail(url=member.avatar_url)
      embed.set_author(name="Member Banned", icon_url=member.avatar_url)
      embed.set_footer(text=f"ID: {member.id}")
      channel = self.client.get_channel(707619715903914084)
      await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_unban(self, guild, member):
      embed = discord.Embed(description=f"{member.mention} {member}", color=discord.Color.green())
      embed.set_thumbnail(url=member.avatar_url)
      embed.set_author(name="Member Unbanned", icon_url=member.avatar_url)
      embed.set_footer(text=f"ID: {member.id}")
      channel = self.client.get_channel(707619715903914084)
      await channel.send(embed=embed)
      

def setup(bot):
    bot.add_cog(modevents(bot))
