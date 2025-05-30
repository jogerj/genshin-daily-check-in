#!/usr/bin/env python3

import asyncio
import genshin
from config import GenshinConfig
from user import User
from notify import Notify
from typing import Dict, List
import logging


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(levelname)s | %(message)s',
        datefmt='%Y-%m-%dT%H:%M:%S%z')
    logger = logging.getLogger('genshin-daily-check-in')
    config = GenshinConfig.instance()
    users: List[User] = config.users

    for i, user in enumerate(users):
        if (not user.auto_claim):
            user.success = False
            user.message = "Reminder to claim your daily reward!"
        else:
            try:
                client = genshin.Client(
                    game=genshin.Game.GENSHIN,
                    region=user.region)
                client.set_cookies(user.cookie)
                reward = await client.claim_daily_reward()
            except genshin.AlreadyClaimed:
                user.success = True
                user.message = "Daily reward already claimed"
            except genshin.DailyGeetestTriggered as e:
                user.success = False
                user.message = "Geetest triggered"
            except (genshin.CookieException, genshin.InvalidCookies) as e:
                user.success = False
                user.message = f"Cookie issue: {e}"
            except Exception as e:
                user.success = False
                user.message = f"Failed to claim daily reward! Unknown error:\n    {e}!"
            else:
                user.success = True
                user.message = f"Claimed {reward.amount}x {reward.name}"
        if (user.success or not user.auto_claim):
            logger.info(f"{user.username} ({user.region}): {user.message}")
        else:
            logger.warning(f"{user.username} ({user.region}): {user.message}")
        if (user.auto_claim and i < len(users) -1):
            await asyncio.sleep(config.delay)

    if (config.discord_webhook):
        logger.info("Sending Discord notification")
        notify = Notify(config.discord_webhook)
        notification_result: str = await notify.send(reversed(users))
    else:
        logger.info("No Discord webhook set, not sending any notifications")

if (__name__ == '__main__'):
    asyncio.run(main())
