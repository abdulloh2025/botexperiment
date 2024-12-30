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
########################################################################################################################
import requests
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
import asyncio

# Bot tokenini kiriting
BOT_TOKEN = "7896463575:AAENMaxCvJcU3lJYxQaor_MlrckpOJK6T1Y"

# Bot va dispatcher ob'ektlari
bot = Bot(token=BOT_TOKEN)
router = Router()
dp = Dispatcher()
dp.include_router(router)

# Foydalanuvchi ma'lumotlarini saqlash
user_data = {}

# Valyuta kurslarini olish funksiyasi
def get_currency_rate(currency_code):
    url = "https://cbu.uz/ru/arkhiv-kursov-valyut/json/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for currency in data:
            if currency["Ccy"] == currency_code.upper():
                return currency
        return None
    return None

# /start komandasi uchun handler
@router.message(F.text == "/start")
async def send_welcome(message: Message):
    username = message.from_user.username or "Foydalanuvchi"
    markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="O'zbek"), KeyboardButton(text="Русский"), KeyboardButton(text="English")]
    ], resize_keyboard=True)

    user_data[message.from_user.id] = {"language": "uz"}  # Standart til - o'zbek

    await message.answer(
        f"Salom, @{username}! 😊\nIltimos, tilni tanlang:\nPlease choose your language:\nПожалуйста, выберите язык:",
        reply_markup=markup
    )

# Til tanlash uchun handler
@router.message(F.text.in_(["O'zbek", "Русский", "English"]))
async def set_language(message: Message):
    lang_map = {"O'zbek": "uz", "Русский": "ru", "English": "en"}
    lang = lang_map[message.text]
    user_data[message.from_user.id]["language"] = lang

    messages = {
        "uz": "Til muvaffaqiyatli o'zgartirildi! Endi qaysi valyuta kursini bilmoqchisiz?",
        "ru": "Язык успешно изменён! Какую валюту вы хотите узнать?",
        "en": "Language successfully changed! Which currency rate would you like to know?"
    }

    await message.answer(messages[lang])

# Valyuta hisob-kitobi uchun handler
@router.message(F.text.regexp(r"^\d+\s+[A-Za-z]{3}\s+to\s+[A-Za-z]{3}$"))
async def convert_currency(message: Message):
    parts = message.text.split()
    amount = float(parts[0])
    from_currency = parts[1].upper()
    to_currency = parts[3].upper()

    from_rate = get_currency_rate(from_currency)
    to_rate = get_currency_rate(to_currency)

    if from_rate and to_rate:
        converted_amount = amount * (float(from_rate['Rate']) / float(to_rate['Rate']))
        lang = user_data[message.from_user.id]["language"]

        messages = {
            "uz": f"{amount} {from_currency} ≈ {converted_amount:.2f} {to_currency}",
            "ru": f"{amount} {from_currency} ≈ {converted_amount:.2f} {to_currency}",
            "en": f"{amount} {from_currency} ≈ {converted_amount:.2f} {to_currency}"
        }
        await message.answer(messages[lang])
    else:
        await message.answer("Valyuta kodlari noto'g'ri kiritilgan yoki mavjud emas!")

# Valyuta kodini so'rash uchun handler
@router.message(F.text.regexp(r"^[A-Za-z]{3}$"))
async def handle_currency_code(message: Message):
    currency_code = message.text.strip().upper()
    currency = get_currency_rate(currency_code)
    lang = user_data[message.from_user.id]["language"]

    if currency:
        messages = {
            "uz": f"💵 {currency['Ccy']} ({currency['CcyNm_UZ']}): {currency['Rate']} so'm",
            "ru": f"💵 {currency['Ccy']} ({currency['CcyNm_RU']}): {currency['Rate']} сум",
            "en": f"💵 {currency['Ccy']} ({currency['CcyNm_EN']}): {currency['Rate']} UZS"
        }
        await message.answer(messages[lang])
    else:
        await message.answer("Valyuta topilmadi. Kodni tekshiring!")

# Asinxron botni ishga tushirish funksiyasi
async def main():
    print("Bot ishga tushdi!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())