from urlextract import URLExtract
from peewee import *

DB = SqliteDatabase(None)


def get_urls(message: str) -> list:
    extractor = URLExtract()
    urls = extractor.find_urls(message)
    return urls


def get_tg_message_url(chat_name: str, message_id: str) -> str:
    raise NotImplementedError


class BotDatabase:
    class Message(Model):
        url = TextField()
        group_name = TextField()
        tg_message_url = TextField()

        class Meta:
            database = DB

    def __init__(self, db_path: str):
        DB.init(db_path)
        with DB:
            DB.create_tables([self.Message])

    def add(self, url: str, group_name: str, tg_message_url: str = ""):
        message = self.Message(url=url, group_name=group_name, tg_message_url=tg_message_url)
        message.save()

    def is_url_in_db(self, url: str) -> bool:
        try:
            result = self.Message.get(self.Message.url == url)
            return True
        except:
            return False
