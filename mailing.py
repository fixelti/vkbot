from vk_api.longpoll import VkEventType, VkLongPoll
import random


def open_file_user_id():
    users_id = open("users_id.txt", encoding='utf8')
    lines = ""
    for line in users_id:
        lines += line
    return lines


def random_id():
    Random = 0
    Random += random.randint(0, 1000000000000)
    return Random


def mailing(vk_session):
    longpoll = VkLongPoll(vk_session)  # подключение к боту
    vk = vk_session.get_api()  # входящее сообщение


    while True:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                message_for_mailing = event.text.lower()
                i = ""
                a = ""
                for i in open_file_user_id():

                    if len(a) < 9:
                        a += i
                        print(int(a))
                    else:
                        vk.messages.send(
                            user_id=int(a),
                            message="кек",
                            keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                            random_id=random_id()
                        )
                    a = ""