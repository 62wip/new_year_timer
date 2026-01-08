from datetime import datetime, timedelta
from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from config import TG_ID, TZ
import app.tools as tools


async def send_day_to_new_year(bot: Bot):
    now_time = datetime.now(TZ)
    time_to_newyear = tools.time_to_newyear(now_time)
    if now_time.month == 12 or now_time.month == 1:
        if now_time.day == 1 and now_time.month == 12:
            answer_text = f'''❄️ <b>Вот и первый день зимы!</b> ⛄️

🎄 Через <u>31 день</u> наступит долгожданный праздник!

━━━━━━━━━━━━━━━━
✨ <i>С наступающим Новым годом!</i> 🎁'''
        elif now_time.day == 1 and now_time.month == 1:
            answer_text = f'''🎆 <b>С НОВЫМ ГОДОМ!</b> 🎆

🎄✨🎁🎉🥳🍾✨🎄

<b>Пусть этот год принесёт счастье, радость и исполнение желаний!</b> 💫'''
        else:
            answer_text = f'''🎄 <b>Новый год всё ближе и ближе!</b> ❄️

⏰ {tools.text_stay_to(time_to_newyear + timedelta(days=1))} <u>{time_to_newyear.days + 1} {tools.text_day_to(time_to_newyear + timedelta(days=1))}</u>

━━━━━━━━━━━━━━━━
✨ <i>Скоро праздник!</i> 🎁'''
        if (now_time.day == 1 and now_time.month == 1) or now_time.month == 12:
            for i in await tools.chat_id_for_mail():
                try:
                    await bot.send_message(i, answer_text, parse_mode="HTML")
                except:
                    continue

def setup_scheduler(bot: Bot):
    scheduler = AsyncIOScheduler(timezone=TZ)
    scheduler.add_job(
        send_day_to_new_year,
        trigger=CronTrigger(hour=21, minute=00),  # каждый день в 00:00
        args=[bot]
    )
    scheduler.start()
    return scheduler
