# from google.cloud import firestore
# from google.cloud.firestore import *
import discord

# from discord.ext.commands import *
# from discord.ui import *
from discord import *
import dataset
from dataset import *

db = dataset.connect('sqlite:///db.sqlite')
# table = db['settings']

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

    @commands.slash_command(name='setnote', description='S***** Noteの文言とチャンネルを変える')
    @commands.option(name='channel')
    @commands.option(name='text')
    async def setnote(self, ctx: ApplicationContext, channel: str, text: str):
        global db
        table: Table = db['notech']
        data = dict(ch=channel, text=text, guild=ctx.guild.id)

        # try:
        #     # table.insert
        #     table.update(data, ['ch'])
        #
        # except:
        #     table.insert(data)
        table.upsert(data, ['ch'])
        r = table.find()
        for x in r:
            print(x['ch'], x['text'])
        # await ctx.respond(f"{ctx.guild.get_channel(table.find_one('ch')}")

        # await ctx.respond(f'{table.find()}')
        r = table.find()
        for x in r:
            if ctx.guild.id == x['guild']:
                # ctx.channel
                await ctx.respond(f"現在の設定内容:")
                await ctx.send_followup(x['ch'] + ': ' + x['text'])

    """
    @commands.slash_command(name='setselfintrodch', description='初期の自己紹介を書くCHを設定する')
    @commands.option(name='ch',type=int)
    async def setselfintrodch(self, ctx: ApplicationContext, ch: int):
        await ctx.send_response(f'Setting to {ch}...')
        global db
        # global table
        table: Table = db['beforech']
        data = dict(ch=ch)
        # table.create_column(')
        # try:
        #     table.update(data, ['id'])
        # except:
        # table.drop_column()
        # table.delete(table)
        # if table.find()
        # table.insert(data)
        # table.update(data, ['id'])
        # table = table.insert(dict())
"""

    @Cog.listener()
    async def on_ready(self):
        print("selfintrod ready.")


def setup(bot):
    bot.add_cog(selfintrod(bot))
