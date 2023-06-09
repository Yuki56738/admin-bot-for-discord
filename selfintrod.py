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
        if message.author.bot:
            return
        if message.channel.id == 1107916826924564480:
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

        # if message.author.bot:
        #     return
        # if message.guild.id != 965354369556049990:
        #     return

        fetchedmsgs = await message.channel.history(limit=15).flatten()
        global db
        table: Table = db['notech']
        r = table.find_one(ch=message.channel.id)
        to_send_msg = r['text']
        # await message.channel.send(r['text'])
        await message.channel.send(embed=Embed(description=to_send_msg))
        self.bot: Bot
        for x in fetchedmsgs:
            if x.author.id == self.bot.user.id:
                await x.delete()

    # @commands.slash_command
    # async def debug(self, ctx: ApplicationContext):
    # ctx.guild.guild
    @commands.slash_command(name='ping')
    async def ping(self, ctx: ApplicationContext):
        await ctx.respond("Pong!")

    @commands.slash_command(name='setnote', description='Noteの文言とチャンネルを変える')
    @commands.option(name='channel', description='チャンネルID')
    @commands.option(name='text')
    async def setnote(self, ctx: ApplicationContext, channel: str, text: str):
        if not ctx.user.id == bot_author_id or not ctx.user.guild_permissions.administrator:
            await ctx.respond("権限拒否")
            return
        global db
        table: Table = db['notech']
        data = dict(ch=channel, text=text, guild=ctx.guild.id)

        table.upsert(data, ['ch'])
        r = table.find()
        for x in r:
            print(x['ch'], x['text'])
        r = table.find()
        for x in r:
            if ctx.guild.id == x['guild']:
                # ctx.channel
                await ctx.respond(f"現在の設定内容:")
                await ctx.send_followup(x['ch'] + ': ' + x['text'])

    @commands.slash_command(name='delnote', description='Noteの投稿を停止する')
    @commands.option(name='channel', description='チャンネルID')
    async def delnote(self, ctx: ApplicationContext, channel: str):
        if not ctx.user.id == bot_author_id or not ctx.user.guild_permissions.administrator:
            await ctx.respond("権限拒否")
            return
        global db
        table: Table = db['notech']
        r = table.find()
        for x in r:
            if ctx.guild.id == x['guild']:
                # ctx.channel
                await ctx.respond(f"現在の設定内容:")
                await ctx.send_followup(x['ch'] + ': ' + x['text'])
                if x['ch'] == channel:
                    x: Table
                    table.delete(ch=channel)
                    await ctx.send_followup(f'該当のチャンネルでの投稿を停止します.')

    # @Cog.listener()
    # async def on_message(self, message: Message):
    #     # if not message.channel.id == 1107916826924564480:
    #     #     return

    # to_send_text =
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
