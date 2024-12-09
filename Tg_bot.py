mport asyncio
from aiogram import Bot,Dispatcher,types
from aiogram.filters import Command

Token="7214286086:AAEEV6WybbzsPNeV2mlJcIBDJXhtBEb8eoM"
channel_username="@nilu2131"

bot=Bot(token=Token)
dp=Dispatcher()

user_data={}

@dp.message()
async def proccess_input(message:types.Message):
    user_id=message.from_user.id
    if user_id not in user_data:
        await start(message)
    elif 'name' not in user_data[user_id]:
        await name(message)
    elif 'phone' not in user_data[user_id]:
        await phone(message)
    elif 'age' not in user_data[user_id]:
        await age(message)

    elif message.text=='Zayavka qoldirish':
        await start(message)

@dp.message(Command ("start"))
async def start(message:types.Message):
    user_id=message.from_user.id
    user_data[user_id]={}
    await message.answer("Assalomu akleykum!\nIltimos ismingizni kiriting:")

async def name(message:types.Message):
    user_id=message.from_user.id
    user_data[user_id]['name']=message.text
    button=[
        [types.KeyboardButton(text="Raqamni jonatish",request_contact=True)]
    ]
    keyboard=types.ReplyKeyboardMarkup(keyboard=button, one_time_keyboard=True)
    await message.answer("Iltimos telefon raqamingizni jo'nating\n Yoki"
                         "Raqamingizni jo'natish knopkasini bosing.",reply_markup=keyboard)

async def phone(message:types.Message):
        user_id=message.from_from_user.id
        if message.connact:
            user_data[user_id]['phone']=message.contact.phone_number
        else:
            user_data[user_id]['phone'] = message.text
        await message.answer("Iltimos yoshingizni kiriting:")

async def age(message:types.Message):
    user_id = message.from_user.id
    user_data[user_id]['age'] = message.text

    message_text = (f"Ismingiz:{user_data[user_id]['name']}\n"
                 f"Telefon raqami:{user_data[user_id]['phone']}\n"
                  f"Yoshingiz: {user_data[user_id]['age']}")
    button=[
        [types.KeyboardButton(text='Zayavka qoldirish')]
    ]
    keyboard=types.ReplyKeyboardMarkup(keyboard=button, one_time_keyboard=True)
    await message.answer(f"Zayavka qabul qilindi!\n"
                         f"{message_text}", reply_markup=keyboard)
    await bot.send_message(channel_username, message_text)
    del user_data[user_id]

async def main():
       print('The bot is running!')
       await dp.start_polling(bot)

asyncio.run(main())
