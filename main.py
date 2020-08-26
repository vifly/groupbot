import telebot
import logging
from utils import *


try:
    from conf import TOKEN, LOGDATEFMT
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

    # For test
    urls = "".join(urls)
    if urls != "":
        bot.reply_to(message, urls)


if __name__ == "__main__":
    bot.polling()
