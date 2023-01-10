from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menubackend = ReplyKeyboardMarkup(
    keyboard=[
            [   
                KeyboardButton(text='Python ✅'),
                KeyboardButton(text='PHP ✅'),
                KeyboardButton(text='JavaScript ✅'),
            
            ],
            [
                KeyboardButton(text= 'Ortga 👈'),
            ],
            
        ],
    resize_keyboard=True,
)