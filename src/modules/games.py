import random
import os

from discord.ext import commands

from libs.embed import EmbedGenerator, ClassicEmbed

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
    async def dice(self, ctx, amount, number = 6):
        try:
            number = int(number)
            e = EmbedGenerator(ctx)
            c = ClassicEmbed(ctx)
            e.title = "[DICE] Tira un dado"
            e.description = "¡Probá tu suerte tirando un dado!"
            dados = []
            for i in range(int(amount)):
                dados.append(("Dado", random.randint(1, number)))
            e.fields = dados
            embed = e.generate_embed()

            await ctx.send(embed=embed)
        except ValueError:
            c.title = "[HELP] Formato invalido"
            c.description = f"""Ingresaste un formato invalido.\n\nFormato aceptado:
```{self.PREFIX}game dice <amount> <number>
<amount> = Cantidad de dados a tirar
<number> = Cantidad de caras del dado```\n
Ejemplo: ```{self.PREFIX}game dice 2 6```"""
            embed = c.generate_embed()
            await ctx.send(embed=embed)