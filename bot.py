from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.environ.get("BOT_TOKEN")

keyboard = [['واریز', 'برداشت', 'پشتیبانی']]
markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=False)

# دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('به ربات خوش آمدید!', reply_markup=markup)

# پاسخ به دکمه‌ها
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == 'واریز':
        await update.message.reply_text('شما واریز را انتخاب کردید.')
    elif text == 'برداشت':
        await update.message.reply_text('شما برداشت را انتخاب کردید.')
    elif text == 'پشتیبانی':
        await update.message.reply_text('ارتباط با پشتیبانی برقرار شد.')
    else:
        await update.message.reply_text('لطفاً یکی از دکمه‌ها را انتخاب کنید.')

# ساخت Application و اضافه کردن هندلرها
app = ApplicationBuilder().token(8545062307:AAEEzzNvqmP_s7ZMzO2Xah5EsneLEEga-IA).build()
app.add_handler(CommandHandler('start', start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

# اجرای ربات
app.run_polling()
