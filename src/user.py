from logging import Logger
from genshin import Region


class User(object):
    def __init__(self,
                 auto_claim: bool,
                 region: Region,
                 username: str,
                 cookie: str,
                 discord_id: str = None):
        self.auto_claim: bool = auto_claim
        self.region: Region = region
        self.username: str = username
        self.cookie: str = cookie
        self.discord_id: str = discord_id
        self.success: bool = None
        self.message: str = None
