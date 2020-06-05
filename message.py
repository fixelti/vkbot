import random
from vk_api.longpoll import VkLongPoll, VkEventType
import week
import pars
import vk_api
import mailing
<<<<<<< HEAD
import students
=======
>>>>>>> e999d5373e65547230a447a523259e1b6c3b1fb5
import SQLACCESS


class Message(object):

    def __init__(self):
        self.fuck = pars.Parse(pars.Site('https://edu.donstu.ru/Rasp/Rasp.aspx?group=32353&sem=2'))
        self.vk_session = vk_api.VkApi(
            token="4e3f2af11078b879a7a574564ca5d14f3eb100cdb69c6ff953e1096c5a67f5a6d06233a295e52bc416026")
        self.longpoll = VkLongPoll(self.vk_session)
        self.vk = self.vk_session.get_api()


    # Функция для передачи случайного числа.
    def random_id(self):
        self.randoms = 0
        self.randoms += random.randint(0, 1000000000000)
        return self.randoms



    def glossing_throwing(self):
        # Принимаем ввод пользователя и по переправляем к определенному методу.
        s = True
        while s:
            for event in self.longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    try:
                        if event.text.lower() == 'назад':  # Если пользователь вводит это значение, то
                            self.vk.messages.send(  # Его выкидывают в начальные кнопки
                                user_id=event.user_id,  # Для выбора другой операци
                                message="Не стоило тебе сюда заходить",
                                keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                                random_id=self.random_id()
                            )
                            s = False
                            return "*боевая музыка из скайрима"
                        elif event.text.lower() == 'узнать рейтинг':
                            for event in self.longpoll.listen():
                                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                    name_students = event.text
                                    self.vk.messages.send(
                                        user_id=event.user_id,
                                        message="Получи",
                                        keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                                        random_id=self.random_id()
                                    )
                                    a = SQLACCESS.Sqlaccess(name_students, 0, event.user_id)
                                    return a.sredreit()
                        else:
                            name_students = event.text.lower() # Фамилия студнета
                            for events in self.longpoll.listen():
                                if events.type == VkEventType.MESSAGE_NEW and event.to_me:
                                    gloss = events.text.lower()  # Оценка для студента
                                    if ( float(gloss) >= 1 ) and ( float(gloss) <= 5 ):
                                        a = SQLACCESS.Sqlaccess(name_students, gloss, events.user_id) # Получаем экземпляр класса
                                        return a.glossing() # Возвращаем значение из функции(Вызывая метод из экземпляра класса)
                                    else:
                                        return "Оценка низкая или высокая"
                    # Проверка на не существуемость пользователя.
                    except UnboundLocalError:
                        self.vk.messages.send(
                            user_id=event.user_id,
                            message="Такого пользователя не существует. Проверти правильность написания или обратитесь в тех. поддержку",
                            random_id=self.random_id()
                        )
                    # Проверка на правильность ввода оценки(должны быть тольцо цифры)
                    except ValueError:
                        print("Твоя оценка подозрительная. Может это буква, А НЕ ЧИСЛО?")
                        self.vk.messages.send(
                            user_id=event.user_id,
                            message="Твоя оценка подозрительная. Может это буква, А НЕ ЧИСЛО?",
                            random_id=self.random_id()
                        )
<<<<<<< HEAD
                        s = False
                        return "*боевая музыка из скайрима"

                    elif event.text.lower() == 'узнать рейтинг':
                        for event in self.longpoll.listen():
                            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                number = event.text
                                self.vk.messages.send(  # Его выкидывают в начальные кнопки
                                    user_id=event.user_id,  # Для выбора другой операци
                                    message="Получи",
                                    keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                                    random_id=self.random_id()
                                )
                                d = 1
                                return SQLACCESS.sredreit(number, d, events.user_id)



                    else:
                        number = event.text.lower()
                        for events in self.longpoll.listen():
                            if events.type == VkEventType.MESSAGE_NEW and event.to_me:
                                gloss = events.text.lower()  # Оценка для студента
                                if ( float(gloss) >= 1 ) and ( float(gloss) <= 5 ):
                                    print("1 Этап работает")
                                    a = SQLACCESS.Sqlaccess
                                    return s.gloss(number, gloss, events.user_id) # Возвращаем значение из функции

                                else:
                                    return "Оценка низкая или высокая"
=======
>>>>>>> e999d5373e65547230a447a523259e1b6c3b1fb5

    # Функция открытия и чтения одного из двух файлом.
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

    # Основная функция. По пользовательскому вводу переводит его в другие методы программы.
    def mess(self):
        while True:
            otvet1 = ['Тыкай по кнопочкам', 'Сейчас разозлюсь']
            otvet2 = ['Че?', 'А?']
            i = 0 # Создаем данную переменную, чтобы выводить случайный доп.ответ.
            k = 1 # Создаем данную переменную, чтобы не выводились доп.ответы, когда они не нужны(Костыль!)
            for event in self.longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
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
                            message='Пока нет  других команд',
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
                        self.vk.messages.send(
                            user_id=event.user_id,
                            message="Введи превым целым числом номер нужного студента " + "\n" + "следующее число - оценка , котору ты бы ему хотел поставить ( от 1 до 5) " + '\n' + self.open_read_file(
                                "students_numbers"),  # Вывод сообщения о входе в режим голосования.
                            keyboard=open("glossing_keyboard.json", "r", encoding="UTF-8").read(),
                            # Вызываем главиатуру голосования.
                            random_id=self.random_id()
                        )
                        self.vk.messages.send(
                            user_id=event.user_id,
                            message=self.glossing_throwing(),
                            # Вызываем метод "голосование"
                            keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                            random_id=self.random_id()
                        )
                        k = 3
                    elif event.text.lower() == "рассылка":
                        self.vk.messages.send(
                            user_id=event.user_id,
                            message= mailing.Mailing.mailing(self),
                            keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
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
