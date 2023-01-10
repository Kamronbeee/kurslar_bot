from operator import eq
from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,Message
from loader import dp , bot
from aiogram.dispatcher import FSMContext
from states.course import Course
from keyboards.default.menyuKeyboard import menu 
from keyboards.default.k_Keyboard import menukiber


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer('Kurslardan birini tanlang', reply_markup=menu)

@dp.message_handler( text ='Kiber Xavfsizlik ✅', state = None)
async def show_menu(message: Message):
    await message.answer('Mavzulardan birini tanlang', reply_markup= menukiber)
    await Course.kiber.set()


@dp.message_handler( text ='1-dars💻', state=Course.kiber)
async def send_lesson_1(message: Message, state:FSMContext):
    await message.answer('1-dars💻:https://youtu.be/hC2UJpxgj5g?list=PLQWSb1rBptoJG9cJ1aRSWRjOgloWeyAe9' )

@dp.message_handler( text ='2-dars💻', state=Course.kiber)
async def send_lesson_2(message: Message, state:FSMContext):
    await message.answer('2-dars💻:https://youtu.be/0OStMi8cDpo?list=PLQWSb1rBptoJG9cJ1aRSWRjOgloWeyAe9')

@dp.message_handler( text ='3-dars💻', state=Course.kiber)
async def send_lesson_3(message: Message, state:FSMContext):
    await message.answer('3-dars💻:https://youtu.be/dw8GS-q7HKM?list=PLQWSb1rBptoJG9cJ1aRSWRjOgloWeyAe9 ')

@dp.message_handler( text ='4-dars💻', state=Course.kiber)
async def send_lesson_4(message: Message, state:FSMContext):
    await message.answer('4-dars💻:https://youtu.be/TSl3HwkNRAY?list=PLQWSb1rBptoJG9cJ1aRSWRjOgloWeyAe9')

@dp.message_handler( text ='5-dars💻', state=Course.kiber)
async def send_lesson_5(message: Message, state:FSMContext):
    await message.answer('5-dars💻:https://youtu.be/B5S93oj4lfM?list=PLQWSb1rBptoJG9cJ1aRSWRjOgloWeyAe9 ')

@dp.message_handler( text ='6-dars💻', state=Course.kiber)
async def send_lesson_6(message: Message, state:FSMContext):
    await message.answer('6-dars💻:https://youtu.be/IX3yy0nvCnc?list=PLQWSb1rBptoJG9cJ1aRSWRjOgloWeyAe9')

@dp.message_handler( text ='7-dars💻', state=Course.kiber)
async def send_lesson_7(message: Message, state:FSMContext):
    await message.answer('7-dars💻:https://youtu.be/tISpdoNrsTs?list=PLQWSb1rBptoJG9cJ1aRSWRjOgloWeyAe9 ')

@dp.message_handler( text ='8-dars💻', state=Course.kiber)
async def send_lesson_8(message: Message, state:FSMContext):
    await message.answer('8-dars💻:https://youtu.be/UvAKzHCENO0?list=PLQWSb1rBptoJG9cJ1aRSWRjOgloWeyAe9 ')

@dp.message_handler( text ='9-dars💻', state=Course.kiber)
async def send_lesson_9(message: Message, state:FSMContext):
    await message.answer('9-dars💻:https://youtu.be/qIcgVMXuFqE?list=PLQWSb1rBptoJG9cJ1aRSWRjOgloWeyAe9')

@dp.message_handler( text ='10-dars💻', state=Course.kiber)
async def send_lesson_10(message: Message, state:FSMContext):
    await message.answer('10-dars💻:https://youtu.be/JVyTnnWgatQ?list=PLQWSb1rBptoJG9cJ1aRSWRjOgloWeyAe9')

@dp.message_handler( text ='11-dars💻', state=Course.kiber)
async def send_lesson_11(message: Message, state:FSMContext):
    await message.answer('11-dars💻:https://youtu.be/HltWH7wOiiQ?list=PLQWSb1rBptoJG9cJ1aRSWRjOgloWeyAe9')

@dp.message_handler( text ='12-dars💻', state=Course.kiber)
async def send_lesson_12(message: Message, state:FSMContext):
    await message.answer('12-dars💻:https://youtu.be/-0X7dFxsXK4?list=PLQWSb1rBptoJG9cJ1aRSWRjOgloWeyAe9')




@dp.message_handler( text ='Ortga 👈', state=Course.kiber)
async def show_menu(message: Message, state:FSMContext):
    await message.answer('Kurslardan birini tanlang', reply_markup=menu)
    await state.finish()