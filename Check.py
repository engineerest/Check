import asyncio
import logging
import time
from aiogram.filters.command import Command
from aiogram import types, Dispatcher, Bot, Router

bot_t = Bot(token="6953283417:AAFU5Y0ux3GI7_As8ObhHJzbgQM9p0v0ZJE")
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Здравствуйте, напишите любую чушь или слова, и проверем есть ли одинаковые буквы!")

@dp.message()
async def if_have(message: types.Message):
    try:
        letter = set()

        for symbol in message.text:
            if symbol in letter:
                await message.answer("True")
                break
            else:
                letter.add(symbol)
        else:
            await message.answer("False")

    except Exception as error:
        await message.answer(f"Error: {error}")
        time.sleep(1)

async def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting bot")

    await dp.start_polling(bot_t)

if __name__ == "__main__":
    asyncio.run(main())