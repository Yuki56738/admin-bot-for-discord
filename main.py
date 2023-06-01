import os

import discord
from discord import *

intents = Intents.all()

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user}")

bot.run(os.environ.get("DISCORD_TOKEN"))