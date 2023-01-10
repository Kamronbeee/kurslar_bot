from operator import eq
from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,Message
from loader import dp , bot
from keyboards.default.menyuKeyboard import menu  
from keyboards.default.fmenyuKeyboard import menufront
from aiogram.dispatcher import FSMContext
from states.course import Course


@dp.message_handler( text ='Frontend ✅', state = None)
async def show_menu(message: Message):
    await message.answer('Mavzulardan birini tanlang', reply_markup=menufront )
    await Course.frontend.set()

@dp.message_handler( text ='1-dars💻', state=Course.frontend)
async def send_lesson_1(message: Message, state:FSMContext):
    await message.answer('1-dars💻:https://www.youtube.com/watch?v=q8yclECd9CY&list=PLpDyZ4xZcDg8fRiY6xgsQcDiMjNYJhNjE&index=1')

@dp.message_handler( text ='2-dars💻', state=Course.frontend)
async def send_lesson_2(message: Message, state:FSMContext):
    await message.answer('2-dars💻:https://www.youtube.com/watch?v=4aDeGEntGFw&list=PLpDyZ4xZcDg8fRiY6xgsQcDiMjNYJhNjE&index=2 ')

@dp.message_handler( text ='3-dars💻', state=Course.frontend)
async def send_lesson_3(message: Message, state:FSMContext):
    await message.answer('3-dars💻:https://www.youtube.com/watch?v=tuh2r2lTcmE&list=PLpDyZ4xZcDg8fRiY6xgsQcDiMjNYJhNjE&index=3 ')

@dp.message_handler( text ='4-dars💻', state=Course.frontend)
async def send_lesson_4(message: Message, state:FSMContext):
    await message.answer('4-dars💻:https://www.youtube.com/watch?v=0WT9klSJl38&list=PLpDyZ4xZcDg8fRiY6xgsQcDiMjNYJhNjE&index=4')

@dp.message_handler( text ='5-dars💻', state=Course.frontend)
async def send_lesson_5(message: Message, state:FSMContext):
    await message.answer('5-dars💻: https://www.youtube.com/watch?v=mr8yY89SN5c&list=PLpDyZ4xZcDg8fRiY6xgsQcDiMjNYJhNjE&index=5')

@dp.message_handler( text ='6-dars💻', state=Course.frontend)
async def send_lesson_6(message: Message, state:FSMContext):
    await message.answer('6-dars💻:https://www.youtube.com/watch?v=9ORRqb1ahSQ&list=PLpDyZ4xZcDg8fRiY6xgsQcDiMjNYJhNjE&index=6 ')

@dp.message_handler( text ='7-dars💻', state=Course.frontend)
async def send_lesson_7(message: Message, state:FSMContext):
    await message.answer('7-dars💻:https://www.youtube.com/watch?v=yq_wbNtt4jw&list=PLpDyZ4xZcDg8fRiY6xgsQcDiMjNYJhNjE&index=7 ')

@dp.message_handler( text ='8-dars💻', state=Course.frontend)
async def send_lesson_8(message: Message, state:FSMContext):
    await message.answer('8-dars💻:https://www.youtube.com/watch?v=hxdYmh4tp9c&list=PLpDyZ4xZcDg8fRiY6xgsQcDiMjNYJhNjE&index=8 ')

@dp.message_handler( text ='9-dars💻', state=Course.frontend)
async def send_lesson_9(message: Message, state:FSMContext):
    await message.answer('9-dars💻:https://www.youtube.com/watch?v=IryLl-sbQt0&list=PLpDyZ4xZcDg8fRiY6xgsQcDiMjNYJhNjE&index=9')

@dp.message_handler( text ='10-dars💻', state=Course.frontend)
async def send_lesson_10(message: Message, state:FSMContext):
    await message.answer('10-dars💻:https://www.youtube.com/watch?v=ygE5JB2DsFY&list=PLpDyZ4xZcDg8fRiY6xgsQcDiMjNYJhNjE&index=10 ')

@dp.message_handler( text ='11-dars💻', state=Course.frontend)
async def send_lesson_11(message: Message, state:FSMContext):
    await message.answer('11-dars💻:https://www.youtube.com/watch?v=uCYtOcs5BSY&list=PLpDyZ4xZcDg8fRiY6xgsQcDiMjNYJhNjE&index=11')

@dp.message_handler( text ='12-dars💻', state=Course.frontend)
async def send_lesson_12(message: Message, state:FSMContext):
    await message.answer('12-dars💻:https://www.youtube.com/watch?v=_p2ROVQA0wg&list=PLpDyZ4xZcDg8fRiY6xgsQcDiMjNYJhNjE&index=12 ')

@dp.message_handler( text ='Ortga 👈', state=Course.frontend)
async def show_menu(message: Message, state:FSMContext):
    await message.answer('Kurslardan birini tanlang', reply_markup=menu )
    await state.finish()
