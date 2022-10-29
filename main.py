import config
import telebot
import keyboard_funks as kb

bot = telebot.TeleBot(token=config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    # #user_name and user_id will need to be entered into the database
    config.temporary_storage_of_received_data[message.from_user.id] = {'user_id': message.from_user.id}
    
    if config.temporary_storage_of_received_data[message.from_user.id]["user_id"] != message.from_user.id:   #Здесь будет проверка наличия анкеты у пользователя
        bot.send_message(message.chat.id, "Хотите перейти к просмотру анкет? (command - /start_browsing_profiles)", reply_markup=kb.after_reg_kb())
    else:   #добавляем user_id, user_name в бд
        config.temporary_storage_of_received_data[message.from_user.id]["user_name"] = str("@" + message.from_user.username)    
        #    ...
        #     И переходим к регистрации, добавляя вводимые данные в бд
        start = bot.send_message(message.chat.id, "Создадим анкету (отправьте что угодно, чтобы начать)", reply_markup=kb.reg_kb())
        bot.register_next_step_handler(start, reg)

def reg(message):
    
    fem = bot.send_message(message.chat.id, "Выберите пол: М/Ж", 
        reply_markup=kb.switch_fem_kb())
    bot.register_next_step_handler(fem, femile)
def femile(message):
    
    #проверка на выход из функции и нан тайп
    try:
        if message.text.lower() == "начать" or message.text.lower() == "перезапуск" or message.text.lower() == "/start":
            restart = bot.send_message(message.chat.id, "Начнем?", reply_markup=kb.reg_kb())
            bot.register_next_step_handler(restart, reg)
            # bot.clear_step_handler(message)
            # 
    
        elif message.text.lower() == 'м' or message.text.lower() == 'ж':
            #save fem db
            config.temporary_storage_of_received_data[message.from_user.id]['fem'] = message.text
            photo_reqest = bot.send_message(message.chat.id, "Отправьте свое фото", 
                reply_markup=kb.restart_kb())
            bot.register_next_step_handler(photo_reqest, photo)
        else:
            restart = bot.send_message(message.chat.id, 
            'Вы ввели неизвестный пол, введите свой пол снова', 
            reply_markup=kb.switch_fem_kb())
            bot.register_next_step_handler(restart, femile)
    except TypeError:
        pass


def photo(message):
    try:
        if message.text.lower() == "перезапуск" or message.text.lower() == "/start":
            restart = bot.send_message(message.chat.id, "Начнем?", reply_markup=kb.reg_kb())
            bot.register_next_step_handler(restart, reg)
        else:
            restart_req = bot.send_message(message.chat.id, "Похоже, вы ввели не фото. Введите фото: ", 
            reply_markup=kb.restart_kb())
            bot.register_next_step_handler(restart_req, photo)
    except AttributeError:
        try:
            if message.photo[-1].file_id:
                config.temporary_storage_of_received_data[message.from_user.id]["img_path"] = message.photo[-1].file_id        
                
                name_reqwest = bot.send_message(message.chat.id, "Введите свое имя: ")
                
                
                bot.register_next_step_handler(name_reqwest, name)
            else:
                pass
        except TypeError:
            restart_req = bot.send_message(message.chat.id, "Похоже, вы ввели не фото. Введите фото: ", reply_markup=kb.reg_kb())
            bot.register_next_step_handler(restart_req, photo)        


def name(message):
    try:
        if message.text.lower() == "начать" or message.text.lower() == "перезапуск" or message.text.lower() == "/start":
            restart = bot.send_message(message.chat.id, "Начнем?", reply_markup=kb.reg_kb())
            bot.register_next_step_handler(restart, reg)
        else:
            #save name in DB
            config.temporary_storage_of_received_data[message.from_user.id]['name'] = message.text
            
            #Позже переедет в др блок
            bot.send_message(message.chat.id, 
                f"Вот ваша анкета:\n{config.temporary_storage_of_received_data[message.from_user.id]['name']}, {config.temporary_storage_of_received_data[message.from_user.id]['fem']}", 
                )
            bot.send_photo(message.chat.id,
                config.temporary_storage_of_received_data[message.from_user.id]['img_path'])
            total_req = bot.send_message(message.chat.id, "Нравится?", reply_markup=kb.after_reg_kb()) #Bot send total anket and req. "Do u like it?"
            bot.register_next_step_handler(total_req, total)
    except TypeError and AttributeError:
        restart = bot.send_message(message.chat.id, "Вы ввели неверный тип", reply_markup=kb.restart_kb())
        bot.register_next_step_handler(restart, name)





def total(message):
    try:
        if message.text.lower() == "да":
            bot.send_message(message.chat.id, 
                "Хотите перейти к просмотру анкет? (command - /start_browsing_profiles)", 
                reply_markup=kb.after_reg_kb_if_yes())
        elif message.text.lower() == "нет":
            "Этот код замени...."
            restart = bot.send_message(message.chat.id, 
                "Создадим анкету (отправьте что угодно, чтобы начать)", 
                reply_markup=kb.reg_kb())
            bot.register_next_step_handler(restart, reg)
            "Этот код замени...."
        else:
            bot.send_message(message.chat.id, "?", reply_markup=kb.reg_kb())
            bot.send_message(message.chat.id, 
                "Хотите перейти к просмотру анкет? (command - /start_browsing_profiles)", 
                reply_markup=kb.after_reg_kb_if_yes())
            
    except Exception as ex:
        bot.send_message(message.chat.id, ex, reply_markup=kb.reg_kb())


@bot.message_handler(commands=["start_browsing_profiles"])
def browsing_profiles(message):
    #if message.from_user.id in
    bot.send_message(message.chat.id, "None", reply_markup=kb.default())
    pass 



bot.polling(none_stop=True, interval=1)

