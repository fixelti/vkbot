class Students(object):

    def __init__(self, number, gloss, user_id, students):
        self.number = number
        self.gloss = gloss
        self.user_id = user_id
        self.students = students

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

        print("Второй пол лихачей прогирал игривым собакам верховного клыка и кости")
        i = 1
        while i < 25:
            print("Работяги пытаются работать")
            if (self.number in self.students) and (float(self.gloss) >= 1) and (
                    float(self.gloss) <= 5):  # Проверка на вход в диапазон оценок
                if self.student_id(self.number, self.user_id):
                    rating = self.students[self.number]
                    rating[1] += float(self.gloss)
                    rating[3] += 1
                    i += 1
                    print("Е")
                    return self.students[self.number]

                else:
                    return "Ты борзый самый?"
            else:
                return "Неправильное число"

    def ratingg(self, number, user_id):
        i = 1

        while i <= len(self.students):
            i += 1
            if number in self.students:
                rating_student = self.students[number]
                sredniy_rating = rating_student[1] / rating_student[3]
                return sredniy_rating
            else:
                return "Error"

    #    while i <= len(students) :
    # peremenay = str(students[ str(i) ])
    # peremenay1 = peremenay[peremenay.rfind(',') + 2:len (peremenay) - 1]
    # print('permenay = '+ peremenay)
    # if str(user_id) == peremenay1 :
    #         peremenay2 = peremenay[peremenay.find(',') + 1:]
    #         peremenay2 = peremenay2[:peremenay2.find(',') ]
    #         print("")
    #         return peremenay2

    # if i > len(students) :
    #     return "Нема тебя в списках, чувачок..."
    # while i <= len(students):
    #     i += 1
    #     if user_id in students:
    #         rating_student = students[number]
    #         sredniy_rating = rating_student[1] / rating_student[3]
    #         return sredniy_rating
    #     else:
    #         return "Error"
