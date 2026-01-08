from datetime import datetime, timedelta

from typing import Any
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Filter, Command

import app.keyboards as kb
import app.tools as tools
from app.jsons import *
from config import TG_ID, TZ


router = Router()
data_chat_id = {}

@router.message(Command('start'))
async def start_command(message: Message) -> None:
    await tools.check_data_json(message.chat.id)
    now_time = datetime.now(TZ)
    if now_time.month == 12:
        answer_text = f'''🎄 <b>Приветствую тебя, <u>{message.from_user.first_name}</u>!</b> ❄️

✨ До Нового года остались <b>считанные дни</b>! 🎊

━━━━━━━━━━━━━━━━
📱 <i>Используй команду</i> <code>/timer</code>
<i>чтобы узнать точное время</i> ⏰

🎁 <b>С наступающим Новым годом!</b> 🎉'''
    else:
        time_to_newyear = tools.time_to_newyear(now_time)
        answer_text = f'''⏳ <b>До Нового года еще</b> <u>{time_to_newyear.days + 1} {tools.text_day_to(time_to_newyear + timedelta(1))}</u> 🎅🏻

━━━━━━━━━━━━━━━━
🗓 <i>Приходи в декабре!</i>
<b>Увидимся, {message.from_user.first_name}!</b> 👋'''
    await message.reply(answer_text, parse_mode="HTML")

@router.message(Command('timer'))
async def timer_command(message: Message) -> None:
    await tools.check_data_json(message.chat.id)
    now_time = datetime.now(TZ)
    time_to_newyear = tools.time_to_newyear(now_time)
    if now_time.month == 12:
        answer_text = f'''🎆 <b>Новый год наступит через:</b>

⏰ <u>{time_to_newyear.days} {tools.text_day_to(time_to_newyear)} {time_to_newyear.seconds // 3600} {tools.text_hour_to(time_to_newyear)} {time_to_newyear.seconds%3600//60} {tools.text_min_to(time_to_newyear)} {time_to_newyear.seconds%3600%60} {tools.text_sec_to(time_to_newyear)}</u> 🥳

━━━━━━━━━━━━━━━━
🎁 <b>С наступающим, {message.from_user.first_name}!</b> 💝'''
    elif now_time.month == 11:
        answer_text = f'''🎆 <b>Новый год наступит через:</b>

⏰ <u>{time_to_newyear.days} {tools.text_day_to(time_to_newyear)} {time_to_newyear.seconds // 3600} {tools.text_hour_to(time_to_newyear)}</u> 🥳

━━━━━━━━━━━━━━━━
✨ <i>Подожди малость, и наступит праздник!</i> 💝'''
    else:
        answer_text = f'''⏳ <b>Новый год наступит через:</b>

📅 <u>{time_to_newyear.days + 1} {tools.text_day_to(time_to_newyear + timedelta(1))}</u>

━━━━━━━━━━━━━━━━
🗓 <i>Еще много времени впереди!</i> ⏰'''
    await message.reply(answer_text, parse_mode="HTML")

@router.message(Command('notification'))
async def notification_command(message: Message) -> None:
    await tools.check_data_json(message.chat.id)
    await message.reply('🔔 <b>Настройка уведомлений</b>\n\n<i>Включить или выключить</i> <u>уведомления в 00:00</u>? 🌌', parse_mode="HTML", reply_markup=await kb.set_notification_func(message.from_user.id))
    data_chat_id[message.from_user.id] = message.chat.id
