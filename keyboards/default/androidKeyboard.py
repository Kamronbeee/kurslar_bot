from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuandroid = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1-dars💻'),
            KeyboardButton(text='2-dars💻'),

           
        ],
        [
            KeyboardButton(text='3-dars💻'),
            KeyboardButton(text='4-dars💻'),
        ],
        [
             
            KeyboardButton(text='5-dars💻'),
            KeyboardButton(text='6-dars💻'),

           
        ],
        [
            KeyboardButton(text='7-dars💻'),
            KeyboardButton(text='8-dars💻'),
        ],
        [
             
            KeyboardButton(text='9-dars💻'),
            KeyboardButton(text='10-dars💻'),
        ],
        
        [
             KeyboardButton(text='Mobil dasturlash kursiga qaytish👈'),
            #  KeyboardButton(text='Oldinga'),
        ],
    ],
    resize_keyboard=True,
)