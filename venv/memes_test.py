import praw
from vkwave.bots import SimpleLongPollBot, SimpleBotEvent
from vkwave.bots.utils.uploaders import PhotoUploader
import  requests
reddit = praw.Reddit(
    client_id="cOEd44XJPTjIgs9jMKYCbg",
    client_secret="TUKP3UDrve7T0GWV979w87bHVF-DZw",
    #password="UC5Td,),vSF.3*x",
    user_agent="http://localhost:8080",
    #username="Teowork123",
    )

memes_sub = reddit.subreddit('memes')
memes_sub = memes_sub.new(limit=1)
print(memes_sub)
item = memes_sub.__next__()
print(item.url)

req = requests.post(item.url)
print(req.text)