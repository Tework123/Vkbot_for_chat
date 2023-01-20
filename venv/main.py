import time
import vk_api, json
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import wiki_parcer
import my_keyboard
from dotenv import load_dotenv  # загрузка информации из .env-файла
import os  # работа с файловой системой
import Name
# загрузка токена и id группы из локального виртуального окружения
load_dotenv()
token_for_group = os.getenv("ACCESS_TOKEN_FOR_GROUP")
token_for_user = os.getenv("ACCESS_TOKEN_FOR_USER")
group_id = os.getenv("GROUP_ID")
my_user_id = os.getenv("USER_ID")

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
        vk.messages.send(user_id=id, message=text, random_id=get_random_id(), keyboard=my_keyboard.get_keyboard_start_user())
    if keyboard == 'keyboard_other':
        vk.messages.send(user_id=id, message=text, random_id=get_random_id(), keyboard=my_keyboard.get_keyboard_other())
    if keyboard == 'get_keyboard_materials':
        vk.messages.send(user_id=id, message=text, random_id=get_random_id(),
                         keyboard=my_keyboard.get_keyboard_materials())
    if keyboard == 'get_keyboard_time':
        vk.messages.send(user_id=id, message=text, random_id=get_random_id(), keyboard=my_keyboard.get_keyboard_time())


# отправка сообщений в группу
def send_chat(id, text, keyboard=None):
    if keyboard == None:
        vk.messages.send(chat_id=id, message=text, random_id=get_random_id())
    if keyboard == 'get_keyboard_start_chat':
        vk.messages.send(chat_id=id, message=text, random_id=get_random_id(), keyboard=my_keyboard.get_keyboard_start_chat())
    if keyboard == 'keyboard_other':
        vk.messages.send(chat_id=id, message=text, random_id=get_random_id(), keyboard=my_keyboard.get_keyboard_other())


# прослушка и выделение id отправителя, id чата, нахождение требуемого ответа из допустимых
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:

        # если получает сообщение из беседы
        if event.from_chat:
            print('chat')
            #из сообщения получает id беседы со стороны каждого пользователя(c моей стороны только)
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

            collection_chat = {
                f"{bot_adress} Отправить мем": (id, f'Отправляю мем', None),
                f"{bot_adress} Получить расписание": (id, f'Выгружаю расписание', None),
            }

            # для пересылания сообщений в группу, оставлю здесь пока, тут по другому ведется подсчет
            if msg == 'a':
                # mes = vk_user.messages.getHistory(peer_id=2000000000+100, random_id=get_random_id(), count=10)
                mes = vk_user.messages.search(q='vot', peer_id=2000000000+100, random_id=get_random_id(), count=1) #ищет сообщение по строке
                # print(mes)
                # for i in mes['items']:
                #     print(i)
                vk_user.messages.send(peer_id=2000000000+100, random_id=get_random_id(), forward_messages=427245) #отправляет сообщение (по id) в беседу
                mes2 = vk_user.messages.searchConversations(q='tren') #ищет беседу
                #print(mes2)

            if msg == '.бот':
                #отправка клавиатуры пользователю в беседу
                #ПРОВЕРИТЬ, КАК РАБОТАЕТ У КАМИЛЯ ПОЛУЧЕНИЕ ЕГО ID БЕСЕДЫ
                send_chat(id, 'Hello my boy', 'get_keyboard_start_chat')

            if msg in collection_chat:
                send_chat(collection_chat[msg][0], collection_chat[msg][1], collection_chat[msg][2])


        # если получает сообщение из личного сообщения
        if event.from_user:
            # достает id юзера
            id = event.message.get('from_id')
            # достает id чата с ботом и юзером
            chat_id = event.group_id

            chat_id = chat_id*-1
            # достает сообщение в текстовом виде
            msg = event.message.get('text')

            if msg == '.бот':
                # отправка клавиатуры пользователю в личные сообщения
                send_to_user(id, 'Hello my boy', 'get_keyboard_start_user')

            collection_user = {
                # клавиатура get_keyboard_start_user
                f"Получить расписание": (id, f'Выгружаю расписание', None),
                f"Получить материалы": (id, f'Выберите предмет', 'get_keyboard_materials'),
                f"Разное": (id, f'Загружаю разное', 'keyboard_other'),

                # клавиатура get_keyboard_other
                f"Отправить мем": (id, f'Отправляю мем', None),
                f"Назад": (id, f'Назад', 'get_keyboard_start_user'),

                # клавиатура get_keyboard_materials
                f"Староверов": (id, f'Староверов', 'get_keyboard_time'),
                f"Менеджмент": (id, f'Менеджмент', 'get_keyboard_time'),
                f"Материаловедение": (id, f'Материаловедение', 'get_keyboard_time'),
                f"Дубровский, Сучков": (id, f'Дубровский, Сучков', 'get_keyboard_time'),
                f"Экология": (id, f'Экология', 'get_keyboard_time'),
                f"Назад": (id, f'Назад', 'get_keyboard_start_user'),
                f"Назад.": (id, f'Назад.', 'get_keyboard_materials')
            }

            collection_user_time = {
                # клавиатура get_keyboard_time
                f"за 2 недели": (id, f'за 2 недели', None),
                f"за 1 месяц": (id, f'за 1 месяц', None),
                f"за 3 месяца": (id, f'за 3 месяца', None),
                f"за 6 месяцев": (id, f'за 6 месяцев', None),
                f"за 1 год": (id, f'за 1 год', None),
            }
            #определяет вид материала, время, за которое нужно вернуть его, а также сам парсер материалов из беседы
            if msg in collection_user_time:
                # определяет, подряд ли идут два сообщения: предмет/препод, а потом время возвращения
                msg_last = vk.messages.getHistory(peer_id=id, random_id=get_random_id(), count=2)
                flag1 = False
                flag2 = False
                time_return = msg_last['items'][0]['text']
                object_or_name = msg_last['items'][1]['text']
                if time_return in collection_user_time:
                    flag1 = True
                if object_or_name in collection_user:
                    flag2 = True
                if flag1 == True and flag2 == True:

                    #время, за которое нужно вернуть сообщения
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
                    # здесь номер группы будет отличаться, здесь счет в хронологическом порядке
                    materials = vk_user.messages.search(q=object_or_name, peer_id=Name.PEER_ID, random_id=get_random_id())
                    # если ничего не нашел
                    if materials['count'] == 0:
                        vk.messages.send(user_id=id, message='Ничего не найдено', random_id=get_random_id())
                    # пересылание сообщений
                    for i in materials['items']:
                        id_message = i['id']

                        # время создания сообщения
                        time_message = i['date']

                        # время создания, отсылается, если сообщение слишком старое
                        old_mes_time = time.asctime(time.localtime(time_message))

                        # сравнивается время создания и настоящее время за вычетом выбранного
                        if (round(time.time()) - int(time_return)) <= time_message:
                            vk_user.messages.send(peer_id=chat_id, random_id=get_random_id(), forward_messages=id_message)
                            print('отправил')
                        else:
                            vk.messages.send(user_id=id, message=f'Слишком старое сообщение, дата его создания: {old_mes_time}', random_id=get_random_id())
                            print('Слишком старый файл')

                # если запрос был задан неправильно
                else:
                    print('No')
                    send_to_user(id, 'Повторите запрос еще раз', 'get_keyboard_materials')

            # определяет объект/препод и отсылает клавиатуру с выбором времени возвращения
            if msg in collection_user:
                send_to_user(collection_user[msg][0], collection_user[msg][1], collection_user[msg][2])


if __name__ == '__main__':
    main()

    # f'@id{id_user} Получить расписание')
    # send_chat(id, f'@id{id_user} Hello everybody')
    # send_chat(id, f'Ваш заказ: {wiki_parcer.wiki_parcer()}')


# group_id1 = vk_user.messages.searchConversations(q=Name.names['group_name'])
# group_id1 = group_id1['items'][0]['peer']['id']
# print(group_id1)