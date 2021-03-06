import os
import sys
import logging

import discord
from discord.ext import commands
from dotenv import load_dotenv

import modules

log = logging.getLogger("main")


def config_log():
    logging.basicConfig(
        format="%(asctime)-30s %(name)-20s %(levelname)-10s %(message)s",
        level=logging.INFO,
    )


if __name__ == "__main__":
    load_dotenv()
    config_log()

    intents = discord.Intents.default()
    intents.members = True

    # Importo las variables de entorno
    PREFIX = os.getenv("DISCORD_PREFIX")
    TOKEN = os.getenv("DISCORD_TOKEN")

    if TOKEN is None:
        log.info("Token not found ...")
        sys.exit(0)

    bot = commands.Bot(
        command_prefix=commands.when_mentioned_or(PREFIX),
        description="Bot Incubator",
        help_command=None,
        intents=intents
    )

    # Lista de módulos activos
    bot.add_cog(modules.Help(bot))
    bot.add_cog(modules.Welcome(bot))
    bot.add_cog(modules.Daily(bot))
    bot.add_cog(modules.Redes(bot))
    bot.add_cog(modules.Games(bot))

    log.info("Bot started ...")
    bot.run(TOKEN)