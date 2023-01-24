import time
import praw  # для парсинга мемов
import vk_api, json
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType  # для прослушки сообщений
from vk_api.utils import get_random_id  # для стабильной работы vk api
import wiki_parcer  # парсит вики страничку
import my_keyboard  # модуль с клавиатурами
from dotenv import load_dotenv  # загрузка информации из .env-файла
import os  # работа с файловой системой
import Name  # файлик с переменными, которые нужно менять, при переносе бота в другую группу
import weather
import requests  # для парсинга мемов

# загрузка токена и id группы из локального виртуального окружения
load_dotenv()
token_for_group = os.getenv("ACCESS_TOKEN_FOR_GROUP")
token_for_user = os.getenv("ACCESS_TOKEN_FOR_USER")
group_id = os.getenv("GROUP_ID")
my_user_id = os.getenv("USER_ID")
# загрузка данных авторизации для реддита
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
user_agent = os.getenv("user_agent")

# авторизация в вк
vk_session = vk_api.VkApi(token=token_for_group)
vk = vk_session.get_api()

vk_session_user = vk_api.VkApi(token=token_for_user)
vk_user = vk_session_user.get_api()

# создания экземпляра класса для прослушки сообщений
longpoll = VkBotLongPoll(vk_session, group_id)


# отправка сообщений в личку (от токена группы)

def send_to_user(id, text, keyboard=None):
    if keyboard == None:
        vk.messages.send(user_id=id, message=text, random_id=get_random_id())
    if keyboard == 'get_keyboard_start_user':
        vk.messages.send(user_id=id, message=text, random_id=get_random_id(),
                         keyboard=my_keyboard.get_keyboard_start_user())
    if keyboard == 'keyboard_other':
        vk.messages.send(user_id=id, message=text, random_id=get_random_id(), keyboard=my_keyboard.get_keyboard_other())
    if keyboard == 'get_keyboard_materials':
        vk.messages.send(user_id=id, message=text, random_id=get_random_id(),
                         keyboard=my_keyboard.get_keyboard_materials())
    if keyboard == 'get_keyboard_time':
        vk.messages.send(user_id=id, message=text, random_id=get_random_id(), keyboard=my_keyboard.get_keyboard_time())
    if keyboard == 'get_keyboard_weather':
        vk.messages.send(user_id=id, message=text, random_id=get_random_id(),
                         keyboard=my_keyboard.get_keyboard_weather())


# отправка сообщений в группу
def send_chat(id, text, keyboard=None):
    if keyboard == None:
        vk.messages.send(chat_id=id, message=text, random_id=get_random_id())
    if keyboard == 'get_keyboard_start_chat':
        vk.messages.send(chat_id=id, message=text, random_id=get_random_id(),
                         keyboard=my_keyboard.get_keyboard_start_chat())
    if keyboard == 'keyboard_other':
        vk.messages.send(chat_id=id, message=text, random_id=get_random_id(), keyboard=my_keyboard.get_keyboard_other())
    if keyboard == 'get_keyboard_weather':
        vk.messages.send(chat_id=id, message=text, random_id=get_random_id(),
                         keyboard=my_keyboard.get_keyboard_weather())

# авторизация в реддите
reddit = praw.Reddit(
                    client_id=client_id,
                    client_secret=client_secret,
                    user_agent=user_agent,
                )
# прослушка и выделение id отправителя, id чата, нахождение требуемого ответа из допустимых
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:

        # если получает сообщение из беседы
        if event.from_chat:
            # из сообщения получает id беседы со стороны каждого пользователя(c моей стороны только)
            id = event.chat_id

            id_user = event.message.get('from_id')
            msg = event.message.get('text')
            # Если в сообщениях в группу с людьми peer_id считается от времени создания
            # в обратном хронологическом порядке (Например, если эта группа создана последней, то номер будет = 1)
            # То в сообщениях личку peer_id считается от времени создания
            # в хронологическом порядке (Например, если эта группа создана последней, то номер будет = 87)
            peer_id = event.message.get('peer_id')

            # цифры - id бота-группы, смотреть в вк, в поисковой строке

            bot_adress = '[club218249845|@public218249845]'
            bot_adress1 = '[club218249845|@club218249845]'

            collection_chat = {
                f"{bot_adress} Погода": (id, f'...', 'get_keyboard_weather'),
                f"{bot_adress1} Погода": (id, f'...', 'get_keyboard_weather'),
                f"{bot_adress} Москва": (id, f'{weather.get_weather("Москва", "RUS")}', None),
                f"{bot_adress1} Москва": (id, f'{weather.get_weather("Москва", "RUS")}', None),
                f"{bot_adress} Назад": (id, f'...', 'get_keyboard_start_chat'),
                f"{bot_adress1} Назад": (id, f'...', 'get_keyboard_start_chat'),
                f"{bot_adress} Получить расписание": (id, f'Выгружаю расписание', None),
                f"{bot_adress1} Получить расписание": (id, f'Выгружаю расписание', None)
            }

            # Возвращает рандомный мем с реддита
            if msg == f"{bot_adress} Отправить мем" or msg == f"{bot_adress1} Отправить мем":

                submission = reddit.subreddit('memes').random()
                item = submission
                while item.url[8] != 'i':
                    submission = reddit.subreddit('memes').random()
                    item = submission
                send_chat(id, f'{item.url}')

            # для пересылания сообщений в группу, оставлю здесь пока, тут по другому ведется подсчет
            if msg == f"{bot_adress} Получить расписание" or msg == f"{bot_adress1} Получить расписание":
                mes = vk_user.messages.search(q='Расписание', peer_id=Name.PEER_ID,
                                              random_id=get_random_id())  # ищет сообщение по строке
                vk_user.messages.send(peer_id=Name.PEER_ID, random_id=get_random_id(),
                                      forward_messages=429330)  # отправляет сообщение (по id) в беседу

            # работа с сообщениями из коллекции
            if msg in collection_chat:
                send_chat(collection_chat[msg][0], collection_chat[msg][1], collection_chat[msg][2])

            # ввод произвольного города и возвращение погоды в нем
            if msg == f"{bot_adress} Ввести другой город" or msg == f"{bot_adress1} Ввести другой город" or msg == 'Введите корректное название города':
                send_chat(id, 'Введите название города и отправьте в беседу')

            # считывает последние два сообщения, в последнем должно содержаться название города
            msg_last_city_chat = vk_user.messages.getHistory(peer_id=Name.PEER_ID, random_id=get_random_id(), count=2)

            city = msg_last_city_chat['items'][0]['text']
            write_city = msg_last_city_chat['items'][1]['text']

            if write_city == 'Введите название города и отправьте в беседу' or write_city == 'Введите корректное название города':
                city = city.split()

                if len(city) == 1:
                    temp = weather.get_weather(city[0])
                    if temp == None:
                        send_chat(id, 'Введите корректное название города')
                    if temp != None:
                        send_chat(id, temp)
                elif len(city) > 1:
                    temp = weather.get_weather(' '.join(city[:-1]), city[-1:])
                    if temp == None:
                        send_chat(id, 'Введите корректное название города')
                    if temp != None:
                        send_chat(id, temp)

            if msg == '.бот':
                # отправка клавиатуры пользователю в беседу
                # ПРОВЕРИТЬ, КАК РАБОТАЕТ У КАМИЛЯ ПОЛУЧЕНИЕ ЕГО ID БЕСЕДЫ
                send_chat(id, 'Hello my boy', 'get_keyboard_start_chat')

        # если получает сообщение из личного сообщения
        if event.from_user:
            # достает id юзера
            id = event.message.get('from_id')

            # достает id чата с ботом и юзером
            # Проверить с КАМОЙ
            chat_id = event.group_id

            chat_id = chat_id * -1

            # достает сообщение в текстовом виде
            msg = event.message.get('text')

            # Возвращает рандомный мем с реддита
            if msg == 'Отправить мем':
                submission = reddit.subreddit('memes').random()
                item = submission
                while item.url[8] != 'i':
                    submission = reddit.subreddit('memes').random()
                    item = submission
                send_to_user(id, f'{item.url}')

            if msg == '.бот':
                # отправка клавиатуры пользователю в личные сообщения
                send_to_user(id, 'Hello my boy', 'get_keyboard_start_user')

            if msg == 'Получить расписание':
                vk_user.messages.send(peer_id=id, random_id=get_random_id(), forward_messages=429330)

            collection_user = {
                # клавиатура get_keyboard_start_user
                f"Получить расписание": (id, f'Выгружаю расписание', None),
                f"Получить материалы": (id, f'Выберите предмет', 'get_keyboard_materials'),
                f"Разное": (id, f'Загружаю разное', 'keyboard_other'),

                # клавиатура get_keyboard_other
                f"Погода": (id, f'...', 'get_keyboard_weather'),
                f"Назад.": (id, f'Назад.', 'get_keyboard_start_user'),

                # клавиатура get_keyboard_materials
                f"Староверов": (id, f'Староверов', 'get_keyboard_time'),
                f"Менеджмент": (id, f'Менеджмент', 'get_keyboard_time'),
                f"Материаловедение": (id, f'Материаловедение', 'get_keyboard_time'),
                f"Дубровский": (id, f'Дубровский', 'get_keyboard_time'),
                f"Экология": (id, f'Экология', 'get_keyboard_time'),
                f"Ввести свой запрос": (
                    id, f'Введите запрос и отправьте мне. Потом выбирите время на клавиатуре', 'get_keyboard_time'),
                f"Назад": (id, f'Назад', 'keyboard_other'),
                f"Назад..": (id, f'Назад.', 'get_keyboard_materials'),

                # клавиатура get_keyboard_weather
                f"Москва": (id, f'{weather.get_weather("Москва", "RUS")}', None),
            }

            collection_user_time = {
                # клавиатура get_keyboard_time
                f"за 2 недели": (id, f'за 2 недели', None),
                f"за 1 месяц": (id, f'за 1 месяц', None),
                f"за 3 месяца": (id, f'за 3 месяца', None),
                f"за 6 месяцев": (id, f'за 6 месяцев', None),
                f"за 1 год": (id, f'за 1 год', None),
            }

            # ввод произвольного города и возвращение погоды в нем
            if msg == f"Ввести другой город" or msg == 'Введите корректное название города':
                send_to_user(id, 'Введите название города и отправьте мне')

            # считывает последние два сообщения, в последнем должно содержаться название города
            msg_last_city_chat = vk.messages.getHistory(peer_id=id, random_id=get_random_id(), count=2)
            city = msg_last_city_chat['items'][0]['text']
            write_city = msg_last_city_chat['items'][1]['text']

            if write_city == 'Введите название города и отправьте мне' or write_city == 'Введите корректное название города':
                city = city.split()
                if len(city) == 1:
                    temp = weather.get_weather(city[0])
                    if temp == None:
                        send_to_user(id, 'Введите корректное название города')
                    if temp != None:
                        send_to_user(id, temp)
                elif len(city) > 1:
                    temp = weather.get_weather(' '.join(city[:-1]), city[-1:])
                    if temp == None:
                        send_to_user(id, 'Введите корректное название города')
                    if temp != None:
                        send_to_user(id, temp)

            # Здесь парсит опять два последних сообщения за счет юзера и смотрит, если в предыдущем "ввести другой город",
            # а в последнем какое то слово, то он его загоняет в weather, а она выдает сразу инфу. Про москву тоже сделать

            # определяет вид материала, время, за которое нужно вернуть его, а также сам парсер материалов из беседы
            if msg in collection_user_time:
                # определяет, подряд ли идут два сообщения: предмет/препод, а потом время возвращения
                msg_last = vk.messages.getHistory(peer_id=id, random_id=get_random_id(), count=2)
                flag1 = False
                flag2 = False
                time_return = msg_last['items'][0]['text']
                object_or_name = msg_last['items'][1]['text']
                if time_return in collection_user_time:
                    flag1 = True
                if object_or_name in collection_user or type(object_or_name) == str:
                    flag2 = True
                if flag1 == True and flag2 == True:

                    # время, за которое нужно вернуть сообщения
                    if time_return == 'за 2 недели':
                        time_return = 1209600
                    if time_return == 'за 1 месяц':
                        time_return = 2419200
                    if time_return == 'за 3 месяца':
                        time_return = 7257600
                    if time_return == 'за 6 месяцев':
                        time_return = 14515200
                    if time_return == 'за 1 год':
                        time_return = 29030400
                    # для нахождения требуемого сообщения (меняется только через код)
                    object_or_name = object_or_name

                    # здесь номер группы будет отличаться, здесь счет в хронологическом порядке
                    materials = vk_user.messages.search(q=object_or_name, peer_id=Name.PEER_ID,
                                                        random_id=get_random_id(), count=100)

                    # цикл перебора полученных материалов и их пересылание

                    # если ничего не нашел
                    if materials['count'] == 0:
                        vk.messages.send(user_id=id, message='Ничего не найдено', random_id=get_random_id())

                    try:
                        # пересылание сообщений
                        materials_counter = materials['count']
                        whole_materials = []

                        for i in materials['items']:
                            id_message = i['id']

                            # время создания сообщения
                            time_message = i['date']

                            # время создания, отсылается, если сообщение слишком старое
                            old_mes_time = time.asctime(time.localtime(time_message))

                            # сравнивается время создания и настоящее время за вычетом выбранного
                            if (round(time.time()) - int(time_return)) <= time_message:
                                whole_materials.append(id_message)

                            else:
                                vk.messages.send(user_id=id,
                                                 message=f'Слишком старое сообщение, дата его создания: {old_mes_time}',
                                                 random_id=get_random_id())
                                print('Слишком старый файл')

                        vk_user.messages.send(peer_id=id, random_id=get_random_id(),
                                              forward_messages=whole_materials)
                        vk.messages.send(user_id=id, message=f'Отправлено: {materials_counter} сообщений. На этом все.',
                                         random_id=get_random_id())
                    except:
                        vk.messages.send(user_id=id,
                                         message=f'Зачем ты тыкаешь, дай мне спокойно все выгрузить. Посиди в бане 5 минут, а потом повтори запрос. Осталось материалов: {materials_counter}',
                                         random_id=get_random_id())

                # если запрос был задан неправильно
                else:
                    print('No')
                    send_to_user(id, 'Повторите запрос еще раз', 'get_keyboard_materials')

            # определяет объект/препод и отсылает клавиатуру с выбором времени возвращения
            if msg in collection_user:
                send_to_user(collection_user[msg][0], collection_user[msg][1], collection_user[msg][2])

if __name__ == '__main__':
    main()
