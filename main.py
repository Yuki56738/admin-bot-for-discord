import os

# import discord
# from discord import Bot, Intents
from discord import *
import discord
# from discord.app_commands import *
# from discord.ext.commands import *
# from discord.ext import *

# from selfintrod import selfintrod

intents = Intents.all()

# bot = discord.Bot(intents=intents)
bot = discord.Bot(intents=intents)
bot.load_extension("selfintrod")
bot.load_extension("musiccog")


@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user}")
    for x in bot.guilds:
        print(x.name)

bot.run(os.environ.get("DISCORD_TOKEN"))