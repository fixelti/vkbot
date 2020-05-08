import random
from vk_api.longpoll import VkLongPoll, VkEventType
import week
import pars
import vk_api
import mailing
import students


class pidor():

    fuck = pars.Parse(pars.Site('https://edu.donstu.ru/Rasp/Rasp.aspx?group=32353&sem=2'))
    vk_session = vk_api.VkApi(token="4e3f2af11078b879a7a574564ca5d14f3eb100cdb69c6ff953e1096c5a67f5a6d06233a295e52bc416026")
    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()

    def open_read_file(self, namefile):
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

    def __init__(self, fuck, vk_session, longpoll, vk, random, lines):
        self.fuck = pars.Parse(pars.Site('https://edu.donstu.ru/Rasp/Rasp.aspx?group=32353&sem=2'))
        self.vk_session = vk_api.VkApi(token="4e3f2af11078b879a7a574564ca5d14f3eb100cdb69c6ff953e1096c5a67f5a6d06233a295e52bc416026")
        self.longpoll = VkLongPoll(vk_session)
        self.vk = vk_session.get_api()
        self.random
        self.lines

    def random_id(self):
        random = 0
        random += random.randint(0, 1000000000000)
        return random

    def glossing(self, vk_session):
        longpoll = VkLongPoll(vk_session)  # подключение к боту
        vk = vk_session.get_api()  # входящее сообщение
        s = True
        while s:
            print("а я тут работаю азазазазазазза")
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    if event.text.lower() == 'назад':  # Если пользователь вводит это значение, то
                        vk.messages.send(  # Его выкидывают в начальные кнопки
                            user_id=event.user_id,  # Для выбора другой операци
                            message="Не стоило тебе сюда заходить",
                            keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                            random_id=self.random_id(self)
                        )
                        s = False
                        return "*боевая музыка из скайрима"

                    elif event.text.lower() == 'узнать рейтинг':
                        for event in longpoll.listen():
                            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                number = event.text.lower()
                                vk.messages.send(  # Его выкидывают в начальные кнопки
                                    user_id=event.user_id,  # Для выбора другой операци
                                    message="Получи",
                                    keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                                    random_id=self.random_id(self)
                                )
                                return students.ratingg(number, event.user_id)



                    else:

                        # # Получаем от пользователя номер студента и его оценку
                        # number = event.text.lower()  # Номер студента
                        # try:
                        #     number = int(number)
                        # except ValueError :
                        #     return "Уверен, в следующий раз у тебя получится написать целую цифрику "
                        number = event.text.lower()
                        for events in longpoll.listen():
                            if events.type == VkEventType.MESSAGE_NEW and event.to_me:
                                gloss = events.text.lower()  # Оценка для студента
                                return students.student_info(number, gloss,
                                                             event.user_id)  # Возвращаем значение из функции
                            # student_info из файла students

    # Функция, чтобы можно было отправлять сообщение одно и тому же

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
                        message="Введи превым целым числом номер нужного студента " + "\n" + "следующее число - оценка , котору ты бы ему хотел поставить ( от 1 до 5) " + '\n' + pidor.open_read_file(
                            "students_numbers"),  # Вывод сообщения о входе в режим голосования.
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
                elif event.text.lower() == "рассылка":
                    if event.user_id == 263542561 or 293470132:
                        vk.messages.send(
                            user_id=event.user_id,
                            message="вставайте, зови мужиком, работаем" + mailing.mailing(vk_session),
                            keyboard=open("glossing_keyboard.json", "r", encoding="UTF-8").read(),
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
        print("айди юзера равен = " + str(event.user_id))
