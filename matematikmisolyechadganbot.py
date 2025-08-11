#from aiogram import Bot, Dispatcher
# from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
# from aiogram.filters import Command
# import asyncio
# import random
#
# # Bot tokeningizni kiriting
# API_TOKEN = "8140375208:AAE-AcdR8nBYjvOAsAj6WUL4ZxByLONxEaM"
#
# # Bot va Dispatcher obyektlarini yaratish
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher()
#
# # Foydalanuvchi o‘yin holatini saqlash uchun
# games = {}
#
# # Tugmachalar
# keyboard = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="Misolni yechish")],
#         [KeyboardButton(text="❓ Qoidalar"), KeyboardButton(text="🔙 Chiqish")]
#     ],
#     resize_keyboard=True
# )
#
# # "/start" komandasi uchun handler
# @dp.message(Command("start"))
# async def start_command(message: Message):
#     await message.answer(
#         "Salom! Keling, matematik misollarni yechamiz!\nQuyidagi tugmalardan birini tanlang:",
#         reply_markup=keyboard
#     )
#
# # "Misolni yechish" tugmasi uchun handler
# @dp.message(lambda msg: msg.text == "Misolni yechish")
# async def give_problem(message: Message):
#     # Tasodifiy ikkita son yaratish
#     num1 = random.randint(1, 10)
#     num2 = random.randint(1, 10)
#     operator = random.choice(["+", "-", "*"])  # Tasodifiy operator tanlash
#
#     # Misol yaratish va saqlash
#     games[message.from_user.id] = (num1, num2, operator)
#     problem_text = f"{num1} {operator} {num2}"
#     await message.answer(f"Misolni yeching: {problem_text}")
#
# # Foydalanuvchining javoblarini qabul qilish
# @dp.message(lambda msg: msg.text.isdigit())
# async def check_answer(message: Message):
#     user_id = message.from_user.id
#
#     if user_id not in games:
#         await message.answer("Avval \"Misolni yechish\" tugmasini bosib o‘yin boshlang.")
#         return
#
#     # Saqlangan misolni olish
#     num1, num2, operator = games[user_id]
#     correct_answer = eval(f"{num1} {operator} {num2}")  # To‘g‘ri javobni hisoblash
#     user_answer = int(message.text)
#
#     if user_answer == correct_answer:
#         await message.answer("Tabriklayman! To‘g‘ri javob!")
#     else:
#         await message.answer(f"Afsuski, noto‘g‘ri. To‘g‘ri javob: {correct_answer}")
#
#     # O‘yin holatini o‘chirish
#     del games[user_id]
#
# # "Qoidalar" tugmasi uchun handler
# @dp.message(lambda msg: msg.text == "❓ Qoidalar")
# async def show_rules(message: Message):
#     await message.answer(
#         "O‘yin qoidalari:\n"
#         "1. Bot sizga matematik misol beradi.\n"
#         "2. Siz javobni yozasiz.\n"
#         "3. To‘g‘ri javob uchun tabrik olasiz, noto‘g‘ri javob uchun to‘g‘ri javob ko‘rsatiladi."
#     )
#
# # "Chiqish" tugmasi uchun handler
# @dp.message(lambda msg: msg.text == "🔙 Chiqish")
# async def exit_game(message: Message):
#     if message.from_user.id in games:
#         del games[message.from_user.id]
#     await message.answer("O‘yindan chiqdingiz. Bosh menyuga qaytdingiz.", reply_markup=keyboard)
#
# # Botni ishga tushirish
# async def main():
#     print("Bot ishga tushdi!")
#     await dp.start_polling(bot)
#
# if __name__ == "__main__":                        "7649947838:AAELaUOckt6ZJvNeXS6TjtQt8ZfgKhmwT7A"
#     asyncio.run(main())
