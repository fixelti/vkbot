from vk_api.longpoll import VkEventType, VkLongPoll
import students
import random


def random_id():
    Random = 0
    Random += random.randint(0, 1000000000000)
    return Random


# эта фу-ция для меню "голосование"
# через нее потом вызывается файл students в котором потом и записываюся балы 
def glossing(vk_session, fuck):
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
                        random_id=random_id( )
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
                                random_id=random_id()
                            )
                            return students.ratingg(number)



                else:
                    # Получаем от пользователя номер студента и его оценку
                    number = event.text.lower()  # Номер студента
                    try:
                        number = int(number)
                    except ValueError :
                        return "Уверен, в следующий раз у тебя получится написать целую цифрику "
                    for events in longpoll.listen():
                        if events.type == VkEventType.MESSAGE_NEW and event.to_me:
                            gloss = events.text.lower()  # Оценка для студента
                            return students.student_info(number, gloss, event.user_id)  # Возвращаем значение из функции
                        # student_info из файла students
