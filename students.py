# Создаем список студентов и их рейтинга
students = dict()
# битва бомжей
# 1 фамилия 2 рейтин 3 комент 4 средний рейтинг 5 айди  
students['1'] = ['Агаркова',0, " ",0,310410918]
students['2'] = ['Ажинов',0, " ",0,263542561]
students['3'] = ['Акимов',0, " ",0,262668821]
students['4'] = ['Алиев',0, " ",0,469677495]
students['5'] = ['Антонян',0, " ",0,556745169]
students['6'] = ['Барабанов',0, " ",0,198092718]
students['7'] = ['Грибенников',0, " ",0,214078701]
students['8'] = ['Дворниченко',0, " ",0,296469265]
students['9'] = ['Джамалдинов',0, " ",0,487620053]
students['10'] = ['Добряков',0, " ",0,510998697]
students['11'] = ['Замореев',0, " ",0 ,293470132]
students['12'] = ['Коваленко',0, " ",0,137283601]
students['13'] = ['Коренев',0, " ", 0,556295439]
students['14'] = ['Кривчиков',0, " ",0,191420134]
students['15'] = ['Кузьминых',0, " ",0,318022133]
students['16'] = ['Леонов',0, " ", 0,212162053]
students['17'] = ['Линник',0, " ", 0,221579176]
students['18'] = ['Маховиков',0, " ",0,206261124]
students['19'] = ['Михайлова',0, " ",0,147082979]
students['20'] = ['Нестеренко',0, " ",0 ,226066141]
students['21'] = ['Пасынков',0, " ",0,281531128]
students['22'] = ['Руппель',0, " ",0 ,306096404]
students['23'] = ['Сафронов',0, " ",0,226905627]
students['24'] = ['Чувак',0, " ",0, 000000000]

def student_id(number, user_id):
    i = 0
    lines = ""
    while i < len(students):
        admin_id_1 = '293470132'
        admin_id_2 = "263542561"
        if number in students:

            file_name = students[number]
            # созадется некоторый масив 
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


def ratingg(number , user_id):
    i = 1
    
    while i <= len(students) : 
        peremenay = str(students[ str(i) ])
        peremenay1 = peremenay[peremenay.rfind(',') + 2:len (peremenay) - 1]
        print('permenay = '+ peremenay)
        if str(user_id) == peremenay1 : 
                peremenay2 = peremenay[peremenay.find(',') + 1:] 
                peremenay2 = peremenay2[:peremenay2.find(',') ]
                print("")
                return peremenay2
               
        i += 1
    if i > len(students) : 
        return "Нема тебя в списках, чувачок..."
    # while i <= len(students):
    #     i += 1
    #     if user_id in students:
    #         rating_student = students[number]
    #         sredniy_rating = rating_student[1] / rating_student[3]
    #         return sredniy_rating
    #     else:
    #         return "Error"
