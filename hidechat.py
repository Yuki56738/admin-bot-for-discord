import discord
from discord import *
from discord.ext.commands import *


class hidechat(Cog):
    def __int__(self):
        self.bot = bot

    @commands.slash_command()
    async def hidechat(self, ctx):
        ctx: ApplicationContext
        self.bot: Bot
        bot: Bot
        testuserid = 816219145003466752
        testuser: User = await ctx.bot.fetch_user(testuserid)
        testChannelId = 1121520790651814009
        testChannel: TextChannel = ctx.guild.get_channel(testChannelId)
        discord.PermissionOverwrite: Permissions
        perm1: PermissionOverwrite = PermissionOverwrite.from_pair(Permissions.voice(), Permissions.all())

        await testChannel.set_permissions(self, perm1)
def setup(bot):
    bot.add_cog(hidechat(bot))
