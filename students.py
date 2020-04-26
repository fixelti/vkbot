# Создаем список студентов и их рейтинга
students = dict()
# битва бомжей
students['1'] = ['Агаркова', 0, " ", 0]
students['2'] = ['Ажинов', 0, " ", 0]
students['3'] = ['Акимов', 0, " ", 0]
students['4'] = ['Алиев', 0, " ",  0]
students['5'] = ['Антонян', 0, " ", 0]
students['6'] = ['Барабанов', 0, " ", 0]
students['7'] = ['Грибенников', 0, " ", 0]
students['8'] = ['Дворниченко', 0, " ", 0]
students['9'] = ['Джамалдинов', 0, " ", 0]
students['10'] = ['Добряков', 0, " ", 0]
students['11'] = ['Замореев', 0, " ", 0]
students['12'] = ['Коваленко', 0, " ", 0]
students['13'] = ['Коренев', 0, " ", 0]
students['14'] = ['Кривчиков', 0, " ", 0]
students['15'] = ['Кузьминых', 0, " ", 0]
students['16'] = ['Леонов', 0, " ", 0]
students['17'] = ['Линник', 0, " ", 0]
students['18'] = ['Маховиков', 0, " ", 0]
students['19'] = ['Нестеренко', 0, " ", 0]
students['20'] = ['Пасынков', 0, " ", 0]
students['21'] = ['Руппель', 0, " ", 0]
students['22'] = ['Сафронов', 0, " ", 0]
students['23'] = ['Чувак', 0, " ", 0]


def student_id(number, user_id):
    i = 0
    lines = ""
    while i < len(students):
        admin_id_1 = '293470132'
        admin_id_2 = "263542561"
        if number in students:

            file_name = students[number]
            event = open("C:\\Program\\vkbot\\student_id\\" + file_name[0] + ".txt", encoding='utf8',)

            for line in event:
                lines += line

            if admin_id_1 in lines or admin_id_2 in lines :
                return True

            elif str(user_id) in lines:
                return False

            else:

                events = open(file_name[0] + ".txt", 'w')
                events.write(lines + str(user_id) + '\n')
                event.close()
                return True


# отвечает на ввод числа (норм это число или не проходит по критериям)
def student_info(number, gloss, user_id):
    i = 1
    while i < 25:
        if (number in students) and ((float(gloss) >= 1) and (float(gloss) <= 5)):  # Проверка на вход в диапазон оценок
            if student_id(number, user_id):
                rating = students[number]
                rating[1] += float(gloss)
                rating[3] += 1
                return students[number]
                i += 1
            else:
                return "Ты борзый самый?"
        else:
            return "Неправильное число"


def ratingg(number):
    i = 0

    while i <= len(students):
        i += 1
        if number in students:
            rating_student = students[number]
            sredniy_rating = rating_student[1] / rating_student[3]
            return sredniy_rating
        else:
            return "Error"
