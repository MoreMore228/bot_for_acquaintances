import config
import telebot
import keyboard_funks as kb

bot = telebot.TeleBot(token=config.TOKEN)


@bot.message_handler(commands=["c"])
def start(message):
    bot.send_message(message.chat.id, "Привет!\nХочешь начать знакомиться?", reply_markup=kb.if__yeah())

@bot.message_handler(commands=["d"])
def start(message):
    bot.send_message(message.chat.id, "Привет!\nХочешь начать знакомиться?", reply_to_message_id=message.message_id, reply_markup=kb.if_no())

@bot.message_handler(commands=["a"])
def start(message):
    bot.send_message(message.chat.id, "[eq", reply_to_message_id=message.message_id, reply_markup=kb.start())



bot.polling(none_stop=True, interval=0)

