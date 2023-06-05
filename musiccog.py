from discord.ext import commands
from discord.ext import *
from discord import *
import discord

import wavelink

class MusicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def connect_nodes(self):
        await self.bot.wait_until_ready()
        node = await wavelink.NodePool.create_node(
            bot=self.bot,
            host="risaton.net",
            port=2333,
            password="yukilava",
            https=False
        )
    @commands.Cog.listener()
    async def on_ready(self):
        print("MusicCog has been loaded.")


def setup(bot):
    bot.add_cog(MusicCog(bot))
    print("MusicCog has been added to the bot.")
