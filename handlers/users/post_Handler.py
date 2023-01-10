from operator import eq
from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,Message
from loader import dp , bot
from aiogram.dispatcher import FSMContext
from states.course import Course
from keyboards.default.menyuKeyboard import menu 
from keyboards.default.mbazaKeyboard import menumbaza
from keyboards.default.postKeyboard import menupost

@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer('Kurslardan birini tanlang', reply_markup=menu)

@dp.message_handler( text ="Ma'lumotlar bazasi ✅")
async def show_menu(message: Message):
    await message.answer('Mavzulardan birini tanlang', reply_markup= menumbaza)


@dp.message_handler( text ='PostgreSQL ✅', state = None)
async def show_menu(message: Message):
    await message.answer('Mavzulardan birini tanlang', reply_markup= menupost)
    await Course.post.set()



@dp.message_handler( text ='1-dars💻', state=Course.post)
async def send_lesson_1(message: Message, state:FSMContext):
    await message.answer('1-dars💻:https://youtu.be/q479qaYVFX4?list=PLcVkxa4hDY3E7o1g3_6GqplbovBPIXnXI')

@dp.message_handler( text ='2-dars💻', state=Course.post)
async def send_lesson_2(message: Message, state:FSMContext):
    await message.answer('2-dars💻:https://youtu.be/5UYgZbZvHwA?list=PLcVkxa4hDY3E7o1g3_6GqplbovBPIXnXI ')

@dp.message_handler( text ='3-dars💻', state=Course.post)
async def send_lesson_3(message: Message, state:FSMContext):
    await message.answer('3-dars💻:https://youtu.be/ee5DAnPNUu8?list=PLcVkxa4hDY3E7o1g3_6GqplbovBPIXnXI ')

@dp.message_handler( text ='4-dars💻', state=Course.post)
async def send_lesson_4(message: Message, state:FSMContext):
    await message.answer('4-dars💻:https://youtu.be/_qkBq1lY_IA?list=PLcVkxa4hDY3E7o1g3_6GqplbovBPIXnXI')

@dp.message_handler( text ='5-dars💻', state=Course.post)
async def send_lesson_5(message: Message, state:FSMContext):
    await message.answer('5-dars💻:https://youtu.be/PvBGKyvTZaI?list=PLcVkxa4hDY3E7o1g3_6GqplbovBPIXnXI ')

@dp.message_handler( text ='6-dars💻', state=Course.post)
async def send_lesson_6(message: Message, state:FSMContext):
    await message.answer('6-dars💻:https://youtu.be/CBnDam5UJK4?list=PLcVkxa4hDY3E7o1g3_6GqplbovBPIXnXI')

@dp.message_handler( text ='7-dars💻', state=Course.post)
async def send_lesson_7(message: Message, state:FSMContext):
    await message.answer('7-dars💻:https://youtu.be/Gxp2fVQzFyE?list=PLcVkxa4hDY3E7o1g3_6GqplbovBPIXnXI  ')

@dp.message_handler( text ='8-dars💻', state=Course.post)
async def send_lesson_8(message: Message, state:FSMContext):
    await message.answer('8-dars💻:https://youtu.be/ZrCasApcXsg?list=PLcVkxa4hDY3E7o1g3_6GqplbovBPIXnXI ')

@dp.message_handler( text ='9-dars💻', state=Course.post)
async def send_lesson_9(message: Message, state:FSMContext):
    await message.answer('9-dars💻:https://youtu.be/MOACxFTTbAM?list=PLcVkxa4hDY3E7o1g3_6GqplbovBPIXnXI')

@dp.message_handler( text ='10-dars💻', state=Course.post)
async def send_lesson_10(message: Message, state:FSMContext):
    await message.answer('10-dars💻:https://youtu.be/6GhxRnjoAqg?list=PLcVkxa4hDY3E7o1g3_6GqplbovBPIXnXI ')

@dp.message_handler( text ="Ma'lumotlar bazasi kursiga qaytish👈", state=Course.post)
async def show_menu(message: Message, state:FSMContext):
    await message.answer('Kurslardan birini tanlang', reply_markup= menumbaza)
    await state.finish()