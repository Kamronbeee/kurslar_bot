from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menukoms = ReplyKeyboardMarkup(
    keyboard=[
            [   
                KeyboardButton(text='Word ✅'),               
                KeyboardButton(text='Exel ✅'),
                KeyboardButton(text='PowerPoint ✅'),
            
            ],
            [
                KeyboardButton(text= 'Ortga 👈'),
            ],
            
        ],
    resize_keyboard=True,
)