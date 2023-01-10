from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menupower = ReplyKeyboardMarkup(
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
             KeyboardButton(text='Kompyuter savodxoligi kursiga qaytish👈'),
            #  KeyboardButton(text='Oldinga'),
        ],
    ],
    resize_keyboard=True,
)