





# Импорты сторонних модулей

import re
import os.path
import random
import vk_api
import sqlite3
import time
import wikipedia
import requests
import io
from bs4 import BeautifulSoup
import json
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import date, datetime

from wikipedia import exceptions
wikipedia.set_lang("RU")




# Функции
# Создадим функцию для ответа на сообщения в лс группы

def blasthack(id, text, random_id=0, keyboard=None, attachment=None):
    bh.method('messages.send', {'user_id' : id, 'message' : text, 'attachment': attachment, 'random_id': random_id, 'keyboard': keyboard})

# Создание кнопки
def get_but(text, color):
    return {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"" + "1" + "\"}",
                    "label": f"{text}"
                },
                "color": f"{color}"
            }

# Создфние кнопки с гиперссылкой
def get_but_link(text, link):
    return {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"" + "1" + "\"}",
                    "label": f"{text}",
                    "link": link
                },  
            }

# Функция для всплывающих окон
def get_but_show(text, color):
    return {
                "action": {
                    "type": "show_snackbar",
                    "payload": "{\"button\": \"" + "1" + "\"}",
                    "label": f"{text}"
                },
                "color": f"{color}"
            }

# Создание клавиатуры
# Цвета клавиатуры: positive-зеленая, negative-красная, primary-синяя
keyboard1 = {
    "one_time" : False,
    "buttons" : [
        [get_but('Картинка', 'positive'), get_but('Магазин', 'primary')],
        [get_but('Вики', 'positive'), get_but('Писюн', 'negative')],
        [get_but('Профиль', 'positive')]
    ]
}
keyboard1 = json.dumps(keyboard1, ensure_ascii = False).encode('utf-8')
keyboard1 = str(keyboard1.decode('utf-8'))

# 2 клавиатура
keyboard2 = {
    "one_time" : False,
    "buttons" : [
        [get_but('+ник', 'positive'), get_but('+фото', 'positive')],
    ],
    "inline": True
}
keyboard2 = json.dumps(keyboard2, ensure_ascii = False).encode('utf-8')
keyboard2 = str(keyboard2.decode('utf-8'))

# 3 клавиатура
keyboard3 = {
    "one_time" : False,
    "buttons" : [
        [get_but('вжмых', 'positive')],
    ],
    "inline": True
}
keyboard3 = json.dumps(keyboard3, ensure_ascii = False).encode('utf-8')
keyboard3 = str(keyboard3.decode('utf-8'))
        


# Геттеры и сеттеры

def get_user(user_id):
    cmd = "SELECT * FROM users WHERE user_id=%d" % user_id
    sql.execute(cmd)
    return sql.fetchone()


def register_new_user(user_id):
    current_date = str(datetime.now().date()).split('-')
    print()
    current_date = ' '.join(current_date)
    cmd = f"INSERT INTO users(user_id, user_image, money, car, waifu, date_regist, penis) VALUES ({user_id}, '', 10000, '', '', '{str(current_date)}', 0)"
    sql.execute(cmd)
    db.commit()


def set_user_image(user_id, user_image):
    cmd = "UPDATE users SET user_image='%s' WHERE user_id=%d" % (user_image, user_id)
    sql.execute(cmd)
    db.commit()


def get_user_image(user_id):
    cmd = "SELECT user_image FROM users WHERE user_id=%d" % user_id
    sql.execute(cmd)
    return sql.fetchone()


def set_date_regist(user_id, user_image):
    cmd = "UPDATE users SET date_regist='%s' WHERE user_id=%d" % (user_image, user_id)
    sql.execute(cmd)
    db.commit()


def get_date_regist(user_id):
    cmd = "SELECT date_regist FROM users WHERE user_id=%d" % user_id
    sql.execute(cmd)
    return sql.fetchone()


def set_nickname(user_id, nickname):
    cmd = "UPDATE users SET nickname='%s' WHERE user_id=%d" % (nickname, user_id)
    sql.execute(cmd)
    db.commit()


def get_nickname(user_id):
    cmd = "SELECT nickname FROM users WHERE user_id=%d" % user_id
    sql.execute(cmd)
    return sql.fetchone()


def set_money(user_id, money):
    cmd = "UPDATE users SET money=%d WHERE user_id=%d" % (money, user_id)
    sql.execute(cmd)
    db.commit()


def append_money(user_id, money):
    set_money(get_money(user_id) + money)    


def get_money(user_id):
    cmd = "SELECT money FROM users WHERE user_id=%d" % user_id
    sql.execute(cmd)
    return sql.fetchone()


def set_car(user_id, car):
    cmd = "UPDATE users SET car='%s' WHERE user_id=%d" % (car, user_id)
    sql.execute(cmd)
    db.commit()


def get_car(user_id):
    cmd = "SELECT car FROM users WHERE user_id=%d" % user_id
    sql.execute(cmd)
    return sql.fetchone()


def set_penis(user_id):
    penis = get_penis(user_id)[0]
    choise = random.randint(-5, 20)
    if choise < 0:
        blasthack(
                    id=user_id,
                    text=f'Увы ваш писюн упал на {choise} теперь его длина {penis + choise}',
                )
        penis += choise
    elif choise > 0:
        blasthack(
                    id=user_id,
                    text=f'Ваш писюн вырос на {choise} теперь его длина {penis + choise}',
                )
        penis += choise
    cmd = "UPDATE users SET penis=%d WHERE user_id=%d" % (penis, user_id)
    sql.execute(cmd)
    db.commit()

# Проверка, использовался писюн или нет
def check_block_penis(user_id):
    pass


def get_penis(user_id):
    cmd = "SELECT penis FROM users WHERE user_id=%d" % user_id
    sql.execute(cmd)
    return sql.fetchone()


def set_car(user_id, house):
    cmd = "UPDATE users SET house='%s' WHERE user_id=%d" % (house, user_id)
    sql.execute(cmd)
    db.commit()


def get_house(user_id):
    cmd = "SELECT house FROM users WHERE user_id=%d" % user_id
    sql.execute(cmd)
    return sql.fetchone()

# Вывод профиля
def profile(user_id):
    user_image = get_user_image(user_id)    
    nickname = get_nickname(user_id)
    money = get_money(user_id)
    # waifu = get_user_image(user_id)
    car = get_car(user_id)
    # data = get_user_image(user_id)
    penis = get_penis(user_id)
    house = get_house(user_id)
    date_regist = get_date_regist(user_id)
    if house == None:
        house = ('нету')
    print(nickname, money, user_image)
    return (
        f'Ваш профиль:\
        \n&#128526;ник: {nickname[0]}\
        \n&#128176;Деньги: {money[0]}\
        \n&#128663;Машина: {car[0]}\
        \n&#128299;Писюн: {penis[0]}\
        \n&#127968;Дом: {house[0]}\
        \nЗарегестрирован с  {date_regist[0]}',
        user_image[0]
        )





# Основные переменные
# Создаём переменную для удобства в которой хранится наш токен от группы

token = "6bbef6c3ea482ba5a4f7517ccd8491f0e3eb7b9545a32f857d41614e2c69dcaa14f81785216b59a2e9a35" # В ковычки вставляем аккуратно наш ранее взятый из группы токен.

# подключение к БД

filepath = os.path.abspath('db.db')
print(str(filepath))
assert os.path.exists(filepath)
db = sqlite3.connect(filepath)
sql = db.cursor()

# Подключаем токен и longpoll

bh = vk_api.VkApi(token = token)
give = bh.get_api()
longpoll = VkLongPoll(bh)


# Основные сообщения

def check_message(cur_event):

    text = cur_event.text.lower()
    user_id = cur_event.user_id

    if text == 'привет':
                blasthack(
                    id=user_id,
                    text='Привет!',
                )

    elif text == 'профиль':
                user = profile(user_id)
                blasthack(
                    id=user_id,
                    text=user[0],
                    attachment=user[1],
                    keyboard=keyboard2
                )
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                        text = event.text.lower()
                        user_id = event.user_id
                        if text == 'назад':
                            blasthack(
                                id=user_id,
                                text='Вы вернулись в главное меню'
                            )
                            break
                        elif text == '+ник':
                            blasthack(
                                id=user_id,
                                text='Введите ник'
                            )
                            for event in longpoll.listen():
                                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                    text = event.text
                                    user_id = event.user_id
                                    set_nickname(user_id, nickname=text)
                                    blasthack(
                                        id=user_id,
                                        text='Ник установлен'
                                    )
                                    blasthack(
                                        id=user_id,
                                        text='Вы вернулись в главное меню'
                                    )
                                    break
                            break
                        elif text == '+фото':
                            blasthack(
                                        id=user_id,
                                        text='скиньте фото вк в формате (photo-192060952_457241801)'
                                    )
                            for event in longpoll.listen():
                                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                    text = event.text
                                    user_id = event.user_id
                                    set_user_image(user_id, user_image=text)
                                    blasthack(
                                        id=user_id,
                                        text='Фото установлено'
                                    )
                                    blasthack(
                                        id=user_id,
                                        text='Вы вернулись в главное меню',
                                        keyboard=keyboard1
                                    )
                                    break
                            break
                        else:
                            blasthack(
                                        id=user_id,
                                        text='Вы вернулись в главное меню',
                                        keyboard=keyboard1
                                    )
                            break

    elif text == 'писюн':
        set_penis(user_id)

    elif text == 'помощь' or text == 'help':
        blasthack(
                    id=user_id,
                    text='Вот список команд\n1)Вики \n2)Писюн \n3)Картинка \n4) Профиль \n5) Магазин \n6) Группа \n7) Картинка',
                    keyboard=keyboard1
                )
    
    elif text == 'магазин':
        blasthack(
                    id=user_id,
                    text='пока не доступна',
                    keyboard=keyboard1
                )
    
    elif text == 'картинка':
        blasthack(
                    id=user_id,
                    text='Доступно: Вжмых, ЧБ',
                    keyboard=keyboard3
                )
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                text = event.text
                user_id = event.user_id
                if text == 'вжмых':
                    blasthack(
                            id=user_id,
                            text='Кидай пикчу!',
                    )
                    for event in longpoll.listen():
                        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                            text = event.text
                            user_id = event.user_id
                            if text == 'назад':
                                blasthack(
                                    id=user_id,
                                    text='Вы вернулись в главное меню',
                                    keyboard=keyboard1
                                )
                                break
                            attachment = event.attachments
                            response = bh.http.get(f'https://m.vk.com/{attachment}', allow_redirects=False)
                            

                            a = bh.method("photos.getMessagesUploadServer")
                            b = requests.post(a['upload_url'], files={'photo': open('file.jpg', 'rb')}).json()
                            c = bh.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
                            attachment = "photo{}_{}".format(c["owner_id"], c["id"])
                else:
                    blasthack(
                            id=user_id,
                            text='Вы вернулись в главное меню',
                            keyboard=keyboard1
                        )
                    break

    elif text == 'Википедия' or text == 'Вики' or text == 'википедия' or text == 'вики' or text == 'Wikipedia' or text == 'wikipedia' or text == 'Wiki' or text == 'wiki': #если нам пришло сообщение с текстом Википедия или Вики или ... или wiki
                blasthack(
                    id=user_id,
                    text='Введите запрос' #Пишем "Введите запрос"
	                )
                if text != 'назад':
                    for event in longpoll.listen():
                        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text: #Пинаем longpoll
                            if event.from_user:
                                try:
                                    blasthack( #Если написали в ЛС
                                        id=user_id,
                                        text='Вот что я нашёл: \n' + str(wikipedia.summary(event.text)) #Пишем "Вот что я нашёл" И то что вернёт нам api Wikipedia по запросу текста сообщения
                                    )
                                except wikipedia.exceptions.DisambiguationError:
                                        blasthack( 
                                            id=user_id,
                                            text='Слишком много вариантов ответа, не могу выбрать... Задайте белее точный вопрос'
                                        ) 
                                break #выходим из цикла
    else:
        blasthack( 
        id=user_id,
        text='Я не знаю такой команды...',
        keyboard=keyboard1
        ) 
        
            

# Основной код
# Слушаем longpoll(Сообщения)
while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:

            if get_user(event.user_id) is None:
                register_new_user(event.user_id)
                blasthack(
                    id=event.user_id,
                    text='Вы зарегистрировались успешно. Для просмотра команд чекайте help/помощь \nВот список команд\n1) Вики \n2) Писюн \n3) Картинка \n4) Профиль \n5) Магазин \n6) Группа',
                    keyboard=keyboard1
                )
            check_message(event)
