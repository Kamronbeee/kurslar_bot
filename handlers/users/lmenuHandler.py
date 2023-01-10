from loader import dp
from aiogram import types

@dp.message_handler(text='📍Joylashuv')
async def get_contact(message: types.Message):
       await message.answer_location(latitude="40.994657983152365",
                                      longitude=" 71.6048352815629")
       await message.answer("Bizning lokatsiyamiz")