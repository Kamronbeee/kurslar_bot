from loader import dp
from aiogram import types
# from keyboards.inline.phone import phone


@dp.message_handler(text="📞Telefon")
async def show_menu(message: types.Message):
    await message.answer("UITC o'quv markazining telefon raqami +998-90-690-00-48. Biz bilan bog'laning va taklif va murojaatlaringizni bildiring.")