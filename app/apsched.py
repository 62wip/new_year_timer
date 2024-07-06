from datetime import datetime, timedelta

from aiogram import Router, Bot
from aiogram.types import Message
import aioschedule
import asyncio

from config import TG_ID, TZ
import app.tools as tools


async def send_day_to_new_year(bot: Bot):
    now_time = datetime.now(TZ)
    time_to_newyear = tools.time_to_newyear(now_time)
    if now_time.month == 12 or now_time.month == 1:
        if now_time.day == 1 and now_time.month == 12:
            answer_text = f'''<b>Вот и первый день зимы</b>
<b>Через <u>31 день</u> наступит долгожданный праздник</b>
<i>С наступающим</i> 🧊❄️⛸️'''
        elif now_time.day == 9 and now_time.month == 12:
            answer_text = f'С НГ'
        else:
            answer_text = f'<b>Уххх, новый год все ближе и ближе ❄️\n{tools.text_stay_to(time_to_newyear + timedelta(days=1))} <u>{time_to_newyear.days + 1} {tools.text_day_to(time_to_newyear + timedelta(days=1))}</u></b>'
        for i in await tools.chat_id_for_mail():
            try:
                await bot.send_message(i, answer_text, parse_mode="HTML")
            except:
                continue

async def scheduler(bot: Bot):
    aioschedule.every().day.at('00:00').do(send_day_to_new_year, bot=bot)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(10)