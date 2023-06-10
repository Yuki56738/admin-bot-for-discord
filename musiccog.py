from discord import *
import discord

import wavelink

song_queue: dict = {}





class MusicCog(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.node = None
        # self.song_queue = {}

    async def on_song_end(guild_id: int, vc: wavelink.Player):
        await vc.play(song_queue[guild_id][0])

        song_queue[guild_id].pop(0)
        # if song_queue[guild_id]:
    async def connect_nodes(self):
        await self.bot.wait_until_ready()
        node = await wavelink.NodePool.create_node(
            bot=self.bot,
            host="risaton.net",
            port=2333,
            password="yukilava",
            https=False
        )
        self.node = node

    @Cog.listener()
    async def on_voice_update(self, member: Member, before: VoiceState, after: VoiceState):
        if len(before.channel.members) == 1:
            # await before.channel.guild.voice_client.disconnect()
            # vc = before.channel.guild.voice_client
            # await vc.disconnect(force=True)
            # await vc.disconnect()
            # await wavelink.Player.disconnect(self, force=True)
            vc = member.guild.voice_client
            await vc.disconnect()


    # @Cog.listener()

    @commands.slash_command(description='再生する')
    @commands.option(name='url', description='URLないし検索ワード')
    async def play(self, ctx: ApplicationContext, url: str):
        vc = ctx.voice_client
        global song_queue
        await ctx.defer()
        if not vc:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
            await vc.set_volume(2)
        if ctx.author.voice.channel.id != vc.channel.id:
            return await ctx.followup.send("BOTと同じボイスチャンネルにいる必要があります！")
        if len(vc.channel.members) == 0:
            await vc.disconnect()
        song = await wavelink.YouTubeTrack.search(query=url, return_first=True)
        if not song:
            return await ctx.followup.send("該当なし.")
        # if ctx.guild_id not in song_queue:
        #     # song_queue[ctx.guild_id] = {}
        # song_queue[ctx.guild_id].append(song)
        song_queue= song_queue|{ctx.guild_id: song}

        # song_queue: dict
        # if not len(song_queue[ctx.guild_id]) == 0:
        if song_queue[ctx.guild_id].title != '':
            await vc.play(song_queue[ctx.guild_id])
            await ctx.followup.send(f"再生中: `{vc.source.title}`")
        else:
            # song_queue[ctx.guild_id].append()
            await ctx.followup.send(f"`{song.title}` をキューに追加しました。")
        while vc.is_playing():
            await asyncio.sleep(1)
        await self.on_song_end(ctx.guild_id, vc)
    @commands.slash_command(name='stop', description='音楽を止める')
    async def stop(self, ctx: ApplicationContext):
        vc = ctx.voice_client
        # await vc.disconnect()
        await wavelink.Player.stop(vc)
        await ctx.respond(embed=Embed(description="Music stop..."))
        song_queue[ctx.guild_id] = []
    @commands.slash_command(name='leave', description='BOTを退出させる')
    async def leave(self, ctx:ApplicationContext):
        vc = ctx.voice_client
        await vc.disconnect()
        # await wavelink.Player.stop(vc)
        await ctx.respond(embed=Embed(description="Disconnecting..."))
        song_queue[ctx.guild_id] = []
    @Cog.listener()
    async def on_ready(self):
        print("MusicCog has been loaded.")
        print(f"Connecting to node...")
        await self.connect_nodes()
    @Cog.listener()
    async def on_wavelink_node_ready(node):
        print("Lava is ready.")
        # print(f"{node.stats} is ready.")  # print a message

def setup(bot):
    bot.add_cog(MusicCog(bot))
    print("MusicCog has been added to the bot.")
