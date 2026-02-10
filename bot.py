from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
import os

TOKEN = os.environ.get("8545062307:AAEEzzNvqmP_s7ZMzO2Xah5EsneLEEga-IA")

keyboard = [['واریز', 'برداشت', 'پشتیبانی']]
markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=False)

def start(update, context):
    update.message.reply_text('به ربات خوش آمدید!', reply_markup=markup)

def handle_text(update, context):
    text = update.message.text
    if text == 'واریز':
        update.message.reply_text('شما واریز را انتخاب کردید.')
    elif text == 'برداشت':
        update.message.reply_text('شما برداشت را انتخاب کردید.')
    elif text == 'پشتیبانی':
        update.message.reply_text('ارتباط با پشتیبانی برقرار شد.')
    else:
        update.message.reply_text('لطفاً یکی از دکمه‌ها را انتخاب کنید.')

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

updater.start_polling()
updater.idle()
