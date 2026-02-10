from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🟢 واریز", "🔴 برداشت"],
        ["💰 موجودی", "💬 پشتیبانی"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "به ربات خوش آمدید 👇",
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token("8545062307:AAEEzzNvqmP_s7ZMzO2Xah5EsneLEEga-IA").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
