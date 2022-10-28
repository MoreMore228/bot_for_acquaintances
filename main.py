from types import NoneType
import config
import telebot
import keyboard_funks as kb

bot = telebot.TeleBot(token=config.TOKEN)


@bot.message_handler(content_types=["text"])
# def start(message):
#     start = bot.send_message(message.chat.id, "Начнем?", reply_markup=kb.start_kb())
#     bot.register_next_step_handler(start, reg)
def reg(message):
    
    if message.text.lower() == "начать" or message.text.lower() == "перезапуск":

        #user_name and user_id will need to be entered into the database
        config.user_id = message.from_user.id
        #if user_id in bd:
        #   переходим к просмотру анкет
        #else: добавляем user_id, user_name в бд
        config.user_name = str("@" + message.from_user.username)
        #...
        #И переходим к регистрации, добавляя вводимые данные в бд 
        fem = bot.send_message(message.chat.id, "Выберите пол: М/Ж", 
            reply_markup=kb.switch_fem_kb())
        bot.register_next_step_handler(fem, femile)
    

def femile(message):
    
    #проверка на выход из функции и нан тайп
    try:
        if message.text.lower() == "начать" or message.text.lower() == "перезапуск":
            bot.clear_step_handler(message)
            bot.send_message(message.chat.id, "Начнем?", reply_markup=kb.reg_kb())
    
        elif message.text.lower() == 'м' or message.text.lower() == 'ж':
            #save fem db
            config.fem_for_save = message.text
            nam = bot.send_message(message.chat.id, "Введите свое имя: ", 
                reply_markup=kb.restart_kb())
            bot.register_next_step_handler(nam, name)
    except TypeError:
        bot.send_message(message.chat.id, 
            'Вы ввели неизвестный пол, перезапустите создание профиля', 
            reply_markup=kb.reg_kb())

def name(message):
    try:
        if message.text.lower() == "начать" or message.text.lower() == "перезапуск":
            bot.clear_step_handler(message)
            bot.send_message(message.chat.id, "Начнем?", reply_markup=kb.reg_kb())
        else:
            #save name in DB
            config.name_for_save = message.text
            
            photo_reqest = bot.send_message(message.chat.id, "Отправьте свое фото", 
                reply_markup=kb.restart_kb())
            bot.register_next_step_handler(photo_reqest, photo)
    except TypeError:
        bot.send_message(message.chat.id, "Ошибка")
        bot.clear_step_handler(message)
        bot.send_message(message.chat.id, "Начнем снова?", reply_markup=kb.start_kb())


def photo(message):
    try:
        if not isinstance(message.text, NoneType):
            if message.text.lower() == "перезапуск":
                bot.clear_step_handler(message)
                bot.send_message(message.chat.id, "Начнем?", reply_markup=kb.reg_kb())
        if message.photo[-1].file_id:
            config.id_photo = message.photo[-1].file_id        
            print_total = bot.send_message(message.chat.id, "Показать вашу анкету?", 
                reply_markup=kb.after_reg_kb())
            bot.register_next_step_handler(print_total, total)
    except TypeError:
        bot.send_message(message.chat.id, "Похоже, вы ввели не фото", reply_markup=kb.reg_kb())
        bot.clear_step_handler(message)
        bot.send_message(message.chat.id, "Начнем снова?", reply_markup=kb.reg_kb())        


def total(message):
    try:
        if message.text.lower() == "да":
            bot.send_message(message.chat.id, 
                f"Вот ваша анкета:\n{config.name_for_save}, {config.fem_for_save}", 
                reply_markup=kb.reg_kb())
            bot.send_photo(message.chat.id, config.id_photo)
        elif message.text.lower() == "нет":
            "Этот код замени...."
            bot.clear_step_handler(message)
            bot.send_message(message.chat.id, "Начнем?", reply_markup=kb.reg_kb())
            "Этот код замени...."
        elif message.text.lower() == "перезапуск":
            bot.clear_step_handler(message)
            bot.send_message(message.chat.id, "Создадим анкету снова", reply_markup=kb.reg_kb())
        else:
            bot.send_message(message.chat.id, "?", reply_markup=kb.reg_kb())
            
    except Exception as ex:
        bot.send_message(message.chat.id, ex, reply_markup=kb.reg_kb())

bot.polling(none_stop=True, interval=0)

