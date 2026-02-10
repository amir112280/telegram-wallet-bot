from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import os

TOKEN = os.environ.get("BOT_TOKEN")  # مطمئن شو متغیر BOT_TOKEN درست در Railway ست شده

# وقتی /start زده می‌شود
def start(update, context):
    keyboard = [
        [InlineKeyboardButton("واریز", callback_data='deposit')],
        [InlineKeyboardButton("برداشت", callback_data='withdraw')],
        [InlineKeyboardButton("پشتیبانی", callback_data='support')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("به ربات خوش آمدید!", reply_markup=reply_markup)

# وقتی یکی از دکمه‌ها زده شد
def button(update, context):
    query = update.callback_query
    query.answer()  # باید جواب داده شود
    if query.data == 'deposit':
        query.edit_message_text(text="شما واریز را انتخاب کردید.")
    elif query.data == 'withdraw':
        query.edit_message_text(text="شما برداشت را انتخاب کردید.")
    elif query.data == 'support':
        query.edit_message_text(text="ارتباط با پشتیبانی برقرار شد.")

# اتصال به تلگرام
updater = Updater(8545062307:AAEEzzNvqmP_s7ZMzO2Xah5EsneLEEga-IA)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

# ربات را روشن می‌کنیم
updater.start_polling()
updater.idle()
