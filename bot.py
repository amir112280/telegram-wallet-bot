from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import os

# توکن را از متغیر محیطی Railway می‌خوانیم
TOKEN = os.environ.get("8545062307:AAEEzzNvqmP_s7ZMzO2Xah5EsneLEEga-IA")

# دستور /start
def start(update, context):
    keyboard = [
        [InlineKeyboardButton("واریز", callback_data='deposit')],
        [InlineKeyboardButton("برداشت", callback_data='withdraw')],
        [InlineKeyboardButton("پشتیبانی", callback_data='support')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("به ربات خوش آمدید!", reply_markup=reply_markup)

# پاسخ به دکمه‌ها
def button(update, context):
    query = update.callback_query
    query.answer()  # حتماً باید این را بزنیم تا تلگرام مشکلی نگیره
    if query.data == 'deposit':
        query.edit_message_text(text="شما واریز را انتخاب کردید.")
    elif query.data == 'withdraw':
        query.edit_message_text(text="شما برداشت را انتخاب کردید.")
    elif query.data == 'support':
        query.edit_message_text(text="ارتباط با پشتیبانی برقرار شد.")

# راه‌اندازی ربات
updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

updater.start_polling()
updater.idle()
