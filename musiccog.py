from discord.ext import commands
from discord.ext import *

class MusicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("MusicCog has been loaded.")


def setup(bot):
    bot.add_cog(MusicCog(bot))
    print("MusicCog has been added to the bot.")
