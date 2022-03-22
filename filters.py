from config import *
from aiogram.dispatcher.filters import Filter
from aiogram import types
from data import admins_id


class IsSet(Filter):
    """Фильтр для проверки, запущен ли бот на обработку опозданий
    (запущен, когда получил имя листа). """
    key = "is_set"

    async def check(self, message: types.Message):
        if bot_var.sheet_id:
            return True
        return False


class IsAdmin(Filter):
    """Фильтр для проверки, является ли юзер, запускающий/останавливающий бота, администратором."""
    key = "is_admin"

    async def check(self, message: types.Message):
        return message.from_user.id in admins_id


class IsGroup(Filter):
    """Фильтр для проверки типа канала, откуда поступает сообщение."""
    key = "is_group"

    async def check(self, message: types.Message):
        return message.chat.type != 'private'
