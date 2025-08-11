

########################################################################################################################


########################################################################################################################
 ########################################################################################################################
########################################################################################################################

########################################################################################################################

#######################################################################################################################

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
#######################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
####################################################################################################################

# from telegram import Update
# from telegram.ext import Application, CommandHandler, ContextTypes
#
# TOKEN = "7751444752:AAEfmgzmAU8CEDxV5j5ALxx6RaqpjilORH8"
#
#
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """/start buyrug'i kelganda ishga tushadi."""
#     user = update.effective_user
#     await update.message.reply_html(
#         f"Hi! {user.mention_html()} 👋",
#         # reply_markup=ForceReply(selective=True), # Agar foydalanuvchiga javob berishni so'ramoqchi bo'lsangiz
#     )
#
#
# def main() -> None:
#     """Botni ishga tushirish uchun asosiy funksiya."""
#     # Bot obyektini yaratish
#     application = Application.builder().token(TOKEN).build()
#
#     # /start buyrug'ini qabul qiluvchi handler qo'shish
#     application.add_handler(CommandHandler("start", start))
#
#     # Botni doimiy tinglash holatiga o'tkazish
#     application.run_polling(allowed_updates=Update.ALL_TYPES)
#
#
# if __name__ == "__main__":
#     main()




































