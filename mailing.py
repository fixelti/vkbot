import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll
import random


def open_file_user_id():
    users_id = open("users_id.txt", encoding='utf8')
    lines = ""
    for line in users_id:
        lines += line
    return lines


class Mailing(object):

    def __init__(self):
        self.vk_session = vk_api.VkApi(
            token="4e3f2af11078b879a7a574564ca5d14f3eb100cdb69c6ff953e1096c5a67f5a6d06233a295e52bc416026")
        self.longpoll = VkLongPoll(self.vk_session)
        self.vk = self.vk_session.get_api()

    def random_id(self):
        Random = 0
        Random += random.randint(0, 1000000000000)
        return Random

    def mailing(self):  # доработать
        longpoll = VkLongPoll(self.vk_session)  # подключение к боту

        while True:
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    message_for_mailing = event.text.lower()
                    b = 0
                    a = ""
                    if event.user_id == 263542561:
                        for i in open_file_user_id():
                            print(i)
                            if b < 9:
                                a += i
                                b += 1
                            elif b == 9:
                                b = 0
                                print(i)
                                self.vk.messages.send(
                                    user_id=int(a),
                                    message=message_for_mailing,
                                    keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                                    random_id=self.random_id()
                                )
                                a = ""
                        return "Выполнено"
                    else:
                        self.vk.messages.send(
                            user_id=event.user_id,
                            message="У тебя здесь нет власти",
                            keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                            random_id=self.random_id()
                        )
                    return "Выполнено"
