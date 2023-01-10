from operator import eq
from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,Message
from loader import dp , bot
from aiogram.dispatcher import FSMContext
from states.course import Course
from keyboards.default.menyuKeyboard import menu 
from keyboards.default.mobilKeyboard import menumobil 
from keyboards.default.flutterKeyboard import menuflutter

@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer('Kurslardan birini tanlang', reply_markup=menu)

@dp.message_handler( text ='Mobil Dasturlash ✅')
async def show_menu(message: Message):
    await message.answer('Mavzulardan birini tanlang', reply_markup= menumobil)

@dp.message_handler( text ='Flutter ✅', state = None)
async def show_menu(message: Message):
    await message.answer('Mavzulardan birini tanlang', reply_markup= menuflutter)
    await Course.flutter.set()


@dp.message_handler( text ='1-dars💻', state=Course.flutter)
async def send_lesson_1(message: Message, state:FSMContext):
    await message.answer('1-dars💻:https://youtu.be/zbczUq2v7uc?list=PLQWSb1rBptoKpgX7NZiROg18wtB3Utwg5')

@dp.message_handler( text ='2-dars💻', state=Course.flutter)
async def send_lesson_2(message: Message, state:FSMContext):
    await message.answer('2-dars💻:https://youtu.be/F1Oo2uSwCFY?list=PLQWSb1rBptoKpgX7NZiROg18wtB3Utwg5 ')

@dp.message_handler( text ='3-dars💻', state=Course.flutter)
async def send_lesson_3(message: Message, state:FSMContext):
    await message.answer('3-dars💻:https://youtu.be/_E18lU-8a0g?list=PLQWSb1rBptoKpgX7NZiROg18wtB3Utwg5 ')

@dp.message_handler( text ='4-dars💻', state=Course.flutter)
async def send_lesson_4(message: Message, state:FSMContext):
    await message.answer('4-dars💻:https://youtu.be/jIjEIDpJoNY?list=PLQWSb1rBptoKpgX7NZiROg18wtB3Utwg5')

@dp.message_handler( text ='5-dars💻', state=Course.flutter)
async def send_lesson_5(message: Message, state:FSMContext):
    await message.answer('5-dars💻:https://youtu.be/5PWoMmDo5ds?list=PLQWSb1rBptoKpgX7NZiROg18wtB3Utwg5')

@dp.message_handler( text ='6-dars💻', state=Course.flutter)
async def send_lesson_6(message: Message, state:FSMContext):
    await message.answer('6-dars💻:https://youtu.be/nQXqRP8UMVs?list=PLQWSb1rBptoKpgX7NZiROg18wtB3Utwg5')

@dp.message_handler( text ='7-dars💻', state=Course.flutter)
async def send_lesson_7(message: Message, state:FSMContext):
    await message.answer('7-dars💻:https://youtu.be/LbSOD5_rQN0?list=PLQWSb1rBptoKpgX7NZiROg18wtB3Utwg5')

@dp.message_handler( text ='8-dars💻', state=Course.flutter)
async def send_lesson_8(message: Message, state:FSMContext):
    await message.answer('8-dars💻:https://youtu.be/cQr9EBFBJxQ?list=PLQWSb1rBptoKpgX7NZiROg18wtB3Utwg5 ')

@dp.message_handler( text ='9-dars💻', state=Course.flutter)
async def send_lesson_9(message: Message, state:FSMContext):
    await message.answer('9-dars💻:https://youtu.be/Lxw9qq_vsn8?list=PLQWSb1rBptoKpgX7NZiROg18wtB3Utwg5')

@dp.message_handler( text ='10-dars💻', state=Course.flutter)
async def send_lesson_10(message: Message, state:FSMContext):
    await message.answer('10-dars💻:https://youtu.be/rwLWzMeUF_I?list=PLQWSb1rBptoKpgX7NZiROg18wtB3Utwg5')

@dp.message_handler( text ='Mobil dasturlash kursiga qaytish👈', state=Course.flutter)
async def show_menu(message: Message, state:FSMContext):
    await message.answer('Kurslardan birini tanlang', reply_markup=menumobil)
    await state.finish()