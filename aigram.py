from aiogram import Bot, Dispatcher, executor,types

bot = Bot('6654201797:AAGL9XKox4I_Qr3Z4WUnh4vmGt7YnQV5Lkw')
dp = Dispatcher(bot)

@dp.message_handler(commands = ['aiogram'])
async def aiogram(message: types.Message):
    await bot.send_message(message.chat.id, 'hello')
    await message.answer('hello2')
    await message.reply('hello3')
    '''file = open('foto','rb')
    await message.answer_audio(file)'''

@dp.message_handler(commands = ['inline'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup(row_width = 2)
    markup.add(types.InlineKeyboardButton('Site', url = 'https://openweathermap.org/current#name'))
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    await message.reply('Hello',reply_markup = markup)

@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)

@dp.message_handler(commands = ['reply'])
async def info(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Site'))
    markup.add(types.KeyboardButton('Website'))
    await message.reply('Reply', reply_markup=markup)


executor.start_polling(dp)