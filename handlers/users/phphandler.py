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
from keyboards.default.phpKeyboard import menuPHP


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer('Kurslardan birini tanlang', reply_markup=menu)

@dp.message_handler( text ='Backend ✅')
async def show_menu(message: Message):
    await message.answer('Mavzulardan birini tanlang', reply_markup= menubackend)

@dp.message_handler( text ='PHP ✅', state = None)
async def show_menu(message: Message):
    await message.answer('Mavzulardan birini tanlang', reply_markup= menuPHP)
    await Course.php.set()

@dp.message_handler( text ='1-dars💻', state=Course.php)
async def send_lesson_1(message: Message, state:FSMContext):
    await message.answer('1-dars💻:https://youtu.be/ea4hkwJyEAg?list=PLAd6rofy-H0e1wH8BP1smNyiz9aGWjiFq')

@dp.message_handler( text ='2-dars💻', state=Course.php)
async def send_lesson_2(message: Message, state:FSMContext):
    await message.answer('2-dars💻:https://youtu.be/fsgTJ4heYog?list=PLAd6rofy-H0e1wH8BP1smNyiz9aGWjiFq')

@dp.message_handler( text ='3-dars💻', state=Course.php)
async def send_lesson_3(message: Message, state:FSMContext):
    await message.answer('3-dars💻:https://youtu.be/yDGrdEoXc18?list=PLAd6rofy-H0e1wH8BP1smNyiz9aGWjiFq ')

@dp.message_handler( text ='4-dars💻', state=Course.php)
async def send_lesson_4(message: Message, state:FSMContext):
    await message.answer('4-dars💻:https://youtu.be/l3TVFIifu0U?list=PLAd6rofy-H0e1wH8BP1smNyiz9aGWjiFq')

@dp.message_handler( text ='5-dars💻', state=Course.php)
async def send_lesson_5(message: Message, state:FSMContext):
    await message.answer('5-dars💻:https://youtu.be/h520TDjcLLA?list=PLAd6rofy-H0e1wH8BP1smNyiz9aGWjiFq')

@dp.message_handler( text ='6-dars💻', state=Course.php)
async def send_lesson_6(message: Message, state:FSMContext):
    await message.answer('6-dars💻:https://youtu.be/3qUl73RPd4I?list=PLAd6rofy-H0e1wH8BP1smNyiz9aGWjiFq')

@dp.message_handler( text ='7-dars💻', state=Course.php)
async def send_lesson_7(message: Message, state:FSMContext):
    await message.answer('7-dars💻:https://youtu.be/eoLq7WsoS08?list=PLAd6rofy-H0e1wH8BP1smNyiz9aGWjiFq ')

@dp.message_handler( text ='8-dars💻', state=Course.php)
async def send_lesson_8(message: Message, state:FSMContext):
    await message.answer('8-dars💻:https://youtu.be/Z6MfpgYIpxI?list=PLAd6rofy-H0e1wH8BP1smNyiz9aGWjiFq ')

@dp.message_handler( text ='9-dars💻', state=Course.php)
async def send_lesson_9(message: Message, state:FSMContext):
    await message.answer('9-dars💻:https://youtu.be/UPDtFl2-B40?list=PLAd6rofy-H0e1wH8BP1smNyiz9aGWjiFq ')

@dp.message_handler( text ='10-dars💻', state=Course.php)
async def send_lesson_10(message: Message, state:FSMContext):
    await message.answer('10-dars💻:https://youtu.be/WV63Uxyv7Vk?list=PLAd6rofy-H0e1wH8BP1smNyiz9aGWjiFq ')

@dp.message_handler( text ='11-dars💻', state=Course.php)
async def send_lesson_11(message: Message, state:FSMContext):
    await message.answer('11-dars💻:https://youtu.be/Gra6790BW3g?list=PLAd6rofy-H0e1wH8BP1smNyiz9aGWjiFq')

@dp.message_handler( text ='12-dars💻', state=Course.php)
async def send_lesson_12(message: Message, state:FSMContext):
    await message.answer('12-dars💻:https://youtu.be/o8jcFfEqIUg?list=PLAd6rofy-H0e1wH8BP1smNyiz9aGWjiFq ' )
    
@dp.message_handler( text ='Backend kurslariga qaytish👈', state=Course.php)
async def show_menu(message: Message, state:FSMContext):
    await message.answer('Kurslardan birini tanlang', reply_markup=menubackend)
    await state.finish() 