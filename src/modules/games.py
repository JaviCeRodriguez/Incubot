import os
import random

from discord.ext import commands

from libs.embed import EmbedGenerator

class Games(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.PREFIX = os.getenv('DISCORD_PREFIX')

    @commands.group()
    async def game(self, ctx):
        if ctx.invoked_subcommand is not None:
            return
        
        e = EmbedGenerator(ctx)
        e.title = "[GAMES]"
        e.description = "Mini juegos disponibles"
        e.fields = [
            (f"`{self.PREFIX}game dice`", "Tirada de dados aleatoriamente")
        ]
        embed = e.generate_embed()

        await ctx.send(embed=embed)

    @game.command()
    async def dice(self, ctx):
        e = EmbedGenerator(ctx)
        e.title = "[DICE] Tira un dado"
        e.description = "¡Probá tu suerte tirando un dado!"
        e.fields = [
            ("Tu número es ", random.randint(1, 6))
        ]
        embed = e.generate_embed()
        print("Dummy print: ", random.randint(1, 6))

        await ctx.send(embed=embed)