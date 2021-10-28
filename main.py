import sqlite3

class DB():
    def __init__(self):
        self.conn = sqlite3.connect('Student_system_managment.db')
        self.c = self.conn.cursor()
        self.c.execute("PRAGMA foreign_keys = ON")

    ### queries for students ###    
    def add_student_to_db(self, first_name, last_name, age, phone='', email=''):
        self.c.execute("INSERT INTO student(first_name, last_name, age, phone, email) VALUES (?,?,?,?,?)",
        (first_name, last_name, age, phone, email))
        self.conn.commit()

    def delete_student_from_db(self):
        delete = input('Wybierz id studenta, którego chcesz usunąć: ')
        self.c.execute("DELETE FROM student WHERE id = ?", (delete))
        self.conn.commit()

    def print_info_about_students(self):
        self.c.execute("SELECT * FROM student")
        items = self.c.fetchall()
        print('Studenci')
        print('-'*50)
        for item in items:
            print(item)

    ### queries for grade_course ###
    def add_grade_course_to_db(self, kierunek):
        self.c.execute("INSERT INTO grade_course(name) VALUES (?)", (kierunek, ))
        self.conn.commit()

    def print_grade_courses(self):
        self.c.execute("SELECT * FROM grade_course")
        items = self.c.fetchall()
        print('Studenci')
        print('-'*50)
        for item in items:
            print(item)

    def delete_grade_course(self, id):
        self.c.execute("DELETE FROM grade_course WHERE id = ?", (id, ))

    ### queries for course ###
    def add_course_to_db(self, przedmiot, g_c_id):
        self.c.execute("INSERT INTO course(name, grade_course_id) VALUES (?, ?)", (przedmiot, g_c_id))
        self.conn.commit()

    def print_courses(self):
        self.c.execute("SELECT * FROM course")
        items = self.c.fetchall()
        print('Studenci')
        print('-'*50)
        for item in items:
            print(item)

    # def print_courses(self):
    #     self.c.execute("SELECT grade_course.name, course.name FROM grade_course INNER JOIN course ON grade_course.id = course.grade_course_id")
    #     items = self.c.fetchall()
    #     print('Przedmioty')
    #     print('-'*50)
    #     for item in items:
    #         print(item)

    def delete_course(self, id):
        self.c.execute("DELETE FROM course WHERE id = ?", (id, ))

    def commit_db(self):
        self.conn.commit()

    def close_db(self):
        self.conn.close()


class Main():
    def __init__(self):
        self.db = DB()
        while True:
            print("-"*50)
            print("Dziennik zarządzania studentami")
            print("1. Dodaj studenta")
            print("2. Usuń studenta")
            print("3. Wypisz studentów")
            print("4. Dodaj kierunek studiów")
            print("5. Wypisz kierunki studiów")
            print("6. Usuń kierunek studiów")
            print("7. Dodaj przedmiot")
            print("8. Wypisz przedmioty")
            print("9. Usuń przedmiot")
            print("q. Wyjdź")
            print("-"*50)
            x = input("Podaj opcje: ")
            if x == "1":
                first_name = input("Wpisz imie ucznia, którego chcesz utworzyć: ")
                last_name = input("Wpisz nazwisko ucznia, którego chcesz utworzyć: ")
                age = input("Wpisz wiek ucznia, którego chcesz utworzyć: ")
                phone = input("Wpisz numer telefonu ucznia, którego chcesz utworzyć: ")
                email = input("Wpisz e-mail ucznia, którego chcesz utworzyć: ")
                self.db.add_student_to_db(first_name, last_name, age, phone, email)
                self.db.commit_db()
            elif x == "2":
                self.db.delete_student_from_db()
                self.db.commit_db()
            elif x == "3":
                self.db.print_info_about_students()
            elif x == "4":
                kierunek = input("Wpisz nazwę nowego kierunku: ")
                self.db.add_grade_course_to_db(kierunek)
                self.db.commit_db()
            elif x == "5":
                self.db.print_grade_courses()
            elif x == "6":
                id = input("Wbierz id kierunku, którego chcesz usunąć: ")
                self.db.delete_grade_course(id)
                self.db.commit_db()
            elif x == "7":
                g_c_id = input("Podaj id kierunku dla którego chcesz dodać przedmiot: ")
                przedmiot = input("Podaj nazwe przedmiotu: ")
                self.db.add_course_to_db(przedmiot, g_c_id)
            elif x == "8":
                self.db.print_courses()
            elif x == "9":
                id = input("Wbierz id przedmiotu, którego chcesz usunąć: ")
                self.db.delete_course(id)
                self.db.commit_db()
            elif x == "q":
                break

    def __del__(self):
        self.db.close_db()
        print('Zamknięcie programu')

main = Main()
main