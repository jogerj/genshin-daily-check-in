from genshin import Region
from typing import Dict, List
from os.path import exists
from user import User
import json
from random import random


class GenshinConfig(object):
    __instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls.__instance is None:
            cls.__instance = cls.__new__(cls)

            config_path = 'config.json'
            if not exists(config_path):
                raise FileNotFoundError(
                    f'Config file not found: {config_path}')
            with open(config_path, 'r') as f:
                config = json.load(f)

            cls.__instance.discord_webhook: str = cls.__discord_webhook(config)
            cls.__instance.users: List[User] = cls.__users(cls, config)
            cls.__instance.delay: int = config.get('delay', 60)

        return cls.__instance

    def __discord_webhook(config: Dict[str, any]) -> str:
        webhook_url = config.get('discord_webhook_url')
        if (not webhook_url):
            return None
        return webhook_url

    def __users(self, config: Dict[str, any]) -> List[User]:
        users: List[User] = []
        for user in list(config.get('users')):
            auto_claim = user.get('auto_claim', True)
            username = user.get('username')
            region_str = user.get('region')
            cookie = user.get('cookie')
            discord_id = user.get('discord_id')
            region = self.__parse_region(region_str)
            if (not username or not region or not cookie):
                print(f"User missing username, region, or cookie: {user}")
                continue
            user = User(auto_claim=auto_claim,
                        region=region,
                        username=username,
                        cookie=cookie,
                        discord_id=discord_id)
            users.append(user)
        users.sort(key=lambda user: (user.auto_claim, random()))
        return users

    def __parse_region(region: str) -> Region:
        if (region == 'cn' or region == 'china'):
            return Region.CHINESE
        elif (region == 'os' or region == 'overseas'):
            return Region.OVERSEAS
        return None
