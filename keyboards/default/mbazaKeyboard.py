from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menumbaza = ReplyKeyboardMarkup(
    keyboard=[
            [   
                KeyboardButton(text='MySQL ✅'),
                KeyboardButton(text='SQLite ✅'),
                KeyboardButton(text='PostgreSQL ✅'),
            
            ],
            [
                KeyboardButton(text= 'Ortga 👈'),
            ],
            
        ],
    resize_keyboard=True,
)