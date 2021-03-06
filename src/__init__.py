from pathlib import Path
import logging
import os

from discord.ext import commands

BASE_DIR = Path(__file__).parent
PREFIX = os.getenv("BOT_PREFIX", "!3.")

# Set up logger
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
handler = logging.FileHandler("33bot.log")
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)


def create_bot():
    # Set up discord bot
    bot = commands.Bot(command_prefix=PREFIX)

    @bot.event
    async def on_ready():
        log.info("Logged Successfully")
        log.info(f"Bot Name: {bot.user.name}")
        log.info(f"Bot ID: {bot.user.id}")
        log.info(f"With {PREFIX=}")

    # set up opus to use voice
    # discord.opus.load_opus('libopus-0.x86.dll')

    # Register Commands
    from src.commands import (
        golden_gun,
        quote,
        random_num,
        roles,
        toggle_role,
        hello,
        heros,
        shaxx,
        thanks,
        echo,
        cs,
    )

    bot.add_command(golden_gun)
    bot.add_command(quote)
    bot.add_command(random_num)
    bot.add_command(roles)
    bot.add_command(toggle_role)
    bot.add_command(hello)
    bot.add_command(heros)
    bot.add_command(shaxx)
    bot.add_command(thanks)
    bot.add_command(echo)
    bot.add_command(cs)

    return bot


bot = create_bot()
