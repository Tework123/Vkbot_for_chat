import vk_api, json
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import wiki_parcer
import my_keyboard
from dotenv import load_dotenv  # загрузка информации из .env-файла
import os  # работа с файловой системой

# загрузка токена и id группы из локального виртуального окружения
load_dotenv()
token = os.getenv("ACCESS_TOKEN")
group_id = os.getenv("GROUP_ID")

# авторизация в вк
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

# создания экземпляра класса для прослушки сообщений
longpoll = VkBotLongPoll(vk_session, group_id)


# отправка сообщений без клавиатуры
def send_chat(id, text):
    vk.messages.send(chat_id=id, message=text, random_id=get_random_id())


def send_to_user(id, text, keyboard=None):
    if keyboard == None:
        vk.messages.send(user_id=id, message=text, random_id=get_random_id())
    if keyboard == 'keyboard_start':
        vk.messages.send(user_id=id, message=text, random_id=get_random_id(), keyboard=my_keyboard.get_keyboard_start())
    if keyboard == 'keyboard_other':
        vk.messages.send(user_id=id, message=text, random_id=get_random_id(), keyboard=my_keyboard.get_keyboard_other())
    if keyboard == 'keyboard_attach':
        vk.messages.send(user_id=id, message=text, random_id=get_random_id(),
                         keyboard=my_keyboard.get_keyboard_attach())
    if keyboard == 'keyboard_put':
        vk.messages.send(user_id=id, message=text, random_id=get_random_id(), keyboard=my_keyboard.get_keyboard_put())


# отправка сообщений с клавиатурой
def send_chat(id, text, keyboard=None):
    if keyboard == None:
        vk.messages.send(chat_id=id, message=text, random_id=get_random_id())
    if keyboard == 'keyboard_start':
        vk.messages.send(chat_id=id, message=text, random_id=get_random_id(), keyboard=my_keyboard.get_keyboard_start())
    if keyboard == 'keyboard_other':
        vk.messages.send(chat_id=id, message=text, random_id=get_random_id(), keyboard=my_keyboard.get_keyboard_other())
    if keyboard == 'keyboard_attach':
        vk.messages.send(chat_id=id, message=text, random_id=get_random_id(),
                         keyboard=my_keyboard.get_keyboard_attach())
    if keyboard == 'keyboard_put':
        vk.messages.send(chat_id=id, message=text, random_id=get_random_id(), keyboard=my_keyboard.get_keyboard_put())


def send_photo(id, text, url):
    vk.messages.send(chat_id=id, message=text, attachment=url, random_id=get_random_id())


# прослушка и выделение id отправителя, id чата, нахождение требуемого ответа из допустимых
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        # если получает сообщение из беседы
        if event.from_chat:
            print('chat')
            id = event.chat_id
            id_user = event.message.get('from_id')
            msg = event.message.get('text')
            # peer_id = event.message.get('peer_id')  # также c attachments
            # print(peer_id)

            bot_adress = '[club218249845|@public218249845]'
            collection = {
                f"{bot_adress} Отправить мем": (id, f' Отправляю мем'),
                f"{bot_adress} Получить расписание": (id, f' Выгружаю расписание'),
                # клавиатура "добавить метку"
                f"{bot_adress} Добавить метку": (id, f'Добавить метку')
            }
            collection_keyboard_start = {
                f"{bot_adress} Назад": (id, f'Назад', 'keyboard_start'),
                f"{bot_adress} Разное": (id, f'Разное', 'keyboard_other'),
                f"{bot_adress} Материалы": (id, f'Выберите дальнейшее действие', 'keyboard_attach'),
                # клавиатура "материалы"
                f"{bot_adress} Добавить метку": (id, f'Добавить метку', 'keyboard_put')
            }

            if msg == '.бот':
                send_chat(id, 'Hello my boy', 'keyboard_start')
            if msg in collection:
                send_chat(collection[msg][0], collection[msg][1])
            if msg in collection_keyboard_start:
                send_chat(collection_keyboard_start[msg][0],
                          collection_keyboard_start[msg][1],
                          collection_keyboard_start[msg][2])

        # если получает сообщение из личного сообщения
        if event.from_user:
            print('user')
            id_user = event.message.get('from_id')
            id = id_user

            collection = {
                f"Отправить мем": (id, f' Отправляю мем'),
                f"Получить расписание": (id, f' Выгружаю расписание'),
                # клавиатура "добавить метку"
                f"Добавить метку": (id, f'Добавить метку')
            }
            collection_keyboard_start = {
                f"Назад": (id, f'Назад', 'keyboard_start'),
                f"Разное": (id, f'Разное', 'keyboard_other'),
                f"Материалы": (id, f'Выберите дальнейшее действие', 'keyboard_attach'),
                # клавиатура "материалы"
                f"Добавить метку": (id, f'Добавить метку', 'keyboard_put')
            }

            msg = event.message.get('text')
            if msg == '.бот':
                send_to_user(id, 'Hello my boy', 'keyboard_start')
            if msg in collection:
                send_to_user(collection[msg][0], collection[msg][1])
            if msg in collection_keyboard_start:
                send_to_user(collection_keyboard_start[msg][0],
                             collection_keyboard_start[msg][1],
                             collection_keyboard_start[msg][2])

if __name__ == '__main__':
    main()

# f'@id{id_user} Получить расписание')
# send_chat(id, f'@id{id_user} Hello everybody')
# send_chat(id, f'Ваш заказ: {wiki_parcer.wiki_parcer()}')
