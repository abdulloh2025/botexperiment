# from aiogram import Bot, Dispatcher
# from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
# from aiogram.filters import Command
# from aiogram import F
#
# import asyncio
#
# # Bot tokeningizni kiriting
# API_TOKEN = "7532759128:AAHRYHqdNs2DjWR-9QBTNOJyiJdNUMBW108"
#
# # Bot va Dispatcher obyektlarini yaratish
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher()
#
# # Tugmachalar yaratish
# keyboard = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="Qoshish"), KeyboardButton(text="Ayirish")],
#         [KeyboardButton(text="Kopaytirish"), KeyboardButton(text="Bolish")]
#     ],
#     resize_keyboard=True
# )
#
# # "/start" komandasi uchun handler
# @dp.message(Command("start"))
# async def start_command(message: Message):
#     await message.answer(
#         "Salom! Men Telegram botman. Quyidagi tugmalardan foydalaning:",
#         reply_markup=keyboard  # Tugmalarni yuboramiz
#     )
#
# # Har qanday matnli xabar uchun handler
# @dp.message(F.text)
# async def handle_buttons(message: Message):
#     if message.text == "Qo‘shish":
#         await message.answer("Ikkita sonni `+` belgisi bilan yuboring (masalan: 12+34).")
#     elif "+" in message.text:  # Foydalanuvchi sonlarni yuborsa
#         try:
#             # Sonlarni ajratish
#             num1, num2 = map(int, message.text.split("+"))
#             result = num1 + num2
#             await message.answer(f"Natija: {num1} + {num2} = {result}")
#         except ValueError:
#             await message.answer("Xatolik! Iltimos, ikkita sonni to‘g‘ri formatda yuboring (masalan: 12+34).")
#
#     if message.text == "Ayirish":
#         await message.answer("Ikkita sonni `-` belgisi bilan yuboring (masalan: 12-34).")
#     elif "-" in message.text:  # Foydalanuvchi sonlarni yuborsa
#         try:
#             # Sonlarni ajratish
#             num1, num2 = map(int, message.text.split("-"))
#             result = num1 - num2
#             await message.answer(f"Natija: {num1} - {num2} = {result}")
#         except ValueError:
#             await message.answer("Xatolik! Iltimos, ikkita sonni to‘g‘ri formatda yuboring (masalan: 12+34).")
#
#
#     if message.text == "Bolish":
#         print("bolishhh")
#         await message.answer("Ikkita sonni `\\` belgisi bilan yuboring (masalan: 12/34).")
#     elif "/" in message.text:  # Foydalanuvchi sonlarni yuborsa
#         try:
#             # Sonlarni ajratish
#             num1, num2 = map(int, message.text.split("/"))
#             result = num1 / num2
#             await message.answer(f"Natija: {num1} / {num2} = {result}")
#         except ValueError:
#             await message.answer("Xatolik! Iltimos, ikkita sonni to‘g‘ri formatda yuboring (masalan: 12/34).")
#
#         print("33")
#     if message.text == "Kopaytirish":
#         print("Kopaytirish")
#         await message.answer("Ikkita sonni `*` belgisi bilan yuboring (masalan: 12*34).")
#     elif "*" in message.text:  # Foydalanuvchi sonlarni yuborsa
#         try:
#            # Sonlarni ajratish
#          num1, num2 = map(int, message.text.split("*"))
#          result = num1 * num2
#          await message.answer(f"Natija: {num1} * {num2} = {result}")
#         except ValueError:
#             await message.answer("Xatolik! Iltimos, ikkita sonni to‘g‘ri formatda yuboring (masalan: 12*34).")
#         print("44")
#         await message.answer("Bosh menyuga qaytdingiz.", reply_markup=keyboard)
#     else:
#         await message.reply(f"Siz yozdingiz: {message.text}")
#
# # Botni ishga tushirish
# async def main():
#     print("Bot ishga tushdi!")
#     await dp.start_polling(bot)
#
# if __name__ == "__main__":
#     asyncio.run(main())
