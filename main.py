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


########################################################################################################################


########################################################################################################################
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
# ########################################################################################################################
#
# from aiogram import Bot, Dispatcher
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
########################################################################################################################
# print("hello-1")
#
# from aiogram import Bot, Dispatcher, types
# from aiogram.types import Message
# from aiogram.filters import Command
# from apscheduler.schedulers.asyncio import AsyncIOScheduler
# from apscheduler.triggers.date import DateTrigger
# import asyncio
# from datetime import datetime, timedelta
#
# # @TezBot202400bot
# # Bot tokeningizni kiriting
# API_TOKEN = "7840274266:AAFSkE7NI7JUNk-V0w8In3ZiGE9MCymU3N4"
#
# # Bot va Dispatcher obyektlarini yaratish
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher()
#
# # Vazifalar ro'yxati
# tasks = []
#
# # Asinxron jadval tuzuvchi
# scheduler = AsyncIOScheduler()
#
# # "/start" komandasi uchun handler
# @dp.message(Command("start"))
# async def start_command(message: Message):
#     await message.answer(
#         "Salom! Vaqtni boshqarish botiga xush kelibsiz! 🕒\n\n"
#         "Mavjud komandalar:\n"
#         "/add - Vazifa qo‘shish\n"
#         "/list - Vazifalarni ko‘rish\n"
#         "/delete - Vazifani o‘chirish\n"
#         "/help - Yordam"
#     )
#
# # "/help" komandasi uchun handler
# @dp.message(Command("help"))
# async def help_command(message: Message):
#     await message.answer(
#         "Komandalar ro‘yxati:\n"
#         "/add - Vazifa qo‘shish. Format: Vazifa nomi va vaqt (HH:MM formatda)\n"
#         "/list - Hozirgi vazifalar ro‘yxati\n"
#         "/delete - Vazifani o‘chirish. Format: Vazifa raqami\n"
#         "/help - Yordam"
#     )
#
# # Vazifa qo‘shish
# @dp.message(Command("add"))
# async def add_task(message: Message):
#     try:
#         args = message.text.split(maxsplit=1)
#         if len(args) < 2:
#             await message.answer("Iltimos, vazifa nomi va vaqtini kiriting (masalan: `Kitob o‘qish 15:30`).")
#             return
#
#         task, time_str = args[1].rsplit(maxsplit=1)
#         task_time = datetime.strptime(time_str, "%H:%M").time()
#         now = datetime.now()
#
#         # Vaqtni to‘liq formatga o‘tkazish
#         task_datetime = datetime.combine(now.date(), task_time)
#         if task_datetime < now:
#             task_datetime += timedelta(days=1)
#
#         # Vazifani jadvalga qo‘shish
#         tasks.append((task, task_datetime))
#         scheduler.add_job(
#             send_reminder,
#             trigger=DateTrigger(run_date=task_datetime),
#             args=(message.chat.id, task)
#         )
#
#         await message.answer(f"Vazifa qo‘shildi: {task} - {task_time.strftime('%H:%M')}.")
#     except Exception as e:
#         await message.answer("Xatolik yuz berdi. Iltimos, to‘g‘ri formatda yozing (masalan: `Kitob o‘qish 15:30`).")
#
# # Vazifalarni ko‘rish
# @dp.message(Command("list"))
# async def list_tasks(message: Message):
#     if not tasks:
#         await message.answer("Hozircha hech qanday vazifa qo‘shilmagan.")
#         return
#
#     task_list = "\n".join(
#         [f"{i + 1}. {task[0]} - {task[1].strftime('%H:%M')}" for i, task in enumerate(tasks)]
#     )
#     await message.answer(f"Hozirgi vazifalar:\n{task_list}")
#
# # Vazifani o‘chirish
# @dp.message(Command("delete"))
# async def delete_task(message: Message):
#     try:
#         args = message.text.split()
#         if len(args) < 2 or not args[1].isdigit():
#             await message.answer("Iltimos, vazifa raqamini kiriting (masalan: `/delete 1`).")
#             return
#
#         task_index = int(args[1]) - 1
#         if task_index < 0 or task_index >= len(tasks):
#             await message.answer("Noto‘g‘ri vazifa raqami.")
#             return
#
#         removed_task = tasks.pop(task_index)
#         await message.answer(f"Vazifa o‘chirildi: {removed_task[0]} - {removed_task[1].strftime('%H:%M')}.")
#     except Exception as e:
#         await message.answer("Xatolik yuz berdi. Iltimos, raqamni to‘g‘ri kiriting.")
#
# # Eslatma yuborish
# async def send_reminder(chat_id: int, task: str):
#     await bot.send_message(chat_id, f"⏰ Eslatma: {task}")
#
# # Botni ishga tushirish
# async def main():
#     print("Bot ishga tushdi!")
#     scheduler.start()
#     await dp.start_polling(bot)
#
# if __name__ == "__main__":7968463575:AAENMaxCvJcU3lJYxQaor_MlrckpOJK6T1Y
#     asyncio.run(main())
########################################################################################################################
# import requests
# from aiogram import Bot, Dispatcher, Router, F
# from aiogram.types import Message
# from aiogram.filters import Command
# import asyncio
#
# # Bot tokenini kiriting
# BOT_TOKEN = "7896463575:AAENMaxCvJcU3lJYxQaor_MlrckpOJK6T1Y"
#
# # Bot va router ob'ektlari
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher()
# router = Router()
#
# # Valyuta kurslarini olish funksiyasi
# def get_currency_rate(currency_code):
#     url = "https://cbu.uz/ru/arkhiv-kursov-valyut/json/"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         for currency in data:
#             if currency["Ccy"] == currency_code.upper():
#                 return f"💵 {currency['Ccy']} ({currency['CcyNm_UZ']}): {currency['Rate']} so'm"
#         return "❌ Bunday koddagi valyuta topilmadi. Iltimos, kodni tekshiring."
#     return "⚠️ Valyuta kurslarini olishda xatolik yuz berdi."
#
# # /start komandasi uchun handler
# @router.message(Command(commands=["start"]))
# async def send_welcome(message: Message):
#     username = message.from_user.username or "Foydalanuvchi"
#     await message.answer(
#         f"Salom, @{username}! 😊\n"
#         "Qaysi valyuta kursini bilmoqchisiz? Valyuta kodini kiriting (masalan, USD yoki EUR)."
#     )
#
# # Foydalanuvchi xabarlari uchun handler
# @router.message()
# async def handle_message(message: Message):
#     currency_code = message.text.strip()
#     if len(currency_code) == 3:  # Foydalanuvchi 3 harfli valyuta kodini kiritgan deb hisoblaymiz
#         result = get_currency_rate(currency_code)
#         await message.answer(result)
#     else:
#         await message.answer("❗ Iltimos, valyuta kodini to'g'ri formatda kiriting (masalan, USD).")
#
# # Asinxron botni ishga tushirish funksiyasi
# async def main():
#     print("Bot ishga tushdi!")
#     dp.include_router(router)  # Routerni dispatcherga qo'shish
#     await dp.start_polling(bot)
#
# if __name__ == "__main__":
#     asyncio.run(main())
#######################################################################################################################
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
########################################################################################################################
# import requests        BU NARHI OSIB KAMAYGANINI KORSATADGONI
# from aiogram import Bot, Dispatcher, Router, F
# from aiogram.types import Message
# import asyncio
# import matplotlib.pyplot as plt
# from datetime import datetime, timedelta
# from io import BytesIO
#
# # Bot tokenini to'g'ridan-to'g'ri kodga kiritish
# BOT_TOKEN = "7896463575:AAENMaxCvJcU3lJYxQaor_MlrckpOJK6T1Y"
#
# if not BOT_TOKEN:
#     raise ValueError("BOT_TOKEN kiritilmagan yoki noto'g'ri!")
#
# # Bot va dispatcher ob'ektlari
# bot = Bot(token=BOT_TOKEN)
# router = Router()
# dp = Dispatcher()
# dp.include_router(router)
#
# # Valyuta kurslari API
# BASE_URL = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
#
# # Valyuta kurslarini olish funksiyasi
# def get_currency_rate(currency_code):
#     response = requests.get(BASE_URL)
#     if response.status_code == 200:
#         data = response.json()
#         for currency in data:
#             if currency["Ccy"] == currency_code.upper():
#                 return currency
#     return None
#
# # Tarixiy ma'lumotlarni olish funksiyasi
# def get_historical_rates(currency_code, days=7):
#     today = datetime.now()
#     rates = []
#     dates = []
#
#     for i in range(days):
#         date = today - timedelta(days=i)
#         formatted_date = date.strftime("%Y-%m-%d")
#         url = f"https://cbu.uz/uz/arkhiv-kursov-valyut/json/{formatted_date}/"
#         response = requests.get(url)
#         if response.status_code == 200:
#             data = response.json()
#             for currency in data:
#                 if currency["Ccy"] == currency_code.upper():
#                     rates.append(float(currency["Rate"]))
#                     dates.append(formatted_date)
#                     break
#     rates.reverse()
#     dates.reverse()
#     return dates, rates
#
# # Grafigni yaratish funksiyasi
# def create_graph(dates, rates, currency_code):
#     plt.figure(figsize=(10, 5))
#     plt.plot(dates, rates, marker="o", linestyle="-", color="blue")
#     plt.title(f"{currency_code} valyutasining so'nggi kurslari")
#     plt.xlabel("Sana")
#     plt.ylabel("Kurs (so'm)")
#     plt.grid(True)
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#
#     buffer = BytesIO()
#     plt.savefig(buffer, format="png")
#     plt.close()
#     buffer.seek(0)
#     return buffer
#
# # /start komandasi uchun handler
# @router.message(F.text == "/start")
# async def handle_start(message: Message):
#     await message.answer("Botga xush kelibsiz! Valyuta kurslarini ko'rish uchun /graph USD buyrug'idan foydalaning.")
#
# # /graph komandasi uchun handler
# @router.message(F.text.startswith("/graph"))
# async def handle_graph_request(message: Message):
#     parts = message.text.split()
#     if len(parts) < 2:
#         await message.answer("❗ Iltimos, valyuta kodini kiriting. Masalan: /graph USD")
#         return
#
#     currency_code = parts[1].upper()
#     dates, rates = get_historical_rates(currency_code)
#
#     if rates:
#         graph_buffer = create_graph(dates, rates, currency_code)
#         await message.answer_photo(photo=graph_buffer)
#     else:
#         await message.answer("❌ Valyuta kodi bo'yicha ma'lumot topilmadi yoki noto'g'ri.")
#
# # Asinxron botni ishga tushirish funksiyasi
# async def main():
#     print("Bot ishga tushdi!")
#     await dp.start_polling(bot)
#
# if __name__ == "__main__":
#     asyncio.run(main())

########################################################################################################################
########################################################################################################################
# class TALABA_GURUHI:
#     def __init__(self):
#         self.talabalar = []
#
#     def talaba_qoshish(self, familiya, tugilgan_yili, telefon_nomeri):
#         talaba = {
#             'familiya': familiya.strip(),
#             'tugilgan_yili': tugilgan_yili,
#             'telefon_nomeri': telefon_nomeri
#         }
#         self.talabalar.append(talaba)
#         print(f"{familiya} guruhga qo'shildi.")
#
#     def talaba_izlash(self, key, value):
#         value = value.lower()
#         for talaba in self.talabalar:
#             if talaba[key].lower() == value:
#                 return talaba
#         return None
#
#     def talaba_ochirish(self, familiya):
#         familiya = familiya.lower()
#         for talaba in self.talabalar:
#             if talaba['familiya'].lower() == familiya:
#                 self.talabalar.remove(talaba)
#                 print(f"{talaba['familiya']} guruhdan o'chirildi.")
#                 return
#         print(f"{familiya} topilmadi.")
#
#     def talabalarni_tartiblash(self, key):
#         self.talabalar.sort(key=lambda a: a[key])
#         print(f"Talabalar {key} bo'yicha tartiblandi.")
#
#     def talabalarni_korsatish(self):
#         if not self.talabalar:
#             print("Guruhda hali hech qanday talaba yo'q.")
#         else:
#             for talaba in self.talabalar:
#                 print(talaba)
#
#
#
# guruh = TALABA_GURUHI()
#
# print("Talaba Tizimi")
# while True:
#     print("Ish rejimini tanlang:")
#     print("1. Talabani qo'shish")
#     print("2. Talabani izlash")
#     print("3. Talabalar ro'yxatini tartiblash")
#     print("4. Chiqish (to'xtatish)")
#
#     tanlov = input("Rejimni tanlang (1, 2, 3, 4): ")
#
#     if tanlov == '1':
#         while True:
#             familiya = input("Familiyasini kiriting: ")
#             tugilgan_yili = int(input("Tug‘ilgan yilini kiriting: "))
#             telefon_nomeri = input("Telefon raqamini kiriting: ")
#             guruh.talaba_qoshish(familiya, tugilgan_yili, telefon_nomeri)
#
#             yana = input("Yana talaba qo‘shasizmi? (ha/yo'q): ").lower()
#             if yana != 'ha':
#                 break
#
#     elif tanlov == '2':
#         familiya = input("Izlamoqchi bo'lgan talabaning familiyasini kiriting: ")
#         talaba = guruh.talaba_izlash('familiya', familiya)
#         if talaba:
#             print("Topildi:", talaba)
#             ochirish = input("Bu talabani o'chirmoqchimisiz? (ha/yo'q): ")
#             if ochirish.lower() == 'ha':
#                 guruh.talaba_ochirish(familiya)
#         else:
#             print("Talaba topilmadi.")
#
#     elif tanlov == '3':
#         print("Talabalar royxati tugilgan yil bo'yicha tartiblanmoqda...")
#         guruh.talabalarni_tartiblash('tugilgan_yili')
#         guruh.talabalarni_korsatish()
#
#     elif tanlov == '4':
#         print("Dastur to'xtatildi. Xayr!")
#         break
#
#     else:
#         print("Noto'g'ri tanlov! Iltimos, 1, 2, 3 yoki 4 ni tanlang.")

########################################################################################################################
########################################################################################################################
#
#
# import tkinter as tk
# from tkinter import messagebox
#
# class TALABA_GURUHI:
#     def __init__(self):
#         self.talabalar = []
#
#     def talaba_qoshish(self, familiya, tugilgan_yil, telefon_raqami):
#         talaba = {
#             'familiya': familiya.strip(),
#             'tugilgan_yil': tugilgan_yil,
#             'telefon_raqami': telefon_raqami
#         }
#         self.talabalar.append(talaba)
#
#     def talaba_qidirish(self, kalit, qiymat):
#         qiymat = qiymat.lower()
#         for talaba in self.talabalar:
#             if talaba[kalit].lower() == qiymat:
#                 return talaba
#         return None
#
#     def talaba_ochirish(self, familiya):
#         familiya = familiya.lower()
#         for talaba in self.talabalar:
#             if talaba['familiya'].lower() == familiya:
#                 self.talabalar.remove(talaba)
#                 return True
#         return False
#
#     def talabalarni_tartiblash(self, kalit):
#         self.talabalar.sort(key=lambda t: t[kalit])
#
#     def talabalar_royxati(self):
#         return self.talabalar
#
# # GUI qismi
# guruh = TALABA_GURUHI()
#
# def talaba_qoshish_gui():
#     familiya = kirish_familiya.get()
#     tugilgan_yil = kirish_tugilgan_yil.get()
#     telefon_raqami = kirish_telefon.get()
#
#     if familiya and tugilgan_yil and telefon_raqami:
#         try:
#             guruh.talaba_qoshish(familiya, int(tugilgan_yil), telefon_raqami)
#             messagebox.showinfo("Muvaffaqiyatli", f"{familiya} muvaffaqiyatli qo‘shildi!")
#             kirish_familiya.delete(0, tk.END)
#             kirish_tugilgan_yil.delete(0, tk.END)
#             kirish_telefon.delete(0, tk.END)
#         except ValueError:
#             messagebox.showerror("Xatolik", "Tug‘ilgan yil raqam shaklida bo‘lishi kerak.")
#     else:
#         messagebox.showerror("Xatolik", "Barcha maydonlarni to‘ldiring.")
#
# def talaba_qidirish_gui():
#     familiya = kirish_qidirish.get()
#     if familiya:
#         talaba = guruh.talaba_qidirish('familiya', familiya)
#         if talaba:
#             natija = f"Familiya: {talaba['familiya']}\nTug‘ilgan yili: {talaba['tugilgan_yil']}\nTelefon raqami: {talaba['telefon_raqami']}"
#             messagebox.showinfo("Topildi", natija)
#         else:
#             messagebox.showwarning("Topilmadi", "Bunday talaba topilmadi.")
#     else:
#         messagebox.showerror("Xatolik", "Familiyani kiriting.")
#
# def talaba_ochirish_gui():
#     familiya = kirish_qidirish.get()
#     if familiya:
#         muvaffaqiyat = guruh.talaba_ochirish( familiya)
#         if muvaffaqiyat:
#             messagebox.showinfo("O'chirildi", f"{familiya} guruhdan o‘chirildi.")
#         else:
#             messagebox.showwarning("Topilmadi", "Bunday talaba topilmadi.")
#     else:
#         messagebox.showerror("Xatolik", "Familiyani kiriting.")
#
# def talabalarni_korsatish_gui():
#     guruh.talabalarni_tartiblash('tugilgan_yil')
#     talabalar = guruh.talabalar_royxati()
#     royxat_list.delete(0, tk.END)
#     for talaba in talabalar:
#         royxat_list.insert(tk.END, f"{talaba['familiya']} - {talaba['tugilgan_yil']} - {talaba['telefon_raqami']}")
#
# # Asosiy oynani yaratish
# oyna = tk.Tk()
# oyna.title("Talabalar Guruhi")
# oyna.geometry("500x600")
#
# # Talaba qo‘shish
# tk.Label(oyna, text="Talaba qo‘shish", font=('Times New Roman', 14)).pack(pady=10)
#
# tk.Label(oyna, text="Familiya:").pack()
# kirish_familiya = tk.Entry(oyna)
# kirish_familiya.pack()
#
# tk.Label(oyna, text="Tug‘ilgan yili:").pack()
# kirish_tugilgan_yil = tk.Entry(oyna)
# kirish_tugilgan_yil.pack()
#
# tk.Label(oyna, text="Telefon raqami:").pack()
# kirish_telefon = tk.Entry(oyna)
# kirish_telefon.pack()
#
# tk.Button(oyna, text="Talaba qo‘shish", command=talaba_qoshish_gui).pack(pady=10)
#
# # Talaba izlash va o‘chirish
# tk.Label(oyna, text="Talaba izlash / o‘chirish", font=('Times New Roman', 14)).pack(pady=10)
#
# tk.Label(oyna, text="Familiya:").pack()
# kirish_qidirish = tk.Entry(oyna)
# kirish_qidirish.pack()
#
# tk.Button(oyna, text="Talabani izlash", command=talaba_qidirish_gui).pack(pady=5)
# tk.Button(oyna, text="Talabani o‘chirish", command=talaba_ochirish_gui).pack(pady=5)
#
# # Talabalar ro‘yxatini ko‘rsatish
# tk.Button(oyna, text="Talabalarni ko‘rsatish va tartiblash", command=talabalarni_korsatish_gui).pack(pady=10)
#
# royxat_list = tk.Listbox(oyna, width=60)
# royxat_list.pack(pady=10)
#
# oyna.mainloop()

########################################################################################################################
########################################################################################################################





#burish[i][j] = matrix[i][j] 360 chapka va onga burganda
# [n - j - 1][i] 90 chapka
# [j][n - i - 1] 90 onga
# [n - i - 1][n - j - 1] 180 chapka
# 270 giradus chapka burish 90onga teng
# 270 giradus onga burish 90chapiga teng


#
#
# #
# def matritsani_90_gradus_chapga_burish(matrix):
#     n = len(matrix)
#     burish = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             burish[j][n - i - 1]= matrix[i][j]
#     return burish
#
#
# def chiqarish_matrix(matrix):
#     for qator in matrix:
#         print(qator)
#
# n = int(input("Matritsa o'lchamini kiriting (n): "))
# matrix = []
#
# print("Matritsa elementlarini kiriting:")
# for i in range(n):
#     qator = list(map(int, input(f"{i+1}-qator elementlari: ").split()))
#     matrix.append(qator)
#
# print("Boshlangich matritsa:")
# chiqarish_matrix(matrix)
#
# aylantirilgan_matritsa = matritsani_90_gradus_chapga_burish(matrix)
#
# print("90 ga soat millariga teskari burilgan matritsa:")
# chiqarish_matrix(aylantirilgan_matritsa)
#


########################################################################################################################
########################################################################################################################


# n = int(input("Nechta haqiqiy son kiritasiz?: "))
# koeff = [1]
# if n == 15:
#    for i in range(1,n):
#            yangi = [0] * (len(koeff) + 1)
#            for i in range(len(koeff)):
#                yangi[i] -= koeff[i] * i  # (x - a) qismini ochish: -a * oldingi
#                yangi[i + 1] += koeff[i]  # x * oldingi
#            koeff = yangi
#            print(koeff)
#    print(n)
#
# else:
#     print("15 bolishi kerak chunki sharti shunday korsatilgan")
# #(x - 1)(x - 2)(x - 3)(x- 4)

# # Dastlabki koeffitsiyentlar [1] => bu 1*x^0 ya'ni 1

########################################################################################################################
####################################################################################################################
# #
#
# class _CHIQARISH:
#     def __init__(self, son, uzunlik, kasr_raqamlar):
#         self.son = son
#         self.uzunlik = uzunlik
#         self.kasr_raqamlar = kasr_raqamlar
#
#     def formatla(self, satr):
#         if '.' not in satr:
#             satr += '.'
#
#         butun_qism, kasr_qism = satr.split('.')
#
#         kasr_qism = kasr_qism[:self.kasr_raqamlar]
#         while len(kasr_qism) < self.kasr_raqamlar:
#             kasr_qism += '0'
#
#         natija = butun_qism + '.' + kasr_qism
#
#         if len(natija) < self.uzunlik:
#             bosh_joy = self.uzunlik - len(natija)
#             natija = ' ' * bosh_joy + natija
#         else:
#             natija = natija[:self.uzunlik]
#
#         return natija
#
#     def chiqar(self):
#         satr = f"{self.son:.{self.kasr_raqamlar}f}"
#         formatlangan = self.formatla(satr)
#         print(formatlangan)
#
#
# class IKKILIK_CHIQARISH(_CHIQARISH):
#     def chiqar(self):
#         butun = int(self.son)
#         kasr = self.son - butun
#
#         butun_ikkilik = ''
#         if butun == 0:
#             butun_ikkilik = '0'
#         else:
#             while butun > 0:
#                 butun_ikkilik = str(butun % 2) + butun_ikkilik
#                 butun //= 2
#
#         kasr_ikkilik = ''
#         for _ in range(self.kasr_raqamlar):
#             kasr *= 2
#             raqam = int(kasr)
#             kasr_ikkilik += str(raqam)
#             kasr -= raqam
#
#         satr = butun_ikkilik + '.' + kasr_ikkilik
#         formatlangan = self.formatla(satr)
#         print(formatlangan)
#
#
# class SAKKIZLIK_CHIQARISH(_CHIQARISH):
#     def chiqar(self):
#         butun = int(self.son)
#         kasr = self.son - butun
#
#         butun_sakkizlik = ''
#         if butun == 0:
#             butun_sakkizlik = '0'
#         else:
#             while butun > 0:
#                 butun_sakkizlik = str(butun % 8) + butun_sakkizlik
#                 butun //= 8
#
#         kasr_sakkizlik = ''
#         for _ in range(self.kasr_raqamlar):
#             kasr *= 8
#             raqam = int(kasr)
#             kasr_sakkizlik += str(raqam)
#             kasr -= raqam
#
#         satr = butun_sakkizlik + '.' + kasr_sakkizlik
#         formatlangan = self.formatla(satr)
#         print(formatlangan)
#
#
# class ONOLTI_CHIQARISH(_CHIQARISH):
#     def chiqar(self):
#         butun = int(self.son)
#         kasr = self.son - butun
#
#         belgilar = "0123456789ABCDEF"
#         butun_onolti = ''
#         if butun == 0:
#             butun_onolti = '0'
#         else:
#             while butun > 0:
#                 qoldiq = butun % 16
#                 butun_onolti = belgilar[qoldiq] + butun_onolti
#                 butun //= 16
#
#         kasr_onolti = ''
#         for _ in range(self.kasr_raqamlar):
#             kasr *= 16
#             raqam = int(kasr)
#             kasr_onolti += belgilar[raqam]
#             kasr -= raqam
#
#         satr = butun_onolti + '.' + kasr_onolti
#         formatlangan = self.formatla(satr)
#         print(formatlangan)

#
# print("10lik:")
# _CHIQARISH(3.14, 15, 6).chiqar()
#
# print("2lik:")
# IKKILIK_CHIQARISH(3.14, 15, 6).chiqar()
#
# print("8lik:")
# SAKKIZLIK_CHIQARISH(3.14, 15, 6).chiqar()
#
# print("16lik:")
# ONOLTI_CHIQARISH(3.14, 15, 6).chiqar()


#
# def daraja(x, k, epsilon=0.0001):
#     y = 1
#     while True:
#         y_navbatagi = y + (x / (y ** (k - 1)) - y) / k
#         if abs(y_navbatagi - y) < epsilon:
#             break
#         y = y_navbatagi
#     return y_navbatagi
#
# a = float(input(" qiymatini kiriting: "))
# yuqori = daraja(a, 3) - daraja(a**2 + 1, 6)
# pastki = 1 + daraja(3 + a, 7)
#
# natija = yuqori / pastki
# print(f"Natija: {natija:.6f}")

#
# lst = [1, 2, 3, 4, 0, 3, 4, 2, 1, 6, 6, 0, 1, 2, 3]
#
# # 0 lar turgan indekslarni topamiz
# zero_indices = [i for i, val in enumerate(lst) if val == 0]
#
# # Agar kamida 2 ta 0 bo‘lsa, ular ORASIDAGI + 0 larni ham qo‘shamiz
# if len(zero_indices) >= 2:
#     start = zero_indices[0]       # 0 ni o'zini ham olamiz
#     end = zero_indices[1] + 1     # ikkinchi 0 ni ham olamiz
#     result = sum(lst[start:end])
#     print("Yig'indisi (0 lar ham qo‘shilgan):", result)
# else:
#     print("Kamida 2 ta nol kerak")


import json
#
# # Oddiy Python dictionary
# data = {
#     "ism": "Ali",
#     "yosh": 25,
#     "talaba": True,
#     "fanlar": ["Matematika", "Fizika"],
#     "manzil": {
#         "shahar": "Toshkent",
#         "pochta": 100100
#     }
# }
#
# # JSON formatga o‘tkazish (matn ko‘rinishida)
# json_data = json.dumps(data, indent=4, ensure_ascii=False)
# print(json_data)



import json
# 1. JSON faylga yozish
# yangi_foydalanuvchi = {
#     "ismi": "Anvar",
#     "yosh": 21,
#     "status": "talaba"
# }
#
# with open("foydalanuvchilar.json", "w", encoding='utf-8') as f:
#     json.dump(yangi_foydalanuvchi, f, indent=4, ensure_ascii=False)
#
# # 2. JSON fayldan o‘qish
# with open("foydalanuvchilar.json", "r", encoding='utf-8') as f:
#     data = json.load(f)
# print("Fayldan o‘qilgan ma’lumot:", data)
#
# # 3. Ma'lumotni tahrirlash
# data["yosh"] = 22
# print("Tahrirlangan ma’lumot:", data)
#
# # 4. Qayta yozib qo‘yish
# with open("foydalanuvchilar.json", "w", encoding='utf-8') as f:
#     json.dump(data, f, indent=4, ensure_ascii=False)
# print("Yangilangan ma’lumot faylga yozildi.")
#


# import json
#
# # Oddiy Python dictionary
# data = {
#     "ism": "Ali",
#     "yosh": 25,
#     "talaba": True,
#     "fanlar": ["Matematika", "Fizika"],
#     "manzil": {
#         "shahar": "Toshkent",
#         "pochta": 100100
#     }
# }
#
# # JSON formatga o‘tkazish (matn ko‘rinishida)
# json_data = json.dumps(data, indent=4, ensure_ascii=False)
# print(json_data)

#
#
# import json
# import gzip
#
# data = {"ism": "Sardor", "rol": "admin", "parol": "123456"}
#
# with gzip.open("xavfsiz_data.json.gz", "wt", encoding="utf-8") as f:
#     json.dump(data, f, indent=4, ensure_ascii=False)
#
# with gzip.open("xavfsiz_data.json.gz", "rt", encoding="utf-8") as f:
#     yuklangan_malumot = json.load(f)
#     print(yuklangan_malumot)
