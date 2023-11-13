#!/bin/env python

import os
from dotenv import load_dotenv
from utils.logger import logger
from telegram import Update, constants as TG_CONSTANTS
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler

from repository.LiteStorage import LiteStorage
from Data.storage import Storage

load_dotenv() # Load App-wide environment variables. No need to call it anywhere again
storage: Storage
logger = logger("bot")

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error(f"Exception while handling an upate in chat {update.effective_chat.id}: " + str(context.error))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type == TG_CONSTANTS.ChatType.GROUP:
        storage.saveGroup(update.effective_chat.id, update.effective_chat.title)
    else: # Is a user
        try:
            storage.saveUser(update.effective_user.id, update.effective_user.username)
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello")
        except Exception:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello again!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type == TG_CONSTANTS.ChatType.CHANNEL:
            storage.saveChannel(update.effective_chat.id, update.effective_chat.title)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Chat ID: %s\nResponse: %s" % (str(update.effective_chat.id), update.effective_message.text))

if __name__ == '__main__':
    storage = LiteStorage()
    
    application = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo, block=False))

    application.add_error_handler(error_handler)
    application.run_polling()
