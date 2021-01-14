"""
Simple Telegram bot that pushes messages to a client.

# Usage:
Send messages to Telegram client
"""

import logging

from property_scraper import scrape
from telegram.ext import CommandHandler, Updater

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# logger.debug("hallo")


updater = Updater(token='ENTER_TOKEN')
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def scrape_it(update, context):
    scrape()
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


start_handler = CommandHandler('start', start)
scrape_handler = CommandHandler('scrape', scrape_it)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(scrape_handler)

updater.start_polling()


# scrape()
