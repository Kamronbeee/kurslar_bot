import asyncio

from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot

from pprint import pprint

@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    number = db.count_users()
    info = f"Bazada {number[0]} ta foydalanuvchi bor"
    # await message.answer(users)
    await message.answer(info)



@dp.message_handler(text="/reklama")
async def send_ad_to_all(message: types.Message):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text="Reklamalar uchun @karimjanofff ga yozing!")
        await asyncio.sleep(0.05)



@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_user(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")


