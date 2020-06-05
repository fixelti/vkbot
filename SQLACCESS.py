import sqlite3


class Sqlaccess(object):

    def __init__(self, name_students, gloss, user_id):
        self.name_students = name_students
        self.gloss = gloss
        self.user_id = user_id

    global db
    db = sqlite3.connect('student.db')

    global sql
    sql = db.cursor()

    # Создаем в БД определенный ячейки
    sql.execute("""CREATE TABLE IF NOT EXISTS users (
        name TEXT,
        id INT,
        gloss FLOAT, 
        count INT
    )""")


    """
    Стрктура БД(Как понял ее я)
    
    name = замореев | name = ажинов
    id = 123        | id = 124
    gloss = 5       | gloss = 5
    count = 1       | count = 1
    ---------------------------------
    Как я понял, елси пишем что-то типа " f"SELECT name FROM users WHERE NAME = '{user_name}'" "
    То мы смотрим значение ячики, которая относится к определенному name.
    """



    db.commit() # Сохраняем БД

    # Метод для регестрации нового пользователя
    def reg(self):
        user_name = input('Add name: ')
        user_id = input('Add id: ')

        # Читаем из БД значение ячейки name
        sql.execute(f"SELECT name FROM users WHERE NAME = '{user_name}'")

        # Если ячейки с таким name не найденно. Начинаем регестрация нового пользователя
        if sql.fetchone() is None:
            # Заносим только user_name и user_id. Оценка и кол-во проголовавших буду вводится в другом месте.
            sql.execute(f"INSERT INTO users VALUES (?, ?, ?, ?)", (user_name, user_id, 0, 0))
            db.commit() # Сохраняем изменения в БД
            print("Пользователь занесен в таблицу")
        else:
            print("Такой пользователь уже существует")

        # Читаем значения ВСЕХ ячеек. После выводим их
        for value in sql.execute("SELECT * FROM users"):
            print(value)

    # Метод, в котором производится пароцесс голосование
    def glossing(self):

        # Читаем значения ячеек с оценко и присв. это значение переменной.
        for i in sql.execute(f"SELECT gloss FROM users WHERE name = '{self.name_students}'"):
            reiting = float(i[0])

        # Тоже самое делаем и с кол-вом проголосовавших
        for i in sql.execute(f"SELECT count FROM users WHERE name = '{self.name_students}'"):
            new_count = int(i[0])

        # Если методв student_id возвращает True, то метод будет выполнятся
        if self.stydent_id(self.name_students, self.user_id):

            sql.execute(f"SELECT name FROM users WHERE name = '{self.name_students}'")
            print(self.name_students)

            # Изменяем значние ячеки gloss
            sql.execute(f"UPDATE users SET gloss = '{reiting + float(self.gloss)}' WHERE name = '{self.name_students}'")
            db.commit()

            # Изменяем значние ячеки count
            sql.execute(f"UPDATE users SET count = '{new_count + 1}' WHERE name = '{self.name_students}'")
            db.commit()

            # Возвращаем значение всех ячеек name.
            for value in sql.execute(f"SELECT * FROM users WHERE name = '{self.name_students}'"):
                return value
        else:
            return "Вы уже голосовали за этого человека"

    # Метод для определение сред. оценки.
    def sredreit(self):
        for i in sql.execute(f"SELECT gloss FROM users WHERE name = '{self.name_students}'"):
            reiting = float(i[0])

        for i in sql.execute(f"SELECT count FROM users WHERE name = '{self.name_students}'"):
            new_count = int(i[0])

        return reiting / new_count

    # Метод для открытия файлов, в которые записуются id проголовавших
    def open_file(self):
        event = open("C:\\Program\\vkbot\\" + self.name_students + ".txt", encoding='utf8')

        lines = ""
        for line in event:
            lines += line
        return lines

    # Метод проверяте есть ли id в файле. Если есть возвр. False. А елси нет - возвр. True и записывает id в файл.
    def stydent_id(self, name_students, user_id):

        admin_id_1 = '293470132'
        admin_id_2 = '263542561'

        a = 1

        for i in sql.execute(f"SELECT id FROM users WHERE name = '{self.name_students}'"):
            new_id = int(i[0])


        while a < 25:
            # Проверят соответствие id к admin_id
            if (admin_id_1 in str(user_id)) or (admin_id_2 in str(user_id)):
                return True

            # Если id уже записано в файл
            elif str(new_id) in open_file(number):
                return False

            # Если id не записан в файл. Записуем его в файл.
            else:
                events = open(number + ".txt", 'w')
                events.write(open_file(number) + str(user_id) + '\n')
                return True

            a += 1
