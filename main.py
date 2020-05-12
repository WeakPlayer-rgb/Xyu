import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import bs4
import requests
from vk_bot import VkBot

def write_msg(user_id, message):
    random_id = vk_api.utils.get_random_id()
    print(message)
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random_id})

token = "34b2ad9d1ff7a407fb596ae2706d717710f4768c779c4d7c63ac8fc394c4a71c8d174cc2d1bed53eded83"

vk = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk)

print("Server started")
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            
            #print('New message:')
            #print(f'For me by: {event.user_id}', end='')
            
            bot = VkBot(event.user_id)
            write_msg(event.user_id, bot.new_message(event.text))
            
            #print('Text: ', event.text)
