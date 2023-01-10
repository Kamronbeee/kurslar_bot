from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menumobil = ReplyKeyboardMarkup(
    keyboard=[
            [   
                KeyboardButton(text='AOS ✅'),
                KeyboardButton(text='Android ✅'),
                KeyboardButton(text='Flutter ✅'),
            
            ],
            [
                KeyboardButton(text= 'Ortga 👈'),
            ],
            
        ],
    resize_keyboard=True,
)