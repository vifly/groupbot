import telebot
import logging
from utils import *


try:
    from conf import TOKEN, LOGDATEFMT, DBPATH
except Exception as e:
    logging.error(e)
    exit(-1)

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(funcName)s(): %(message)s",
    datefmt=LOGDATEFMT,
)

logger = telebot.logger
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True)
def check_url(message):
    urls = get_urls(message.text)
    group_name = message.chat.title
    message_id = message.message_id

    db = BotDatabase(DBPATH)

    # For test
    urls = "".join(urls)
    if urls != "":
        bot.reply_to(message, f"提取的链接：{urls} 群组名称：{group_name} 消息 ID：{message_id}")


if __name__ == "__main__":
    bot.polling()
