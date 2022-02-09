from discord.ext import commands

class Daily(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def daily(self, ctx):
        await ctx.send('hola')