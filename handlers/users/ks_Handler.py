from operator import eq
from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,Message
from loader import dp , bot
from aiogram.dispatcher import FSMContext
from states.course import Course
from keyboards.default.menyuKeyboard import menu 
from keyboards.default.komsKeyboard import menukoms 
from keyboards.default.ksKeyboard import menuks

@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer('Kurslardan birini tanlang', reply_markup=menu)

@dp.message_handler( text ='Kompyuter savodxonligi ✅')
async def show_menu(message: Message):
    await message.answer("Yo'nalishlardan birini tanlang", reply_markup= menukoms)

@dp.message_handler( text ='Word ✅')
async def show_menu(message: Message):
    await message.answer('Mavzulardan birini tanlang', reply_markup= menuks )


@dp.message_handler( text ='1-dars')
async def send_lesson_1(message: Message):
    await message.answer('1-dars:https://t.me/SARIQ_DEV_PYTHON/2')

@dp.message_handler( text ='2-dars')
async def send_lesson_2(message: Message):
    await message.answer('2-dars:https://t.me/SARIQ_DEV_PYTHON/3 ')

@dp.message_handler( text ='3-dars')
async def send_lesson_3(message: Message):
    await message.answer('3-dars:https://t.me/SARIQ_DEV_PYTHON/4 ')

@dp.message_handler( text ='4-dars')
async def send_lesson_4(message: Message):
    await message.answer('4-dars:https://t.me/SARIQ_DEV_PYTHON/5')

@dp.message_handler( text ='5-dars')
async def send_lesson_5(message: Message):
    await message.answer('5-dars:https://t.me/SARIQ_DEV_PYTHON/6 ')

@dp.message_handler( text ='6-dars')
async def send_lesson_6(message: Message):
    await message.answer('6-dars:https://t.me/SARIQ_DEV_PYTHON/7 ')

@dp.message_handler( text ='7-dars')
async def send_lesson_7(message: Message):
    await message.answer('7-dars:https://t.me/SARIQ_DEV_PYTHON/8 ')

@dp.message_handler( text ='8-dars')
async def send_lesson_8(message: Message):
    await message.answer('8-dars:https://t.me/SARIQ_DEV_PYTHON/9 ')

@dp.message_handler( text ='9-dars')
async def send_lesson_9(message: Message):
    await message.answer('9-dars:https://t.me/SARIQ_DEV_PYTHON/10 ')

@dp.message_handler( text ='10-dars')
async def send_lesson_10(message: Message):
    await message.answer('10-dars:https://t.me/SARIQ_DEV_PYTHON/11 ')

@dp.message_handler( text ='11-dars')
async def send_lesson_11(message: Message):
    await message.answer('11-dars:https://t.me/SARIQ_DEV_PYTHON/12 ')

@dp.message_handler( text ='12-dars')
async def send_lesson_12(message: Message):
    await message.answer('12-dars:https://t.me/SARIQ_DEV_PYTHON/13 ')



@dp.message_handler( text ='Kompyuter savodxoligi kursiga qaytish👈')
async def show_menu(message: Message):
    await message.answer('Kurslardan birini tanlang', reply_markup=menukoms)