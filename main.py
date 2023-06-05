import os

import discord
from discord import *
# from discord.app_commands import *
# from discord.ext.commands import *
# from discord.ext import *

# from selfintrod import selfintrod

intents = discord.Intents.all()

# bot = discord.Bot(intents=intents)
bot = discord.Bot(intents=intents)
bot.load_extension("selfintrod")
bot.load_extension("musiccog")

# bot.add_cog(selfintrod(bot))

@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user}")

bot.run(os.environ.get("DISCORD_TOKEN"))