import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8691307767:AAFxev34srMY3m8DnNkYXyI4zsOwRFw5uEk"

songs = [
    "Imagine Dragons – Believer",
    "The Weeknd – Blinding Lights",
    "Billie Eilish – Bad Guy",
    "Ed Sheeran – Shape of You",
    "Dua Lipa – Levitating"
]

keyboard = [
    ["Випадкова пісня"],
    ["Топ музика"],
    ["Плейлист"]
]

markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт. Я музичний бот. Обери кнопку:",
        reply_markup=markup
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Команди бота:\n"
        "/start — запуск бота\n"
        "/help — список команд\n\n"
        "Кнопки:\n"
        "Випадкова пісня — отримати випадкову пісню\n"
        "Топ музика — популярні пісні\n"
        "Плейлист — рекомендації"
    )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text == "Випадкова пісня":
        song = random.choice(songs)
        await update.message.reply_text(f"Ось пісня:\n{song}")

    elif text == "Топ музика":
        await update.message.reply_text(
            "Топ пісні:\n"
            "1. The Weeknd – Blinding Lights\n"
            "2. Dua Lipa – Levitating\n"
            "3. Ed Sheeran – Shape of You"
        )

    elif text == "Плейлист":
        await update.message.reply_text(
            "Плейлист дня:\n"
            "• Imagine Dragons – Believer\n"
            "• Billie Eilish – Bad Guy\n"
            "• The Weeknd – Starboy"
        )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

print("Бот запущений")
app.run_polling()