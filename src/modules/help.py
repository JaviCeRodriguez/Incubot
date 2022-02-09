import os

from discord.ext import commands

from libs.embed import ClassicEmbed, EmbedGenerator

class Help(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.PREFIX = os.getenv('DISCORD_PREFIX')

    @commands.group()
    async def help(self, ctx):
        e = EmbedGenerator(ctx)
        e.title = "[HELP] Módulos"
        e.description = "Descripción corta de todos los módulos de Incubot"
        e.fields = [
            ("Welcome", "Da la bienvenida a los nuevos usuarios (no es un comando).")
        ]
        embed = e.generate_embed()

        await ctx.send(embed=embed)

    @help.command()
    async def welcome(self, ctx):
        e = ClassicEmbed(ctx)
        e.title = "[HELP] Welcome"
        e.description = "Módulo de bienvenida a los nuevos usuarios. No existe comando, es automático!"
        embed = e.generate_embed()
        
        await ctx.send(embed=embed)
    
    @help.command()
    async def redes(self, ctx):
        e = ClassicEmbed(ctx)
        e.title = "[HELP] Redes"
        e.description = """Módulo de redes sociales. 
        El comando es prefix + redes, muestra los links de las redes sociales de Incubator."""
        embed = e.generate_embed()
        
        await ctx.send(embed=embed)
    
    @help.command()
    async def games(self, ctx):
        e = ClassicEmbed(ctx)
        e.title = "[HELP] Games"
        e.description = """Módulo de juegos. Lista de juegos disponibles hasta el momento: 
        - roll_dice"""
        embed = e.generate_embed()
        
        await ctx.send(embed=embed)