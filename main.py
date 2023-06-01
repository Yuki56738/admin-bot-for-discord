import os

import discord
from discord import *
# from discord.app_commands import *
# from discord.ext.commands import *
# from discord.ext import *

from selfintrod import selfintrod

intents = Intents.all()

bot = Bot(intents=intents, command_prefix=None)
bot.load_extension("selfintrod")


# bot.add_cog(selfintrod(bot))

@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user}")

bot.run(os.environ.get("DISCORD_TOKEN"))