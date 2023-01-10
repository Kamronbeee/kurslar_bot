from operator import eq
from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,Message
from loader import dp , bot
from aiogram.dispatcher import FSMContext
from states.course import Course
from keyboards.default.menyuKeyboard import menu 
from keyboards.default.pmenyuKeyboard  import menuPython
from keyboards.default.backKeyboard import menubackend
from keyboards.default.javaKeyboard import menujava


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer('Kurslardan birini tanlang', reply_markup=menu)

@dp.message_handler( text ='Backend ✅')
async def show_menu(message: Message):
    await message.answer('Mavzulardan birini tanlang', reply_markup= menubackend)

@dp.message_handler( text ='JavaScript ✅', state = None)
async def show_menu(message: Message):
    await message.answer('Mavzulardan birini tanlang', reply_markup= menujava)
    await Course.java.set()


@dp.message_handler( text ='1-dars💻', state=Course.java)
async def send_lesson_1(message: Message):
    await message.answer('1-dars💻:https://youtu.be/L8MHt0be6pI?list=PLPCDJXWqKXKEM3kJgJeo8dD8KK5bT4Cdx')

@dp.message_handler( text ='2-dars💻', state=Course.java)
async def send_lesson_2(message: Message):
    await message.answer('2-dars💻:https://youtu.be/8M4gxlEDJZE?list=PLPCDJXWqKXKEM3kJgJeo8dD8KK5bT4Cdx ')

@dp.message_handler( text ='3-dars💻', state=Course.java)
async def send_lesson_3(message: Message):
    await message.answer('3-dars💻:https://youtu.be/O79-Y_MG9No?list=PLPCDJXWqKXKEM3kJgJeo8dD8KK5bT4Cdx ')

@dp.message_handler( text ='4-dars💻', state=Course.java)
async def send_lesson_4(message: Message):
    await message.answer('4-dars💻:https://youtu.be/o5-GLKmiS0o?list=PLPCDJXWqKXKEM3kJgJeo8dD8KK5bT4Cdx')

@dp.message_handler( text ='5-dars💻', state=Course.java)
async def send_lesson_5(message: Message):
    await message.answer('5-dars💻:https://youtu.be/Iqt3BpdDusI?list=PLPCDJXWqKXKEM3kJgJeo8dD8KK5bT4Cdx ')

@dp.message_handler( text ='6-dars💻', state=Course.java)
async def send_lesson_6(message: Message):
    await message.answer('6-dars💻:https://youtu.be/5ajoiKw90Qs?list=PLPCDJXWqKXKEM3kJgJeo8dD8KK5bT4Cdx ')

@dp.message_handler( text ='7-dars💻', state=Course.java)
async def send_lesson_7(message: Message):
    await message.answer('7-dars💻:https://youtu.be/tVNZp80msG0?list=PLPCDJXWqKXKEM3kJgJeo8dD8KK5bT4Cdx')

@dp.message_handler( text ='8-dars💻', state=Course.java)
async def send_lesson_8(message: Message):
    await message.answer('8-dars💻:https://youtu.be/KcOaXIwI83k?list=PLPCDJXWqKXKEM3kJgJeo8dD8KK5bT4Cdx')

@dp.message_handler( text ='9-dars💻', state=Course.java)
async def send_lesson_9(message: Message):
    await message.answer('9-dars💻:https://youtu.be/PQTCs6on9Xw?list=PLPCDJXWqKXKEM3kJgJeo8dD8KK5bT4Cdx')

@dp.message_handler( text ='10-dars💻', state=Course.java)
async def send_lesson_10(message: Message):
    await message.answer('10-dars💻:https://youtu.be/KlJ1dBCznIY?list=PLPCDJXWqKXKEM3kJgJeo8dD8KK5bT4Cdx')

@dp.message_handler( text ='11-dars💻', state=Course.java)
async def send_lesson_11(message: Message):
    await message.answer('11-dars💻:https://youtu.be/Mwfa0y4C6pI?list=PLPCDJXWqKXKEM3kJgJeo8dD8KK5bT4Cdx')

@dp.message_handler( text ='12-dars💻', state=Course.java)
async def send_lesson_12(message: Message):
    await message.answer('12-dars💻:https://youtu.be/a752NVuGAGE?list=PLPCDJXWqKXKEM3kJgJeo8dD8KK5bT4Cdx ')

@dp.message_handler( text ='Backend kurslariga qaytish👈', state=Course.java)
async def show_menu(message: Message, state=Course.java):
    await message.answer('Kurslardan birini tanlang', reply_markup= menubackend)
    await state.finish()