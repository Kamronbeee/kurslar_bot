from operator import eq
from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,Message
from loader import dp , bot
from aiogram.dispatcher import FSMContext
from states.course import Course
from keyboards.default.menyuKeyboard import menu 
from keyboards.default.komsKeyboard import menukoms 
from keyboards.default.exel_Keyboard import menuexel


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer('Kurslardan birini tanlang', reply_markup=menu)

@dp.message_handler( text ='Kompyuter savodxonligi ✅')
async def show_menu(message: Message):
    await message.answer('Mavzulardan birini tanlang', reply_markup= menukoms)

@dp.message_handler( text ='Exel ✅', state = None)
async def show_menu(message: Message):
    await message.answer('Mavzulardan birini tanlang', reply_markup= menuexel)
    await Course.exel.set()

@dp.message_handler( text ='1-dars💻', state=Course.exel)
async def send_lesson_1(message: Message, state:FSMContext):
    await message.answer('1-dars💻:https://youtu.be/0KIw98oFwVs?list=PLBsQ7kvE-3Ui2PxYN8f-kgNV7QA3PsO7V')

@dp.message_handler( text ='2-dars💻', state=Course.exel)
async def send_lesson_2(message: Message, state:FSMContext):
    await message.answer('2-dars💻:https://youtu.be/Av0aumrOTmc?list=PLBsQ7kvE-3Ui2PxYN8f-kgNV7QA3PsO7V ')

@dp.message_handler( text ='3-dars💻', state=Course.exel)
async def send_lesson_3(message: Message, state:FSMContext):
    await message.answer('3-dars💻:https://youtu.be/i6EM91VkjBk?list=PLBsQ7kvE-3Ui2PxYN8f-kgNV7QA3PsO7V')

@dp.message_handler( text ='4-dars💻', state=Course.exel)
async def send_lesson_4(message: Message, state:FSMContext):
    await message.answer('4-dars💻:https://youtu.be/i6EM91VkjBk?list=PLBsQ7kvE-3Ui2PxYN8f-kgNV7QA3PsO7V')

@dp.message_handler( text ='5-dars💻', state=Course.exel)
async def send_lesson_5(message: Message, state:FSMContext):
    await message.answer('5-dars💻:https://youtu.be/sVPP_PcAC1E?list=PLBsQ7kvE-3Ui2PxYN8f-kgNV7QA3PsO7V ')

@dp.message_handler( text ='6-dars💻', state=Course.exel)
async def send_lesson_6(message: Message, state:FSMContext):
    await message.answer('6-dars💻:https://youtu.be/Qn2zOetITng?list=PLBsQ7kvE-3Ui2PxYN8f-kgNV7QA3PsO7V ')

@dp.message_handler( text ='7-dars💻', state=Course.exel)
async def send_lesson_7(message: Message, state:FSMContext):
    await message.answer('7-dars💻:https://youtu.be/-qdNg9Zth1o?list=PLBsQ7kvE-3Ui2PxYN8f-kgNV7QA3PsO7V ')

@dp.message_handler( text ='8-dars💻', state=Course.exel)
async def send_lesson_8(message: Message, state:FSMContext):
    await message.answer('8-dars💻:https://youtu.be/XDVxQTqskBA?list=PLBsQ7kvE-3Ui2PxYN8f-kgNV7QA3PsO7V ')


@dp.message_handler( text ='Kompyuter savodxoligi kursiga qaytish👈', state=Course.exel)
async def show_menu(message: Message, state:FSMContext):
    await message.answer('Kurslardan birini tanlang', reply_markup=menukoms)
    await state.finish()     