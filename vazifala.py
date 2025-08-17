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
