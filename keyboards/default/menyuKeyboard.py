from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Backend ✅'),
            KeyboardButton(text='Frontend ✅'),
        ],
        [
            KeyboardButton(text='3D modeling ✅'),
            KeyboardButton(text='Grafik dizayn ✅'),
        ],
        [
            KeyboardButton(text="Kiber Xavfsizlik ✅"),
            KeyboardButton(text="Kompyuter savodxonligi ✅"),
        ],
        [
            KeyboardButton(text="Mobil Dasturlash ✅"),
            KeyboardButton(text="Ma'lumotlar bazasi ✅"),
        ],
        [
             KeyboardButton(text='📍Joylashuv'),
             KeyboardButton(text='📞Telefon'),
        ],
        [
            KeyboardButton(text="🎬Biz haqimizda")
        ],
    ],
    resize_keyboard=True,

)