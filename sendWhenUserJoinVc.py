import os

import discord
from discord import *
from discord.ext.commands import *
import sendgrid
from sendgrid import From, To
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv


class sendWhenUserJoinVc(Cog):
    def __int__(self):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print(f"sendWhenUserJoinVc ready.")

    @Cog.listener()
    async def on_voice_state_update(self, member: Member, before: VoiceState, after: VoiceState):
        if before.channel is None and after.channel is not None:
            load_dotenv()
            sg = sendgrid.SendGridAPIClient(
                api_key=os.environ.get("SG_TOKEN"))
            from_email = From(os.environ.get("MAIL_ADDR"), 'adminbot-discord')
            to_email = To(os.environ.get("MAIL_ADDR"), 'Yuki')
            subject = 'adminbot notify: joined user'
            content = f"User: {member.name} ({member.display_name}) joined vc at {member.guild.name}."
            message = Mail(from_email=from_email, to_emails=to_email, subject=subject, html_content=content)
            response = sg.send(message)
            print(response.status_code)


def setup(bot):
    bot.add_cog(sendWhenUserJoinVc(bot))
    print(f'sendWhenUserJoinVc added.')
