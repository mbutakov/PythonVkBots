import random

import time
import vk_api
import collections
import datetime
import jconfig
import random

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from multiprocessing import Process
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.audio import VkAudio
from vk_api.upload import VkUpload
TOKEN_VK = ""



def mbutakov():
    vk_session = vk_api.VkApi(
        token=TOKEN_VK)
    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()
    x = 0
    randomint = 0
    list = ["💖","💚","❤","💜","💛","💚","💙"]

    while(True):
        time.sleep(30)
        randomint = random.randint(0,3)
        vk.messages.send(peer_id=342002487, random_id=get_random_id(), message="" + random.choice(list) + random.choice(list) + random.choice(list) + random.choice(list))
        x += 1
        print(x)
        if x > 199:
                print("stoped bot")
                SystemExit(228)
                exit(0)


if __name__ == '__main__':
    Process(target=mbutakov).start()
