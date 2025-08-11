# import random
# from aiogram import Bot, Dispatcher
# from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
# from aiogram.filters import Command
# import asyncio
# import random
#
# # Bot tokeningizni kiriting
# API_TOKEN = "7840274266:AAFSkE7NI7JUNk-V0w8In3ZiGE9MCymU3N4"
#
# # Bot va Dispatcher obyektlarini yaratish
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher()
#
# # O'yin holatini saqlash uchun
# games = {}
#
# # Tugmachalar
# keyboard = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="O‘yinni boshlash")],
#         [KeyboardButton(text="❓ Qoidalar"), KeyboardButton(text="🔙 Chiqish")]
#     ],
#     resize_keyboard=True
# )
#
# # "/start" komandasi uchun handler
# @dp.message(Command("start"))
# async def start_command(message: Message):
#     await message.answer(
#         "Salom! Men bilan o‘yin o‘ynashga tayyormisiz?\nQuyidagi tugmalardan birini tanlang:",
#         reply_markup=keyboard
#     )
#
# # "O‘yinni boshlash" uchun handler
# @dp.message(lambda msg: msg.text == "O‘yinni boshlash")
# async def start_game(message: Message):
#     random_number = random.randint(1, 100)  # 1 dan 100 gacha son tanlash
#     games[message.from_user.id] = random_number
#     await message.answer("Men 1 dan 100 gacha bo‘lgan son o‘yladim. Uni topishga harakat qiling!")
#
# # Foydalanuvchining javoblarini qabul qilish
# @dp.message(lambda msg: msg.text.isdigit())
# async def guess_number(message: Message):
#     if message.from_user.id not in games:
#         await message.answer("Avval o‘yin boshlashingiz kerak. \"O‘yinni boshlash\" tugmasini bosing.")
#         return
#
#     guessed_number = int(message.text)
#     actual_number = games[message.from_user.id]
#
#     if guessed_number < actual_number:
#         await message.answer("Men o‘ylagan son kattaroq. Yana urinib ko‘ring!")
#     elif guessed_number > actual_number:
#         await message.answer("Men o‘ylagan son kichikroq. Yana urinib ko‘ring!")
#     else:
#         await message.answer(f"Tabriklayman! To‘g‘ri topdingiz! Men {actual_number} sonini o‘ylagan edim.")
#         del games[message.from_user.id]  # O‘yin yakunlandi
#
# # "Qoidalar" tugmasi uchun handler
# @dp.message(lambda msg: msg.text == "❓ Qoidalar")
# async def show_rules(message: Message):
#     await message.answer(
#         "O‘yinning qoidalari:\n"
#         "1. Bot 1 dan 100 gacha bo‘lgan sonni tanlaydi.\n"
#         "2. Siz ushbu sonni topishga harakat qilasiz.\n"
#         "3. Bot sizga \"kattaroq\" yoki \"kichikroq\"  \"yaqin keldiz\" deb yordam beradi.\n"
#         "4. To‘g‘ri topganingizda g‘olib bo‘lasiz!"
#     )
#
# # "Chiqish" tugmasi uchun handler
# @dp.message(lambda msg: msg.text == "🔙 Chiqish")
# async def exit_game(message: Message):
#     if message.from_user.id in games:
#         del games[message.from_user.id]
#     await message.answer("O‘yindan chiqdingiz. Bosh menyuga qayting.", reply_markup=keyboard)
#
# # Botni ishga tushirish
# async def main():
#     print("Bot ishga tushdi!")
#     await dp.start_polling(bot)
#
# if __name__ == "__main__":
#     asyncio.run(main())
