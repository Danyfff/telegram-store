from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import register_all_routers


bot = Bot(token=TOKEN)
dp = Dispatcher()

register_all_routers(dp)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())