import random

from discord.ext import commands

from libs.embed import EmbedGenerator

class Games(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.group()
    async def game(self, ctx):
        pass

    @game.command()
    async def dice(self, ctx):
        e = EmbedGenerator(ctx)
        e.title = "[DICE] Tira un dado"
        e.description = "¡Probá tu suerte tirando un dado!"
        e.fields = [
            ("Tu número es ", random.randint(1, 6))
        ]
        embed = e.generate_embed()

        await ctx.send(embed=embed)