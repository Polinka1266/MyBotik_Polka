import asyncio
import random
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

API_TOKEN = "8691307767:AAFxev34srMY3m8DnNkYXyI4zsOwRFw5uEk"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# список анекдотів
jokes = [
    "Програміст заходить у бар. Замовляє 1 пиво, 10 пива, 100 пива. Потім 0 пива. Потім -1 пиво. Бармен каже: тестування пройдено.",

    "Викладач питає студента: чому ваша програма не працює? Студент: вона працює, просто результат не той, що ви очікували.",

    "Системний адміністратор — це людина, яку кличуть коли щось не працює, і звинувачують коли все працює повільно.",

    "— Чому програмісти плутають Хелловін і Різдво?\n— Бо OCT 31 = DEC 25.",

    "Програміст каже лікарю: у мене проблема зі сном. Лікар: яка саме? Програміст: не можу закрити всі відкриті вкладки."
]

# історія анекдотів
history_text = """
Анекдоти існують сотні років. Спочатку це були короткі дотепні історії,
які передавались усно. У XIX–XX столітті анекдоти стали популярними
в літературі, газетах та театральних виступах.

У Радянському Союзі анекдоти часто використовувались як спосіб
сатири на політику і суспільство. Люди розповідали їх на кухнях,
у компаніях друзів та колег.

Сьогодні анекдоти поширюються через інтернет, соціальні мережі
та відеоплатформи.
"""

# представники гумору
comedians = """
Відомі представники гумору:

Аркадій Райкін — радянський актор і сатирик.
Михайло Жванецький — письменник і майстер іронічної сатири.
Роман Карцев — комедійний актор.
Джим Керрі — актор комедійного жанру.
"""


# /start
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Вітаю. Я бот про анекдоти.\n"
        "Напишіть /help щоб побачити команди."
    )


# /help
@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "Команди:\n"
        "/start — запуск\n"
        "/help — список команд\n"
        "/joke — випадковий анекдот\n"
        "/history — історія анекдотів\n"
        "/comedians — відомі гумористи\n"
        "/bye — завершити"
    )


# випадковий анекдот
@dp.message(Command("joke"))
async def joke_command(message: Message):
    joke = random.choice(jokes)
    await message.answer(joke)


# історія
@dp.message(Command("history"))
async def history_command(message: Message):
    await message.answer(history_text)


# гумористи
@dp.message(Command("comedians"))
async def comedians_command(message: Message):
    await message.answer(comedians)


# /bye
@dp.message(Command("bye"))
async def bye_command(message: Message):
    await message.answer("До побачення")


# обробка тексту
@dp.message()
async def echo_text(message: Message):
    text = message.text.lower()

    if "анекдот" in text:
        await message.answer(random.choice(jokes))
    elif "історія" in text:
        await message.answer(history_text)
    else:
        await message.answer("Я можу розповісти анекдот. Напишіть /joke")


# запуск
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())