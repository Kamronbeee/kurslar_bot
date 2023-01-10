from operator import eq
from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,Message
from loader import dp , bot
from keyboards.default.menyuKeyboard import menu  
from keyboards.default.dmenyuKeyboard import menumodeling
from aiogram.dispatcher import FSMContext
from states.course import Course

# @dp.message_handler(Text(equals="Kurslar"))
# async def menu
#asosiy tugmalar uchun
@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer('Kurslardan birini tanlang', reply_markup=menu)

@dp.message_handler( text ='3D modeling ✅' , state=None)
async def show_menu(message: Message):
    await message.answer('Mavzulardan birini tanlang', reply_markup=menumodeling)
    await Course.model3d.set()


@dp.message_handler( text ='1-dars💻', state=Course.model3d)
async def send_lesson_1(message: Message, state:FSMContext):
    await message.answer('1-dars💻:https://youtu.be/UbjbEuIHgQA')

@dp.message_handler( text ='2-dars💻', state=Course.model3d)
async def send_lesson_2(message: Message, state:FSMContext):
    await message.answer('2-dars💻:https://youtu.be/ZA6LCOonsIk')

@dp.message_handler( text ='3-dars💻', state=Course.model3d)
async def send_lesson_3(message: Message, state:FSMContext):
    await message.answer('3-dars💻:https://youtu.be/Mrf1dHrpxcY')

@dp.message_handler( text ='4-dars💻', state=Course.model3d)
async def send_lesson_4(message: Message, state:FSMContext):
    await message.answer('4-dars💻:https://youtu.be/XoDgF-w7LBA')

@dp.message_handler( text ='5-dars💻', state=Course.model3d)
async def send_lesson_5(message: Message, state:FSMContext):
    await message.answer('5-dars💻:https://youtu.be/qEF6VJ_LkEk')

@dp.message_handler( text ='6-dars💻', state=Course.model3d)
async def send_lesson_6(message: Message, state:FSMContext):
    await message.answer('6-dars💻:https://youtu.be/Q1vIoRL4Zck ')

@dp.message_handler( text ='7-dars💻', state=Course.model3d)
async def send_lesson_7(message: Message, state:FSMContext):
    await message.answer('7-dars💻:https://youtu.be/79LA_a2FsxE')

@dp.message_handler( text ='8-dars💻', state=Course.model3d)
async def send_lesson_8(message: Message, state:FSMContext):
    await message.answer('8-dars💻:https://www.youtube.com/watch?v=rsK4S8xFkng')

@dp.message_handler( text ='9-dars💻', state=Course.model3d)
async def send_lesson_9(message: Message, state:FSMContext):
    await message.answer('9-dars💻:https://www.youtube.com/watch?v=UZUYzRDch14')

@dp.message_handler( text ='10-dars💻', state=Course.model3d)
async def send_lesson_10(message: Message, state:FSMContext):
    await message.answer('10-dars💻:https://www.youtube.com/watch?v=t8CTsaF9BLU')

@dp.message_handler( text ='11-dars💻', state=Course.model3d)
async def send_lesson_11(message: Message, state:FSMContext):
    await message.answer('11-dars💻:https://www.youtube.com/watch?v=T_YBSbRPOa8')

@dp.message_handler( text ='12-dars💻', state=Course.model3d)
async def send_lesson_12(message: Message, state:FSMContext):
    await message.answer('12-dars💻:https://www.youtube.com/watch?v=mCMRtJfGi5Q')

@dp.message_handler( text ='Ortga 👈', state="*")
async def show_menu(message: Message, state:FSMContext):
    await message.answer('Kurslardan birini tanlang', reply_markup=menu )
    await state.finish()