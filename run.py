from functools import partial

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession

# Импортируем настройки и модули для клавиатур и обработчиков
# import app.keyboards as kb
from app.handlers import router as router_h
from app.callback import router as router_c
from app.apsched import scheduler
from config import *

async def on_startup(dp: Dispatcher, bot: Bot) -> None:
    asyncio.create_task(scheduler(bot))
    print("Bot is starting up...")

async def on_shutdown(dp: Dispatcher) -> None:
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
    dp.shutdown.register(partial(on_shutdown, dp))
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt or RuntimeError:
        print('Exit successful.')
