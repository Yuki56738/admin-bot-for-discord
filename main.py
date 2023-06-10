import os

from discord import *
import discord

from dotenv import load_dotenv
load_dotenv()

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