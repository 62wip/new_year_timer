from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def set_notification_func(user_id: int):
    set_notification_kb = [
        [InlineKeyboardButton(text='Включить', callback_data=f'on_notification_{user_id}'),
        InlineKeyboardButton(text='Выключить', callback_data=f'off_notification_{user_id}')]
    ]
    set_notification = InlineKeyboardMarkup(
        inline_keyboard=set_notification_kb
    )
    return set_notification
