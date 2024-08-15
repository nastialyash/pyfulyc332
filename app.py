import asyncio
from aiogram import Bot,Dispatcher
from aiogram.filters import CommandStart,Command
from dotenv import find_dotenv,load_dotenv
import os
from aiogram.types import Message

load_dotenv(find_dotenv())
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

@dp.message(CommandStart=['images.jfif'])
async def cmd_start(message: Message):
  await message.answer("This is foto")

@dp.message(Command['foto'])
async def cmd_start(message: Message):
  file = open('images.jfif')
  await message.answer(file,"This is foto")
  
    


async def main():
  await  dp.start_polling(bot)

asyncio.run(main())