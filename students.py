class Students(object):

    def __init__(self, number, gloss, user_id):
        self.number = number
        self.gloss = gloss
        self.user_id = user_id

    studentss = dict()
    # 1 фамилия 2 рейтин 3 комент 4 средний рейтинг 5 айди
    studentss['1'] = ['Агаркова', 0, "гигобайтик", 0, 310410918]
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

    def student_id(self, number, user_id):
        i = 0
        lines = ""
        while i < len(self.students):
            admin_id_1 = '293470132'
            admin_id_2 = "263542561"
            if number in self.students:

                file_name = self.students[number]
                # созадется некоторый масив
                event = open("C:\\Program\\vkbot\\student_id\\" + file_name[0] + ".txt", encoding='utf8', )

                for line in event:
                    lines += line

                if admin_id_1 in lines or admin_id_2 in lines:
                    return True

                elif str(user_id) in lines:
                    return False

                else:

                    events = open(file_name[0] + ".txt", 'w')
                    events.write(lines + str(user_id) + '\n')
                    event.close()
                    return True

    # отвечает на ввод числа (норм это число или не проходит по критериям)
    def student_info(self):

        i = 1
        while i < 25:
            if (self.number in self.studentss) and (float(self.gloss) >= 1) and (
                    float(self.gloss) <= 5):  # Проверка на вход в диапазон оценок
                if self.student_id(self.number, self.user_id):
                    self.rating = self.studentss[self.number]
                    self.rating[1] += float(self.gloss)
                    self.rating[3] += 1
                    i += 1
                    return self.studentss[self.number]

                else:
                    return "Ты борзый самый?"
            else:
                return "Неправильное число"

    def ratingg(self):
        i = 1

        while i <= len(self.studentss):
            i += 1
            if self.number in self.studentss:
                self.rating_student = self.studentss[self.number]
                print(self.studentss[self.number])
                self.sredniy_rating = self.rating_student[1] / self.rating_student[3]
                return self.sredniy_rating
            else:
                return "Error"
