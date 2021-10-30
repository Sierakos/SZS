from db_connect import Sqlite
import re

class Controller():
    __connection=None
    __curr=None

    def __init__(self):
        self.__connection = Sqlite.connect(self)
        self.__curr = self.__connection.cursor()

    ### kod w funkcji poniżej tymczasowy
    def Form(self, student):
        if self.__isvalidForm(student):
            if self.__isvalidEmail(student):
                # To na pewno wymaga modyfikacji
                try:
                    student.setAge(int(student.getAge()))
                    if student.getAge() > 0:
                        self.__valid(student)
                        return True
                    else:
                        student.setMessage("Wiek musi być większy od zera")
                except:
                    student.setMessage("Wiek musi być liczbą całkowitą")  
                    return False
            else:
                student.setMessage("Niepoprawny e-mail: proszę wpisać e-mail według wzoru 'email@email.com' ")
                return False
        else:
            student.setMessage("Wpisz imie, nazwisko i wiek")
            return False

    # validacje - Sprawdza czy podczas dodawania studenta wprowadzamy poprawne dane
    def __isvalidForm(self, student):
        if student.getFname() != "" and student.getLname() != "" and student.getAge != 0: 
            return True
        else:
            return False

    def __isvalidEmail(self, student):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if student.getEmail() == "":
            return True
        else:
            if (re.fullmatch(regex, student.getEmail())):
                return True
            else:
                return False

    def __valid(self, student):
        student.setMessage("Dane poprawne")
        # return True

    # def getStudents(self):
    #     students = self.__curr.execute("SELECT * FROM student")
    #     for student in students:
    #         print(student)

    ### Zapytania dla studenta ###    
    def add_student_to_db(self, student, first_name, last_name, age=0, phone="", email=''):
        if student.getMessage() == "Dane poprawne":
            print("DODAWANIE DO BAZY")
            self.__curr.execute("INSERT INTO student(first_name, last_name, age, phone, email) VALUES (?,?,?,?,?)", (first_name, last_name, age, phone, email))
            Sqlite.commit(self, self.__connection)
        else:
            print("NIE DODAWANIE DO BAZY")

    def delete_student_from_db(self):
        delete = input('Wybierz id studenta, którego chcesz usunąć: ')
        self.__curr.execute("DELETE FROM student WHERE id = ?", (delete, ))
        Sqlite.commit(self, self.__connection)

    def print_info_about_students(self):
        self.__curr.execute("SELECT * FROM student")
        items = self.__curr.fetchall()
        print('Studenci')
        print('-'*50)
        for item in items:
            print(item)

    ### queries for grade_course ###
    def add_grade_course_to_db(self, kierunek):
        self.__curr.execute("INSERT INTO grade_course(name) VALUES (?)", (kierunek, ))
        Sqlite.commit(self, self.__connection)

    def print_grade_courses(self):
        self.__curr.execute("SELECT * FROM grade_course")
        items = self.__curr.fetchall()
        print('Studenci')
        print('-'*50)
        for item in items:
            print(item)

    def delete_grade_course(self, id):
        self.__curr.execute("DELETE FROM grade_course WHERE id = ?", (id, ))
        Sqlite.commit(self, self.__connection)

    ### queries for course ###
    def add_course_to_db(self, przedmiot, g_c_id):
        self.__curr.execute("INSERT INTO course(name, grade_course_id) VALUES (?, ?)", (przedmiot, g_c_id))
        Sqlite.commit(self, self.__connection)

    def print_courses(self):
        self.__curr.execute("SELECT * FROM course")
        items = self.__curr.fetchall()
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
        self.__curr.execute("DELETE FROM course WHERE id = ?", (id, ))
        Sqlite.commit(self, self.__connection)

    def close_db(self):
        Sqlite.close(self, self.__connection)