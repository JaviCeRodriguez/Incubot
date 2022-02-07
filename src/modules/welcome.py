import os

from discord.ext import commands

class Welcome(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.channel_id = int(os.getenv("DISCORD_WELCOME_CH_ID"))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(self.channel_id)
        await channel.send(f"Bienvenido <@{member.id}>!")
