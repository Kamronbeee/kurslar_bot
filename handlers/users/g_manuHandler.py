from operator import eq
from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,Message
from loader import dp , bot
from keyboards.default.menyuKeyboard import menu  
from keyboards.default.gmenyuKeyboard import menugrafik
from aiogram.dispatcher import FSMContext
from states.course import Course

@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer('Kurslardan birini tanlang', reply_markup=menu)

@dp.message_handler( text ='Grafik dizayn ✅', state = None)
async def show_menu(message: Message):

    await message.answer('Mavzulardan birini tanlang', reply_markup=menugrafik)
    await Course.grafik.set()


@dp.message_handler( text ='1-dars💻', state=Course.grafik)
async def send_lesson_1(message: Message, state:FSMContext):
    await message.answer('1-dars💻:https://youtu.be/9Yh25FQgH4k')

@dp.message_handler( text ='2-dars💻', state=Course.grafik)
async def send_lesson_2(message: Message, state:FSMContext):
    await message.answer('2-dars💻:https://youtu.be/LfiFt-eKsUE ')

@dp.message_handler( text ='3-dars💻', state=Course.grafik)
async def send_lesson_3(message: Message, state:FSMContext):
    await message.answer('3-dars💻:https://youtu.be/-SE0L8fEU-8 ')

@dp.message_handler( text ='4-dars💻', state=Course.grafik)
async def send_lesson_4(message: Message, state:FSMContext):
    await message.answer('4-dars💻:https://youtu.be/8Sm_D27gDOs')

@dp.message_handler( text ='5-dars💻', state=Course.grafik)
async def send_lesson_5(message: Message, state:FSMContext):
    await message.answer('5-dars💻:https://youtu.be/cdkqh4xIpBg')

@dp.message_handler( text ='6-dars💻', state=Course.grafik)
async def send_lesson_6(message: Message, state:FSMContext):
    await message.answer('6-dars💻:https://youtu.be/58K704qLaro')

@dp.message_handler( text ='7-dars💻', state=Course.grafik)
async def send_lesson_7(message: Message, state:FSMContext):
    await message.answer('7-dars💻:https://youtu.be/x2Uur1rE3Hg')

@dp.message_handler( text ='8-dars💻', state=Course.grafik)
async def send_lesson_8(message: Message, state:FSMContext):
    await message.answer('8-dars💻:https://youtu.be/F5tyP4xnFH4')

@dp.message_handler( text ='9-dars💻', state=Course.grafik)
async def send_lesson_9(message: Message, state:FSMContext):
    await message.answer('9-dars💻:https://youtu.be/yjGIlYfQhwc')

@dp.message_handler( text ='10-dars💻', state=Course.grafik)
async def send_lesson_10(message: Message, state:FSMContext):
    await message.answer('10-dars💻:https://youtu.be/GIKrLj9wh-A')

@dp.message_handler( text ='11-dars💻', state=Course.grafik)
async def send_lesson_11(message: Message, state:FSMContext):
    await message.answer('11-dars💻:https://youtu.be/JrCsC8adKKM')

@dp.message_handler( text ='12-dars💻', state=Course.grafik)
async def send_lesson_12(message: Message, state:FSMContext):
    await message.answer('12-dars💻:https://youtu.be/lTkRqJNPDyY')


@dp.message_handler( text ='Ortga 👈', state="*")
async def show_menu(message: Message, state:FSMContext):
    await message.answer('Kurslardan birini tanlang', reply_markup=menu )
    await state.finish()