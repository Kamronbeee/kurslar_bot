from loader import dp ,bot
from aiogram import types
from aiogram.dispatcher.filters import Command, Text


@dp.message_handler( text ='🎬Biz haqimizda', state = None)
async def show_menu(message: types.Message):
    filee = "https://t.me/testuchun1_channel/2"
    await message.answer_video(filee , caption="Biz haqimizda")
    
