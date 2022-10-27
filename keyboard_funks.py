from telebot import types


def start():
    keybd = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/c")
    btn2 = types.KeyboardButton("/d")
    keybd.add(btn1, btn2)
    return keybd


def if__yeah():
    keybd = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    btn1 = types.KeyboardButton("/b")
    btn2 = types.KeyboardButton("/a")
    keybd.add(btn1, btn2)
    return keybd


def if_no():
    keybd = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    btn1 = types.KeyboardButton("/start")
    btn2 = types.KeyboardButton("/c")
    keybd.add(btn1, btn2)
    return keybd