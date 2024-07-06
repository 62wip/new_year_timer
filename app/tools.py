from datetime import datetime, timedelta
from json import load, dump


from config import TZ
from app.jsons import *

# futere_new_year_date = datetime(datetime.now(TZ).year + 1, 1, 1, 0, 0, 0, 0, TZ)

def time_to_newyear(now_time: datetime) -> timedelta:
    return datetime(datetime.now(TZ).year + 1, 1, 1, 0, 0, 0, 0, TZ) - now_time


def text_day_to(time_to: timedelta) -> str:
    days = time_to.days
    if days % 10 == 1 and days != 11:
        return 'день'
    elif 2 <= days % 10 <= 4 and not(12 <= days <= 14):
        return 'дня'
    else:
        return 'дней'

    return day_to

def text_hour_to(time_to: timedelta) -> str:
    hours = time_to.seconds // 3600
    if hours % 10 == 1 and hours != 11:
        return 'час'
    elif 2 <= hours % 10 <= 4 and not(12 <= hours <= 14):
        return 'часа'
    else:
        return 'часов'

def text_min_to(time_to: timedelta) -> str:
    mins = time_to.seconds % 3600 // 60
    if mins % 10 == 1 and mins != 11:
        return 'минута'
    elif 2 <= mins % 10 <= 4 and not(12 <= mins <= 14):
        return 'минуты'
    else:
        return 'минут'

def text_sec_to(time_to: timedelta) -> str:
    secs = time_to.seconds % 3600 % 60
    if secs % 10 == 1 and secs != 11:
        return'секунда'
    elif 2 <= secs % 10 <= 4 and not(12 <= secs <= 14):
        return'секунды'
    else:
        return 'секунд'

def text_stay_to(time_to: timedelta) -> str:
    days = time_to.days
    if days % 10 == 1 and days != 11:
        return 'Остался'
    else:
        return 'Осталось'

async def check_data_json(chat_id: int) -> None:
    chat_data = load_data()
    chat_data.setdefault(str(chat_id), True)
    dump_data(chat_data)

async def update_data_json(chat_id: int, value: bool) -> None:
    chat_data = load_data()
    chat_data[str(chat_id)] = value
    dump_data(chat_data)

async def chat_id_for_mail() -> list[int]:
    chat_data = load_data()
    result = []
    for key in chat_data:
        if chat_data[key]:
            result.append(key)
    return result
