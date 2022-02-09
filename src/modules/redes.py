import os

from discord.ext import commands

from libs.embed import ClassicEmbed, EmbedGenerator

class Redes(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def redes(self, ctx):
        e = EmbedGenerator(ctx)
        e.title = "[SOCIALS] Links de redes sociales"
        e.description = "Links de redes sociales de Incubot"
        e.fields = [
            ("Twitter", "Todavía no disponible"),
            ("Discord", "Es privado panflin"),
            ("Página Web", "https://incubator.com.ar/"),
            ("Linkedin", "https://www.linkedin.com/company/incubator-ar/")
        ]
        embed = e.generate_embed()

        await ctx.send(embed=embed)