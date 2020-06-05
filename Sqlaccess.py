import sqlite3


class Sqlaccess(object):

    def __init__(self, number, gloss, user_id):
        self.number = number
        self.gloss = gloss
        self.user_id = user_id


    global db
    db = sqlite3.connect('student.db')

    global sql
    sql = db.cursor()

    sql.execute("""CREATE TABLE IF NOT EXISTS users (
        name TEXT,
        id INT,
        gloss FLOAT, 
        count INT
    )""")

    db.commit()

    def reg(self):
        user_name = input('Add name: ')
        user_id = input('Add id: ')

        sql.execute(f"SELECT name FROM users WHERE NAME = '{user_name}'")

        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO users VALUES (?, ?, ?, ?)", (user_name, user_id, 0, 0))
            db.commit()
            print("Пользователь занесен в таблицу")
        else:
            print("Такой пользователь уже существует")

        for value in sql.execute("SELECT * FROM users"):
            print(value)

    def gloss(self, gloss, number, user_id):
        # user_name = input("Add name gloss: ")
        # user_gloss = float(input("Add gloss: "))

        for i in sql.execute(f"SELECT gloss FROM users WHERE name = '{self.number}'"):
            reiting = float(i[0])

        for i in sql.execute(f"SELECT count FROM users WHERE name = '{self.number}'"):
            new_count = int(i[0])

        if self.stydent_id(user_id):
            sql.execute(f"SELECT name FROM users WHERE name = '{self.number}'")
            print(self.number)
            if sql.fetchone() is None:
                print(
                    "Такого пользователя не существует. Проверти правильность написания или обратитесь в тех. поддержку")
            else:
                sql.execute(f"UPDATE users SET gloss = '{reiting + float(self.gloss)}' WHERE name = '{self.number}'")
                db.commit()
                sql.execute(f"UPDATE users SET count = '{new_count + 1}' WHERE name = '{self.number}'")
                db.commit()
                for value in sql.execute(f"SELECT * FROM users WHERE name = '{self.number}'"):
                    return value
        else:
            return "Вы уже голосовали за этого человека"

    def sredreit(self):
        for i in sql.execute(f"SELECT gloss FROM users WHERE name = '{self.number}'"):
            reiting = float(i[0])

        for i in sql.execute(f"SELECT count FROM users WHERE name = '{self.number}'"):
            new_count = int(i[0])

        return reiting / new_count

    def open_file(self):
        event = open("C:\\Program\\vkbot\\" + self.number + ".txt", encoding='utf8')

        lines = ""
        for line in event:
            lines += line
        return lines

    def stydent_id(self, number, user_id):
        print("1 work")
        for i in sql.execute(f"SELECT id FROM users WHERE name = '{self.number}'"):
            new_id = int(i[0])

        print("2 work")

        admin_id_1 = '293470132'  # '293470132'
        admin_id_2 = '263542561'

        i = 1

        while i < 25:

            if (admin_id_1 in str(user_id)) or (admin_id_2 in str(user_id)):
                print("3 work")
                return True
            elif str(new_id) in open_file(number):
                print("4 work")
                return False
            else:
                events = open(number + ".txt", 'w')
                events.write(open_file(number) + str(user_id) + '\n')
                #            event.close()
                print("5 work")
                return True

            i += 1
