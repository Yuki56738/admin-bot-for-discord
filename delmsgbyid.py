import discord
from discord import *
from discord.ext.commands import *
from discord.ui import *


class delmsgbyid(Cog):
    def __int__(self):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print('delmsgbyid ready.')

    class ModalAreyousure(discord.ui.Modal):
        def __init__(self, userid, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self.userid = userid
            self.add_item(discord.ui.InputText(label=f"Type yes in uppercase to exeute."))

        async def callback(self, interaction: Interaction):
            print(self.userid)
            interaction.response: InteractionResponse
            if self.userid == interaction.client.user.id:
                return
            if self.children[0].value == 'YES' and interaction.permissions.administrator or interaction.user.id == 816219145003466752:
                await interaction.response.send_message("deleting...")
                toDeleteember = await interaction.client.fetch_user(int(self.userid))
                print(toDeleteember.name, toDeleteember.id)
                channs = await interaction.guild.fetch_channels()
                for chann in channs:
                    # if not chann is TextChannel:
                    #     continue
                    # if chann == TextChannel:
                    #     print(3)
                    try:
                        msgs = await chann.history(limit=1000).flatten()
                    except:
                        continue
                    for x in msgs:
                        if x.author == toDeleteember:
                            # if channel_id is None:
                                print('deleting:', x.content)
                                await x.delete()
                            # elif int(x.channel.id) == int(channel_id):
                            #     print('deleting at channel:', self.bot.get_channel(int(channel_id)).name)
                            #     print('deleting:', x.content)
                            #     await x.delete()
                await interaction.followup.send('削除しました。')



    @commands.slash_command(description='IDからユーザーの投稿を全て削除する')
    # @commands.option('u)
    @commands.option('userid', description="削除対象のID", type=str)
    async def delmsgbyid(self, ctx: ApplicationContext, userid):
        # await ctx.respond()
        modal = self.ModalAreyousure(userid, title='Are you sure?')
        await ctx.send_modal(modal)


def setup(bot: Bot):
    bot.add_cog(delmsgbyid(bot))
