from aiogram import types
from aiogram.dispatcher import filters
from loader import dp


@dp.message_handler(hashtags="test")
async def  firt_hashtag(msg: types.Message()):
	await msg.answer("Siz botni tekshiryapsiz :)")


@dp.message_handler(hashtags="python")
async def  second_hashtag(msg: types.Message()):
	await msg.answer("pyhton the best programming language")