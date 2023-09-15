from discord_webhook import DiscordWebhook, DiscordEmbed
from textwrap import dedent
from user import User
from typing import List
import logging

logger = logging.getLogger(__name__)

class Notify(object):
    def __init__(self, webhook_url: str):
        self.webhook = DiscordWebhook(url=webhook_url)

    async def send(self, users: List[User]):
        success: int = 0
        failed: int = 0
        embed_body = ""
        for user in users:
            if (not user.success and user.discord_id):
                result_body = f'**{user.username}** <@{user.discord_id}>\n    {user.message}\n\n'
            else:
                result_body = f'**{user.username}**\n    {user.message}\n\n'
            if (user.success):
                success += 1
            else:
                failed += 1

            embed_body += result_body

        embed_header = dedent(f"""\
            Genshin Daily Sign-In
            - Number of successful sign-ins: {success}    
            - Number of failed sign-ins: {failed}
            """)

        embed = DiscordEmbed(title=embed_header,
                             description=embed_body, color='03b2f8')
        self.webhook.add_embed(embed)

        try:
            response = self.webhook.execute()
            if (response.status_code in [200, 204]):
                logger.info("Successfully sent Discord notification")
            else:
                raise RuntimeError(f"Received response\n{response.json()}")
        except Exception as e:
            logger.error(f"Failed to send Discord notification: {e}")
