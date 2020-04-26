import random
from vk_api.longpoll import VkLongPoll, VkEventType
import week
import pars
import vk_api
import glossing

fuck = pars.Parse(pars.Site('https://edu.donstu.ru/Rasp/Rasp.aspx?group=32353&sem=2'))
vk_session = vk_api.VkApi(token="4e3f2af11078b879a7a574564ca5d14f3eb100cdb69c6ff953e1096c5a67f5a6d06233a295e52bc416026")
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()


def random_id():
    Random = 0
    Random += random.randint(0, 1000000000000)
    return Random


# Функция, чтобы можно было отправлять сообщение одно и тому же

def open_read_file(namefile):
    if namefile in "events.txt":
        event = open("events.txt", encoding='utf8')
        lines = ""
        for line in event:
            lines += line
        return lines

    elif namefile in "students_numbers":
        students_numbers = open("students_numbers", encoding='utf8')
        linet = ''
        for line in students_numbers:
            linet += line
        return linet


while True:
    otvet1 = ['Тыкай по кнопочкам', 'Сейчас разозлюсь']
    otvet2 = ['Че?', 'А?']
    i = 0
    k = 1
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            # пусть пока будет так но потом нужно будет это норм сделать
            # может быть стоит это потом вынести в отдельную фу-цию


            if event.text.lower() == 'расписание':  # Нижний регистр.
                vk.messages.send(
                    user_id=event.user_id,
                    message=fuck,
                    keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                    random_id=random_id()
                )
                k = 2
            elif event.text.lower() == 'неделя':
                vk.messages.send(
                    user_id=event.user_id,
                    message=week.Week(fuck),
                    keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                    random_id=random_id()
                )
                k = 2
            elif event.text.lower() == 'другие команды':
                vk.messages.send(
                    user_id=event.user_id,
                    message='Ты взломать мою жепку',
                    keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                    random_id=random_id()
                )
                k = 2

            elif event.text.lower() == "события":
                vk.messages.send(
                    user_id=event.user_id,
                    message=open_read_file("events.txt"),
                    keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                    random_id=random_id()
                )
                k = 2

            elif event.text.lower() == 'голосование':

                vk.messages.send(
                    user_id=event.user_id,
                    message=open_read_file("students_numbers"),  # Вывод сообщения о входе в режим голосования.
                    keyboard=open("glossing_keyboard.json", "r", encoding="UTF-8").read(),
                    # Вызываем главиатуру голосования.
                    random_id=random_id()
                )
                vk.messages.send(
                    user_id=event.user_id,
                    message=glossing.glossing(vk_session, fuck),  # Вызываем метод "голосование"
                    keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                    random_id=random_id()
                )
                k = 3

            else:
                if k != 3:
                    if i < 4:
                        vk.messages.send(
                            user_id=event.user_id,
                            message=random.choice(otvet1),
                            keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                            random_id=random_id()
                        )
                        i += 1
                    else:
                        vk.messages.send(
                            user_id=event.user_id,
                            message=random.choice(otvet2),
                            keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                            random_id=random_id()
                        )
