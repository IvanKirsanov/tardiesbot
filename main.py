from filters import *
from functions import *
import logging
import googleapiclient.errors
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(filename='app.log', format='%(asctime)s - %(message)s', level=logging.INFO)


@dp.message_handler(IsAdmin(), commands="start")
async def start(message: types.Message):
    if bot_var.spreadsheet_id != '':
        await message.answer("Бот уже запущен")
    else:
        await message.answer("Отправьте ссылку на таблицу опозданий")
        await BotStates.waiting_for_url.set()


@dp.message_handler(state=BotStates.waiting_for_url)
async def get_url(message: types.Message, state: FSMContext):
    try:
        get_sheet_id(message.text)
        get_sheet_name(bot_var.spreadsheet_id, bot_var.sheet_id)
        await message.reply("Бот запущен на обработку опозданий")
        logging.info(f'Bot started by {message.from_user.username}')
        await state.finish()
    except (googleapiclient.errors.HttpError, ValueError):
        await message.answer("Отправьте ссылку на таблицу опозданий")


@dp.message_handler(IsAdmin(), commands="stop")
async def stop(message: types.Message):
    if bot_var.spreadsheet_id == '':
        await message.answer("Бот не был запущен")
    else:
        logging.info(f'Bot stopped by {message.from_user.username}.')
        bot_var.reset_var()
        await message.answer("Бот остановлен")


@dp.message_handler(IsSet(), IsGroup(), regexp=key_words_regexp)
async def grabbing(message: types.Message):
    writing(message.text, searching_empty_cell())
    await message.reply('+')


if __name__ == '__main__':
    dp.bind_filter(IsAdmin)
    dp.bind_filter(IsSet)
    dp.bind_filter(IsGroup)
    executor.start_polling(dp, skip_updates=True)
