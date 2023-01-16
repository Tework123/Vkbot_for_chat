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


# отправка сообщений с клавиатурой
def send_new_keyboard(id, text, keyboard):
    if keyboard == 'keyboard_start':
        vk.messages.send(chat_id=id, message=text, random_id=get_random_id(), keyboard=my_keyboard.get_keyboard_start())
    if keyboard == 'keyboard_one':
        vk.messages.send(chat_id=id, message=text, random_id=get_random_id(), keyboard=my_keyboard.get_keyboard_one())
    if keyboard == 'keyboard_two':
        vk.messages.send(chat_id=id, message=text, random_id=get_random_id(), keyboard=my_keyboard.get_keyboard_two())


def send_photo(id, url):
    vk.messages.send(chat_id=id, attachment=url, random_id=get_random_id())


# прослушка и выделение id отправителя, id чата, нахождение требуемого ответа из допустимых
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_chat:
            id = event.chat_id
            id_user = event.message.get('from_id')
            msg = event.message.get('text')
            peer_id = event.message.get('peer_id')  # также c attachments
            bot_adress = '[club218249845|@public218249845]'

            # словари с ответными действиями
            collection = {
                f"{bot_adress} Отправить мем": (id, f' Отправляю мем'),
                f"{bot_adress} Получить расписание": (id, f' Выгружаю расписание'),
            }
            collection_keyboard = {
                f"{bot_adress} Назад": (id, f' Назад', 'keyboard_start'),
                f"{bot_adress} Разное": (id, f' Разное', 'keyboard_one'),
                f"{bot_adress} Материалы": (id, f' Выберите дальнейшее действие', 'keyboard_two')
            }

            if msg == '.бот':
                send_new_keyboard(id, 'Hello my boy', 'keyboard_start')
            if msg in collection:
                send_chat(collection[msg][0], collection[msg][1])
            if msg in collection_keyboard:
                send_new_keyboard(collection_keyboard[msg][0], collection_keyboard[msg][1], collection_keyboard[msg][2])

if __name__ == '__main__':
    main()

# f'@id{id_user} Получить расписание')
# send_chat(id, f'@id{id_user} Hello everybody')
# send_chat(id, f'Ваш заказ: {wiki_parcer.wiki_parcer()}')
