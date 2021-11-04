from db_connect import Sqlite
import re
import pandas as pd
# ctr
class Controller():
    __connection=None
    __curr=None

    def __init__(self):
        self.__connection = Sqlite.connect(self)
        self.__curr = self.__connection.cursor()

    ### kod w funkcji poniżej tymczasowy
    def studentForm(self, student):
        if self.__isvalidForm(student):
            if self.__isvalidEmail(student):
                if self.__isvalidAge(student):
                    if student.getAge() > 0:
                        if self.__isvalidPhone(student):
                            self.__valid(student)
                            return True
                        else:
                            student.setMessage("Numer telefonu musi być tylko liczbą")
                            return False
                    else:
                        student.setMessage("Wiek musi być większy od zera")
                        return False
                else:
                    student.setMessage("Wiek musi być liczbą całkowitą")  
                    return False
            else:
                student.setMessage("Niepoprawny e-mail: proszę wpisać e-mail według wzoru 'email@email.com' ")
                return False
        else:
            student.setMessage("Wpisz imie, nazwisko i wiek")
            return False

    def courseForm(self, course):
        if self.__isvalidG_courseId(course):
            course.setMessage("Dodano nowy przedmiot")
            return True
        else:
            course.setMessage("Niepoprawne id kierunku")
            return False

    def g_courseForm(self, g_course):
        pass

    def examForm(self, exam):
        if self.__isvalidCourseId(exam):
            exam.setMessage("Dodano egzamin")
            return True
        else:
            exam.setMessage("Niepoprawne id przedmiotu")
            return False

    # validacje dla studenta
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

    def __isvalidAge(self, student):
        numbers_only = r'[0-9]+'
        if (re.fullmatch(numbers_only, student.getAge())):
            student.setAge(int(student.getAge())) 
            return True
        else:
            return False

    def __isvalidPhone(self, student):
        numbers_only = r'[0-9]+'
        if student.getPhone() == "":
            return True
        else:
            if (re.fullmatch(numbers_only, student.getPhone())):
                return True
            else:
                return False

    def __valid(self, student):
        student.setMessage("Dane poprawne")

    # validacje dla przedmiotu
    def __isvalidG_courseId(self, course):
        self.__curr.execute("SELECT id FROM grade_course WHERE id = ?", (course.getGradeCourseId(), ))
        item = self.__curr.fetchall()
        if item:
            return True
        else:
            return False

    def __isvalidCourseId(self, exam):
        self.__curr.execute("SELECT id FROM course WHERE id = ?", (exam.getCourseId(), ))
        item = self.__curr.fetchall()
        if item:
            return True
        else:
            return False

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
        df = pd.DataFrame(items)
        df.columns = 'id', 'imie', 'nazwisko', 'wiek', 'nr_tel', 'email', 'kierunek'
        print(df)
        # for item in items:
        #     print(item[1])

    ### zapytania dla kierunku ###
    def add_grade_course_to_db(self, kierunek):
        self.__curr.execute("INSERT INTO grade_course(name) VALUES (?)", (kierunek, ))
        Sqlite.commit(self, self.__connection)

    def print_grade_courses(self):
        self.__curr.execute("SELECT * FROM grade_course")
        items = self.__curr.fetchall()
        print('Kierunki')
        print('-'*50)
        df = pd.DataFrame(items)
        df.columns = 'id', 'nazwa kierunku'
        print(df)
        # for item in items:
        #     print(item)

    def delete_grade_course(self, id):
        self.__curr.execute("DELETE FROM grade_course WHERE id = ?", (id, ))
        Sqlite.commit(self, self.__connection)

    ### zapytania dla przedmiotu ###
    def add_course_to_db(self, przedmiot, g_c_id):
        self.__curr.execute("INSERT INTO course(name, grade_course_id) VALUES (?, ?)", (przedmiot, g_c_id))
        Sqlite.commit(self, self.__connection)

    def print_courses(self):
        self.__curr.execute("SELECT * FROM course")
        items = self.__curr.fetchall()
        print('Przedmioty')
        print('-'*50)
        df = pd.DataFrame(items)
        df.columns = 'id', 'nazwa przedmiotu', 'id kierunku'
        print(df)
        # for item in items:
        #     print(item)

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

    ### zapytania dla egzaminu ###
    def add_exam_to_db(self, exam, c_id):
        self.__curr.execute("INSERT INTO exam(name, course_id) VALUES (?, ?)", (exam, c_id))
        Sqlite.commit(self, self.__connection)

        ### Za kazdym razem jak program dodaje egzamin to dla kazdego studenta danego kierunku w innej tabeli tworzy wiersz
        ### laczacy danego studenta i egzamin

        egz = self.__curr.execute("SELECT * FROM exam WHERE name = ?", (exam, ))
        id_egzaminu = egz.fetchall()[-1][0]

        id_kierunkow = self.__curr.execute("SELECT grade_course.id FROM exam INNER JOIN course ON course.id = exam.course_id INNER JOIN grade_course ON course.grade_course_id = grade_course.id WHERE exam.name = ?", (exam, ))
        id_kierunku = id_kierunkow.fetchall()[0][0]
        studenci = self.__curr.execute("SELECT * FROM student INNER JOIN grade_course ON student.grade_course_id = grade_course.id WHERE grade_course.id = ?", (id_kierunku, ))
        items = studenci.fetchall()
        id_studentow = []
        for item in items:
            id_studentow.append(item[0])
        ilosc_informatykow = len(items)

        for i in range(ilosc_informatykow):
            self.__curr.execute("INSERT INTO exam_for_student(student_id, exam_id) VALUES (?, ?)", (items[i][0], id_egzaminu))
            Sqlite.commit(self, self.__connection)

    def print_exams(self):
        self.__curr.execute("SELECT exam.id, exam.name, course.name, grade_course.name FROM exam INNER JOIN course ON course.id = exam.course_id INNER JOIN grade_course ON course.grade_course_id = grade_course.id")
        items = self.__curr.fetchall()
        print('Egzaminy')
        print('-'*50)
        df = pd.DataFrame(items)
        df.columns = 'id egzaminu', 'nazwa egzaminu', 'nazwa przedmiotu', 'nazwa kierunku'
        print(df)
        # for item in items:
        #     print(item)

    def delete_exam(self, id):
        self.__curr.execute("PRAGMA foreign_keys = OFF")
        self.__curr.execute("DELETE FROM exam WHERE id = ?", (id, ))
        self.__curr.execute("PRAGMA foreign_keys = OFF")
        Sqlite.commit(self, self.__connection)

    def print_exam_for_student(self):
        self.__curr.execute("SELECT efs.id, efs.grade, exam.name, course.name, student.last_name FROM exam_for_student as efs INNER JOIN exam ON exam.id = efs.exam_id INNER JOIN student ON efs.student_id = student.id INNER JOIN course ON exam.course_id = course.id")
        items = self.__curr.fetchall()
        print("Oceny z egzaminow")
        if items:
            df = pd.DataFrame(items)
            df.columns = 'id', 'ocena', 'nazwa egzaminu', 'przedmiot', 'nazwisko studenta'
            print(df)
        else:
            print("Nie ma zadnych egzaminow w bazie")

    def close_db(self):
        Sqlite.close(self, self.__connection)