# from google.cloud import firestore
# from google.cloud.firestore import *
import discord

# from discord.ext.commands import *
# from discord.ui import *
from discord import *
import dataset
db = dataset.connect('sqlite:///db.sqlite/adminbot')
table = db['settings']

# db = firestore.Client()
bot_author_id = 451028171131977738


class selfintrod(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_message(self, message: Message):
        if not message.channel.id == 1107916826924564480:
            return
        if message.author.bot:
            return
        msgauthorroles = message.author.roles
        # flag = False
        hasvillager = False
        villagerrole = 0
        for x in msgauthorroles:
            # print(x.name)
            if '村人' in x.name:
                hasvillager = True
                villagerrole = x
                break
        citizenrole = 0
        for x in message.guild.roles:
            if '市民' in x.name:
                citizenrole = x
        # if message.channel.id == 965426636436697088:
        if hasvillager and message.channel.id == 1107916826924564480:
            # print('debug: now to do run some code')
            msg = message.content
            tosendchan = message.guild.get_channel(965426636436697088)
            msg = f"{message.author.mention} さんのプロフ:\n" + msg
            await tosendchan.send(msg)
            await message.delete()
            await message.author.remove_roles(villagerrole)
            await message.author.add_roles(citizenrole)

    # @commands.slash_command
    # async def debug(self, ctx: ApplicationContext):
    # ctx.guild.guild
    @commands.slash_command(name='ping')
    async def ping(self, ctx: ApplicationContext):
        await ctx.respond("Pong!")
    @commands.slash_command(name='setselfintrodch', description='初期の自己紹介を書くCHを設定する')
    @commands.option(name='ch',type=int)
    async def setselfintrodch(self, ctx: ApplicationContext, ch: int):
        await ctx.send_response(f'Setting to {ch}...')
        global db
        global table
        table = table.insert(dict(name='settings'))

    @Cog.listener()
    async def on_ready(self):
        print("selfintrod ready.")


def setup(bot):
    bot.add_cog(selfintrod(bot))
