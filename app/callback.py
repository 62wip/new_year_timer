from typing import Any
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Filter, Command

from app.handlers import data_chat_id
from app.tools import update_data_json

router = Router()

@router.callback_query(lambda call: call.data.startswith('on_notification_'))
async def on_notification_callback(callback: CallbackQuery):
    if callback.data == f'on_notification_{callback.from_user.id}':
        await update_data_json(data_chat_id[callback.from_user.id], True)
        await callback.message.edit_text('✅ <b>Уведомления включены!</b>\n\n🌃 <i>Вы будете получать сообщения каждый день в полночь</i> 🔔', parse_mode="HTML")

@router.callback_query(lambda call: call.data.startswith('off_notification_'))
async def on_notification_callback(callback: CallbackQuery):
    if callback.data == f'off_notification_{callback.from_user.id}':
        await update_data_json(data_chat_id[callback.from_user.id], False)
        await callback.message.edit_text('🔕 <b>Уведомления выключены</b>\n\n<i>Вы больше не будете получать сообщения в полночь</i> 🌙', parse_mode="HTML")
