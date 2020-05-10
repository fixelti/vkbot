import random
from vk_api.longpoll import VkLongPoll, VkEventType
import week
import pars
import vk_api
import mailing
import students


class Message():


    def __init__(self):
        self.fuck = pars.Parse(pars.Site('https://edu.donstu.ru/Rasp/Rasp.aspx?group=32353&sem=2'))
        self.vk_session = vk_api.VkApi(
            token="4e3f2af11078b879a7a574564ca5d14f3eb100cdb69c6ff953e1096c5a67f5a6d06233a295e52bc416026")
        self.longpoll = VkLongPoll(self.vk_session)
        self.vk = self.vk_session.get_api()


    def random_id(self):
        self.randoms = 0
        self.randoms += random.randint(0, 1000000000000)
        return self.randoms

    def glossing(self):
        # Создаем список студентов и их рейтинга
        studentss = dict()
        # битва бомжей
        # 1 фамилия 2 рейтин 3 комент 4 средний рейтинг 5 айди
        studentss['1'] = ['Агаркова', 0, " ", 0, 310410918]
        studentss['2'] = ['Ажинов', 0, " ", 0, 263542561]
        studentss['3'] = ['Акимов', 0, " ", 0, 262668821]
        studentss['4'] = ['Алиев', 0, " ", 0, 469677495]
        studentss['5'] = ['Антонян', 0, " ", 0, 556745169]
        studentss['6'] = ['Барабанов', 0, " ", 0, 198092718]
        studentss['7'] = ['Грибенников', 0, " ", 0, 214078701]
        studentss['8'] = ['Дворниченко', 0, " ", 0, 296469265]
        studentss['9'] = ['Джамалдинов', 0, " ", 0, 487620053]
        studentss['10'] = ['Добряков', 0, " ", 0, 510998697]
        studentss['11'] = ['Замореев', 0, " ", 0, 293470132]
        studentss['12'] = ['Коваленко', 0, " ", 0, 137283601]
        studentss['13'] = ['Коренев', 0, " ", 0, 556295439]
        studentss['14'] = ['Кривчиков', 0, " ", 0, 191420134]
        studentss['15'] = ['Кузьминых', 0, " ", 0, 318022133]
        studentss['16'] = ['Леонов', 0, " ", 0, 212162053]
        studentss['17'] = ['Линник', 0, " ", 0, 221579176]
        studentss['18'] = ['Маховиков', 0, " ", 0, 206261124]
        studentss['19'] = ['Михайлова', 0, " ", 0, 147082979]
        studentss['20'] = ['Нестеренко', 0, " ", 0, 226066141]
        studentss['21'] = ['Пасынков', 0, " ", 0, 281531128]
        studentss['22'] = ['Руппель', 0, " ", 0, 306096404]
        studentss['23'] = ['Сафронов', 0, " ", 0, 226905627]
        studentss['24'] = ['Чувак', 0, " ", 0, 000000000]
        print("Собрали мы армию бомжей. 300 бомжей-лихочей")
        s = True
        while s:
            print("а я тут работаю азазазазазазза")
            for event in self.longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    if event.text.lower() == 'назад':  # Если пользователь вводит это значение, то
                        self.vk.messages.send(  # Его выкидывают в начальные кнопки
                            user_id=event.user_id,  # Для выбора другой операци
                            message="Не стоило тебе сюда заходить",
                            keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                            random_id=self.random_id()
                        )
                        print("Тут нас накрыи дилдаом")
                        s = False
                        return "*боевая музыка из скайрима"

                    elif event.text.lower() == 'узнать рейтинг':
                        for event in self.longpoll.listen():
                            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                number = event.text.lower()
                                self.vk.messages.send(  # Его выкидывают в начальные кнопки
                                    user_id=event.user_id,  # Для выбора другой операци
                                    message="Получи",
                                    keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                                    random_id=self.random_id
                                )
                                s = students.Students(number, event.user_id)
                                return s.ratingg()



                    else:
                        print("Были битвы. Грязные битвы")
                        # # Получаем от пользователя номер студента и его оценку
                        # number = event.text.lower()  # Номер студента
                        # try:
                        #     number = int(number)
                        # except ValueError :
                        #     return "Уверен, в следующий раз у тебя получится написать целую цифрику "
                        number = event.text.lower()
                        for events in self.longpoll.listen():
                            if events.type == VkEventType.MESSAGE_NEW and event.to_me:
                                gloss = events.text.lower()  # Оценка для студента
                                print("Пердык")
                                s = students.Students(number, gloss, event.user_id, studentss)
                                print("Саня Варвар")
                                s.student_info()
                                print("Пердук")
                                print(s)
                                return s.student_info()  # Возвращаем значение из функции
                            # student_info из файла students

    # Функция, чтобы можно было отправлять сообщение одно и тому же
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

    def mess(self):
        while True:
            otvet1 = ['Тыкай по кнопочкам', 'Сейчас разозлюсь']
            otvet2 = ['Че?', 'А?']
            i = 0
            k = 1
            for event in self.longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    # пусть пока будет так но потом нужно будет это норм сделать
                    # может быть стоит это потом вынести в отдельную фу-цию

                    if event.text.lower() == 'расписание':  # Нижний регистр.
                        self.vk.messages.send(
                            user_id=event.user_id,
                            message=self.fuck,
                            keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                            random_id=self.random_id()
                        )
                        k = 2
                    elif event.text.lower() == 'неделя':
                        self.vk.messages.send(
                            user_id=event.user_id,
                            message=week.Week(self.fuck),
                            keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                            random_id=self.random_id()
                        )
                        k = 2
                    elif event.text.lower() == 'другие команды':
                        self.vk.messages.send(
                            user_id=event.user_id,
                            message='Ты взломать мою жепку',
                            keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                            random_id=self.random_id()
                        )
                        k = 2

                    elif event.text.lower() == "события":
                        self.vk.messages.send(
                            user_id=event.user_id,
                            message=self.open_read_file("events.txt"),
                            keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                            random_id=self.random_id()
                        )
                        k = 2

                    elif event.text.lower() == 'голосование':
                        print("Тут накала Сашка")
                        self.vk.messages.send(
                            user_id=event.user_id,
                            message="Введи превым целым числом номер нужного студента " + "\n" + "следующее число - оценка , котору ты бы ему хотел поставить ( от 1 до 5) " + '\n' + self.open_read_file(
                                "students_numbers"),  # Вывод сообщения о входе в режим голосования.
                            keyboard=open("glossing_keyboard.json", "r", encoding="UTF-8").read(),
                            # Вызываем главиатуру голосования.
                            random_id=self.random_id()
                        )
                        print("А тут Олег")
                        self.vk.messages.send(
                            user_id=event.user_id,
                            message=self.glossing(),
                            # Вызываем метод "голосование"
                            keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                            random_id=self.random_id()
                        )
                        k = 3
                    elif event.text.lower() == "рассылка":
                        if event.user_id == 263542561 or 293470132:
                            self.vk.messages.send(
                                user_id=event.user_id,
                                message="вставайте, зови мужиком, работаем" + mailing.mailing(self.vk_session),
                                keyboard=open("glossing_keyboard.json", "r", encoding="UTF-8").read(),
                                random_id=self.random_id()
                            )
                        k = 3
                    else:
                        if k != 3:
                            if i < 4:
                                self.vk.messages.send(
                                    user_id=event.user_id,
                                    message=random.choice(otvet1),
                                    keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                                    random_id=self.random_id()
                                )
                                i += 1
                            else:
                                self.vk.messages.send(
                                    user_id=event.user_id,
                                    message=random.choice(otvet2),
                                    keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                                    random_id=self.random_id()
                                )
            print("айди юзера равен = " + str(event.user_id))


Message().mess()