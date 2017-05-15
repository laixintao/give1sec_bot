# coding: utf-8

from telegram.ext import Updater, CommandHandler

total_seconds = 0

def get_token():
    with open('token.txt') as token_file:
        token = token_file.read()
    return token

def start(bot, update):
    update.message.reply_text('请续命1s')

def too_young_too_simple(bot, update):
    update.message.reply_text(
        '{}为长者续了一秒，目前一共{}秒'.format(update.message.from_user.first_name, total_seconds))

updater = Updater(get_token())

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('too_young_too_simple', too_young_too_simple))

updater.start_polling()
updater.idle()
