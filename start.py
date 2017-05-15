# coding: utf-8

from telegram.ext import Updater, CommandHandler


import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)

logger = logging.getLogger(__name__)


def get_token():
    with open('token.txt') as token_file:
        token = token_file.read().strip()
        logger.info("token: {}".format(token))
    return token

def start(bot, update):
    update.message.reply_text('请续命1s')

def too_young_too_simple(bot, update):
    global total_seconds
    update.message.reply_text(
        '{}为长者续了一秒，目前一共{}秒'.format(update.message.from_user.first_name, total_seconds))
    total_seconds += 1

if __name__ == '__main__':
    global total_seconds
    total_seconds = 0
    updater = Updater(get_token())

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('too_young_too_simple', too_young_too_simple))

    updater.start_polling()
    updater.idle()
