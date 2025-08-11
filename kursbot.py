# import requests           #https://t.me/ValyutaInfo_bot
# from aiogram import Bot, Dispatcher, Router, F
# from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
# import asyncio
#
# BOT_TOKEN = "7896463575:AAENMaxCvJcU3lJYxQaor_MlrckpOJK6T1Y"
#
# # Bot va dispatcher ob'ektlari
# bot = Bot(token=BOT_TOKEN)
# router = Router()
# dp = Dispatcher()
# dp.include_router(router)
#
# # Foydalanuvchi ma'lumotlarini saqlash
# user_data = {}
#
# # Valyuta kurslarini olish funksiyasi
# def get_currency_rate(currency_code):
#     url = "https://cbu.uz/ru/arkhiv-kursov-valyut/json/"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         for currency in data:
#             if currency["Ccy"] == currency_code.upper():
#                 return currency
#         return None
#     return None
#
# # /start komandasi uchun handler
# @router.message(F.text == "/start")
# async def send_welcome(message: Message):
#     username = message.from_user.username or "Foydalanuvchi"
#     markup = ReplyKeyboardMarkup(keyboard=[
#         [KeyboardButton(text="O'zbek"), KeyboardButton(text="Русский"), KeyboardButton(text="English")]
#     ], resize_keyboard=True)
#
#     user_data[message.from_user.id] = {"language": "uz"}  # Standart til - o'zbek
#
#     await message.answer(
#         f"Salom, @{username}! 😊\nIltimos, tilni tanlang:\nPlease choose your language:\nПожалуйста, выберите язык:",
#         reply_markup=markup
#     )
#
# # Til tanlash uchun handler
# @router.message(F.text.in_(["O'zbek", "Русский", "English"]))
# async def set_language(message: Message):
#     lang_map = {"O'zbek": "uz", "Русский": "ru", "English": "en"}
#     lang = lang_map[message.text]
#     user_data[message.from_user.id]["language"] = lang
#
#     messages = {
#         "uz": "Til muvaffaqiyatli o'zgartirildi! Endi qaysi valyuta kursini bilmoqchisiz?",
#         "ru": "Язык успешно изменён! Какую валюту вы хотите узнать?",
#         "en": "Language successfully changed! Which currency rate would you like to know?"
#     }
#
#     await message.answer(messages[lang])
#
# # Valyuta hisob-kitobi uchun handler
# @router.message(F.text.regexp(r"^\d+\s+[A-Za-z]{3}\s+to\s+[A-Za-z]{3}$"))
# async def convert_currency(message: Message):
#     parts = message.text.split()
#     amount = float(parts[0])
#     from_currency = parts[1].upper()
#     to_currency = parts[3].upper()
#
#     from_rate = get_currency_rate(from_currency)
#     to_rate = get_currency_rate(to_currency)
#
#     if from_rate and to_rate:
#         converted_amount = amount * (float(from_rate['Rate']) / float(to_rate['Rate']))
#         lang = user_data[message.from_user.id]["language"]
#
#         messages = {
#             "uz": f"{amount} {from_currency} ≈ {converted_amount:.2f} {to_currency}",
#             "ru": f"{amount} {from_currency} ≈ {converted_amount:.2f} {to_currency}",
#             "en": f"{amount} {from_currency} ≈ {converted_amount:.2f} {to_currency}"
#         }
#         await message.answer(messages[lang])
#     else:
#         await message.answer("Valyuta kodlari noto'g'ri kiritilgan yoki mavjud emas!")
#
# # Valyuta kodini so'rash uchun handler
# @router.message(F.text.regexp(r"^[A-Za-z]{3}$"))
# async def handle_currency_code(message: Message):
#     currency_code = message.text.strip().upper()
#     currency = get_currency_rate(currency_code)
#     lang = user_data[message.from_user.id]["language"]
#
#     if currency:
#         messages = {
#             "uz": f"💵 {currency['Ccy']} ({currency['CcyNm_UZ']}): {currency['Rate']} so'm",
#             "ru": f"💵 {currency['Ccy']} ({currency['CcyNm_RU']}): {currency['Rate']} сум",
#             "en": f"💵 {currency['Ccy']} ({currency['CcyNm_EN']}): {currency['Rate']} UZS"
#         }
#         await message.answer(messages[lang])
#     else:
#         await message.answer("Valyuta topilmadi. Kodni tekshiring!")
#
# # Asinxron botni ishga tushirish funksiyasi
# async def main():
#     print("Bot ishga tushdi!")
#     await dp.start_polling(bot)
#
# if __name__ == "__main__":
#     asyncio.run(main())