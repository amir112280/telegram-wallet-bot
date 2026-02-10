from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# توکن و ایدی ادمین (اینجا جایگزین کنید)
TOKEN = "8545062307:AAEEzzNvqmP_s7ZMzO2Xah5EsneLEEga-IA"          # <-- اینجا توکن ربات خودت را بگذار
ADMIN_ID =  AMIRROZ0       # <-- اینجا ایدی تلگرام خودت را بگذار

# قیمت ووچرها
prices = {
    "Premium Voucher": {"خرید": 100000, "فروش": 95000},
    "U Voucher": {"خرید": 50000, "فروش": 45000},
    "Hot Voucher": {"خرید": 70000, "فروش": 65000}
}

# منوی اصلی
def main_menu():
    keyboard = [
        [InlineKeyboardButton("💰 خرید ووچر", callback_data="buy")],
        [InlineKeyboardButton("💸 فروش ووچر", callback_data="sell")],
        [InlineKeyboardButton("📜 قیمت‌ها", callback_data="prices")],
        [InlineKeyboardButton("🛠 پشتیبانی", callback_data="support")]
    ]
    return InlineKeyboardMarkup(keyboard)

# دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "🌟 سلام! به ربات رسمی فروش ووچر خوش آمدید! 🌟\n\n"
        "لطفاً یکی از گزینه‌های زیر را انتخاب کنید:"
    )
    await update.message.reply_text(welcome_text, reply_markup=main_menu())

# پاسخ دکمه‌ها
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_name = query.from_user.full_name
    data = query.data

    if data == "prices":
        price_text = "💎 قیمت ووچرها:\n\n"
        for name, price in prices.items():
            price_text += f"{name}: خرید {price['خرید']} | فروش {price['فروش']}\n"
        await query.edit_message_text(price_text, reply_markup=main_menu())

    elif data == "buy":
        keyboard = [[InlineKeyboardButton(name, callback_data=f"buy_{name}")] for name in prices.keys()]
        await query.edit_message_text("💰 خرید ووچر: لطفاً ووچر مورد نظر را انتخاب کنید:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data.startswith("buy_"):
        voucher = data.split("_")[1]
        await query.edit_message_text(f"💰 شما {voucher} را برای خرید انتخاب کردید.\nلطفاً تعداد را وارد کنید یا پرداخت را انجام دهید.", reply_markup=main_menu())

    elif data == "sell":
        await query.edit_message_text("💸 فروش ووچر: لطفاً کد ووچر خود را ارسال کنید.", reply_markup=main_menu())

    elif data == "support":
        await query.edit_message_text("🛠 پیام شما به پشتیبانی ارسال شد.", reply_markup=main_menu())
        await context.bot.send_message(chat_id=ADMIN_ID, text=f"🛠 کاربر {user_name} نیاز به پشتیبانی دارد!")

# ساخت ربات
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler('start', start))
app.add_handler(CallbackQueryHandler(button))

# اجرای ربات
app.run_polling()
