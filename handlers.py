from start_bot import bot, dp
from aiogram import types, Dispatcher

from config import CHANNELS_ID

async def start(message: types.Message):
    start_markup = types.InlineKeyboardMarkup()
    user_id_btn = types.InlineKeyboardButton('Отправить ID', callback_data='user_id')
    start_markup.row(user_id_btn)
    await message.answer("Боту нужен твой ID", reply_markup=start_markup)

async def user_id_inline_callback(callback_query: types.CallbackQuery):
    global user_id
    user_id = callback_query.from_user.id
    await menu(user_id)

async def menu(user_id):
    menu_markup = make_buttons()
    await bot.send_message(chat_id=user_id, text='Список каналов', reply_markup=menu_markup)

async def make_buttons():
    menu = types.InlineKeyboardMarkup(row_width=len(CHANNELS_ID))
    i = 1
    for channel in CHANNELS_ID:
        btn_name = 'Channel ' + str(i)
        link = bot.create_chat_invite_link(channel)
        btn = types.InlineKeyboardButton(btn_name, link)
        menu.add(btn)
        i += 1
    await menu

async def check_subscribe(message: types.Message):
    for channel_id in CHANNELS_ID:
        bot.get_chat_member(channel_id, user_id)

async def go_to_channel():
    pass

async def link():
    pass

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(check_subscribe, commands=['check'])
    dp.register_callback_query_handler(user_id_inline_callback, text='user_id')