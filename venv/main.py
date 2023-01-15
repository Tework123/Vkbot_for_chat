import vk_api, json
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import wiki_parcer
import my_keyboard
from dotenv import load_dotenv  # загрузка информации из .env-файла
import os  # работа с файловой системой

load_dotenv()
token = os.getenv("ACCESS_TOKEN")
group_id = os.getenv("GROUP_ID")
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

longpoll = VkBotLongPoll(vk_session, group_id)


def send(id, text):
    pass
#aasd

def send_chat(id, text):
    vk.messages.send(chat_id=id, message=text, random_id=get_random_id(), keyboard=my_keyboard.get_my_keyboard())


def send_photo(id, url):
    vk.messages.send(chat_id=id, attachment=url, random_id=get_random_id())


for event in longpoll.listen():

    if event.type == VkBotEventType.MESSAGE_NEW:
        print(event.object)
        print(event.object.message['from_id'])
        print(event.object.message['attachments'])
        print(event.object.message['peer_id'])
        print(event.object.message['text'])

        if event.from_chat:
            id = event.chat_id
            id_user = event.object.message['from_id']
            msg = event.object.message['text'].lower()
            if msg == 'a':
                send_chat(id, f'@id{id_user} Hello everybody')
                send_chat(id, f'Ваш заказ: {wiki_parcer.wiki_parcer()}')

        # if __name__ == '__main__':
        #     main()