import vk_api
import requests
from dotenv import load_dotenv
from vk_api.utils import get_random_id  # для стабильной работы vk api
import os

# загрузка токена и id группы из локального виртуального окружения
load_dotenv()
token_for_group = os.getenv("ACCESS_TOKEN_FOR_GROUP")
token_for_user = os.getenv("ACCESS_TOKEN_FOR_USER")
group_id = os.getenv("GROUP_ID")
my_user_id = os.getenv("USER_ID")

vk_session = vk_api.VkApi(token=token_for_user)
vk_user = vk_session.get_api()

vk_session_group = vk_api.VkApi(token=token_for_group)
vk = vk_session_group.get_api()
# загрузка фото на стену группы
text = 'a vot tak'
# #vk_user.messages.send(user_id=my_user_id, message=text, random_id=get_random_id())
vk.messages.send(user_id=my_user_id, message=text, random_id=get_random_id())
upload_url = vk_user.photos.getWallUploadServer(group_id=group_id)['upload_url']
print(upload_url)
request = requests.post(upload_url, url='https://i.redd.it/res0dl1oyqda1.jpg')
print(request.json())

save_wall_photo = vk_user.photos.saveWallPhoto(group_id=group_id, photo=request.json()['photo'],
                                                server=request.json()['server'], hash=request.json()['hash'])
print(save_wall_photo)
saved_photo = 'photo' + str(save_wall_photo[0]['owner_id']) + '_' + str(save_wall_photo[0]['id'])
print(saved_photo)
#
vk_user.wall.post(owner_id=-218249845,attachments=saved_photo)
print('YES')

# загрузка фото в сообщения

# upload_url = vk.photos.getMessagesUploadServer(peer_id=0)['upload_url']
# print(upload_url)
#
# request = requests.post(upload_url)
# print(request.json())
# save_Messages_photo = vk.photos.saveMessagesPhoto(photo=request.json()['photo'],
#                                                 server=request.json()['server'], hash=request.json()['hash'])
# print(save_Messages_photo)
# saved_photo = 'photo' + str(save_Messages_photo[0]['owner_id']) + '_' + str(save_Messages_photo[0]['id'])
# print(saved_photo)
# #vk_user.messages.send(user_id=my_user_id, message=text, attachment=saved_photo, random_id=get_random_id())
# vk.messages.send(user_id=my_user_icd, message=text, attachment=saved_photo, random_id=get_random_id())
# print('YES')