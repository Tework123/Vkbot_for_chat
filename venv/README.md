# Vk_bot for chat
___
Bot search messages with attachments in the vk group. Send them to user.
Then bot get weather any city. Send random memes from reddit and few other functions.
:smiley:
### Example
___
![logo](1.PNG)
![logo](2.PNG)


### Installation and usage
___
:white_circle: Repository:
+ Copy repository on your pc.
+ Install requirements.txt
  + in the Terminal: `pip freeze > requirements.txt`

:large_blue_circle: Vk group:
+ Create new group in vk
  +  get access_token for this group (full access).
     + create on your pc .env, put there access_token (example exist)
     + take group_id (your bot) from search string and put this to .env
     + put group_id for bot_adress and bot_adress1
  + turn on LongPull Api in settings vk group
  + you must give 2 permissions for bot:
    +  settings > LongPull Api > 'Типы событий' > 'full marks'
    +  messages > 'Сообщения сообщества' > 'turn on'
    
:large_blue_diamond: Vk page:
    
Yes, messages will be send from your personal page. My pleasure vk for full permission
for beginner developers.
+ Get access_token for your personal page.
  + put this to .env
  + take user_id (your personal) from search string and put this to .env

:red_circle: Reddit:
+ create new app
  + get client_id and put to .env
  + get client_secret and put to .env
  + user_agent="http://localhost:8080" (always) and put to .env

:pencil: Put few fails:
  + Put 'Инструкция.pdf' to folder
  + Put 'расписание.jpg' to folder

:school: Vk group with users:
+ Add bot to group
    + get permission put messages for bot
    + take peer_id (this group(not bot)) from search string (last digits) and put this to .env
+ You must be there too

:boy: Usage for peoples:
+ Say them:
        send message ".бот" to group with bot