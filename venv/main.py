import telebot
from telebot import types
import time
import bs4
import random

def cal_t():
    months_eng = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    months_rus = ['Январь', "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь",
                  "Ноябрь", "Декабрь"]
    days_eng = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    days_rus = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    t = time.ctime()
    td_ind = days_eng.index(t[:3])
    t = t.replace(t[:3], days_rus[td_ind]) #аааа
    tm_ind = months_eng.index(t[3:6])
    t = t.replace(t[3:6], months_rus[tm_ind])
    return t


token = '5863949340:AAF93M7a3FtA4DzUN6RhSBTyK_TvAUunZsg'
bot = telebot.TeleBot(token)  #да блть

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Начало работы бота')
    bot.send_message(message.chat.id, 'Введите /com для просмотра списка комманд')

@bot.message_handler(commands=['com'])
def d(message):
    bot.send_message(message.chat.id,'/start - начало \n /долг - долг Виктора \n /писюн \n /топ')


users = {}

@bot.message_handler(commands=['писюн'])
def penis(message):
    name = message.from_user.username
    s_t = time.time()
    if name in users:
        if round(time.time() - users[name][1]) >= 60*60*24: #играл сегодня или нет
            x = random.randint(-5, 10)
            l = users[name][0] + x
            users[name][0] = l
            if x >= 0:
                bot.send_message(message.chat.id, f'{name}, твій пісюн виріс на {x} см. Тепер його довжина {l} см')
            else:
                if l < 0:
                    while l < 0:
                        x = random.randint(-5, 10)
                        l = users[name][0] + x
                bot.send_message(message.chat.id, f'{name}, твій пісюн зменшився на {abs(x)} см. Тепер його довжина {l} см')
        else:
            bot.send_message(message.chat.id, f'{name}, ти сьогодні вже грав')
    else:
        x = random.randint(1, 10)
        users.setdefault(name, []).append(x)
        users[name].append(s_t) #доб времени прироста
        bot.send_message(message.chat.id, f'{name} ты в игре, твой кок целых {users[name][0]} см')


@bot.message_handler(commands=['топ'])
def top(message):
    c = 0
    for i in users:
        c += 1
        bot.send_message(message.chat.id, f'{c}. {i} -  {users[i][0]} cm')



@bot.message_handler(commands=['долг'])
def dolg(message):
    t = cal_t()
    bot.send_message(message.chat.id, f'На сегодняшний день, {t} \n Виктор должен: \n Марку - 1000 руб, Олегу - 1000 руб, Глебу - 1000 руб, Стёпе - 200 руб, Ярику - пачку чапмана с яблоком, а также взять подик в школу')



bot.infinity_polling()()