from telebot import types


keyboard_hide = types.ReplyKeyboardRemove()


def reg_kb():
    keybd = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Начать")
    keybd.add(btn1)
    return keybd


def after_reg_kb():
    keybd = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("Да")
    btn2 = types.KeyboardButton("Нет")
    keybd.add(btn1, btn2)
    return keybd


def switch_fem_kb():
    keybd = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("М")
    btn2 = types.KeyboardButton("Ж")
    btn3 = types.KeyboardButton("Перезапуск")
    keybd.add(btn1, btn2, btn3)
    return keybd


def restart_kb():
    keybd = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Перезапуск")
    keybd.add(btn1)
    return keybd

def after_reg_kb_if_yes():
    keybd = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("/start_browsing_profiles")
    keybd.add(btn1)
    return keybd

def default():
    keybd = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("/start")
    keybd.add(btn1)
    return keybd
