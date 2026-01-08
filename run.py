from functools import partial

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession

# Импортируем настройки и модули для клавиатур и обработчиков
# import app.keyboards as kb
from app.handlers import router as router_h
from app.callback import router as router_c
from config import *

# Глобальная переменная для хранения планировщика
scheduler = None

async def on_startup(dp: Dispatcher, bot: Bot) -> None:
    global scheduler
    from app.apsched import setup_scheduler
    scheduler = setup_scheduler(bot)

    print("Bot is starting up...")
    print(f"Scheduler started. Next job run time: {scheduler.get_jobs()[0].next_run_time}")

async def on_shutdown(dp: Dispatcher, bot: Bot) -> None:
    global scheduler
    # Останавливаем планировщик при выключении бота
    if scheduler:
        scheduler.shutdown()
    print("Bot is shutting down...")

async def main() -> None:
    # session = AiohttpSession(proxy=PROXY)
    # bot = Bot(token=API_TOKEN, session=session)
    bot = Bot(token=API_TOKEN)
    await bot.delete_webhook(drop_pending_updates=True)
    dp = Dispatcher()
    dp.include_router(router_h)
    dp.include_router(router_c)
    dp.startup.register(partial(on_startup, dp, bot))
    dp.shutdown.register(partial(on_shutdown, dp, bot))
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt or RuntimeError:
        print('Exit successful.')
