from db_connect import Sqlite
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF

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

    def print_info_about_active_students(self):
        self.__curr.execute("SELECT s.id, s.first_name, s.last_name, s.age, s.phone, s.email, gc.name FROM student as s INNER JOIN grade_course as gc ON gc.id = s.grade_course_id")
        items = self.__curr.fetchall()
        print('Aktywni studenci')
        print('-'*50)
        if items:
            df = pd.DataFrame(items)
            df.columns = 'id studenta', 'imie', 'nazwisko', 'wiek', 'nr_tel', 'email', 'kierunek'
            print(df)
        else:
            print("Nie ma zadnych studentów w bazie")

    def print_info_about_all_students(self):
        self.__curr.execute("SELECT * FROM student")
        items = self.__curr.fetchall()
        print('Wszyscy studenci')
        print('-'*50)
        if items:
            df = pd.DataFrame(items)
            df.columns = 'id studenta', 'imie', 'nazwisko', 'wiek', 'nr_tel', 'email', 'kierunek'
            print(df)
        else:
            print("Nie ma zadnych studentów w bazie")

    def add_student_to_g_course(self, student_id, g_c_id):
        self.__curr.execute("UPDATE student SET grade_course_id = ? WHERE student.id = ?", (g_c_id, student_id))
        Sqlite.commit(self, self.__connection)
        
    ### zapytania dla kierunku ###
    def add_grade_course_to_db(self, kierunek):
        self.__curr.execute("INSERT INTO grade_course(name) VALUES (?)", (kierunek, ))
        Sqlite.commit(self, self.__connection)

    def print_grade_courses(self):
        self.__curr.execute("SELECT * FROM grade_course")
        items = self.__curr.fetchall()
        print('Kierunki')
        print('-'*50)
        if items:
            df = pd.DataFrame(items)
            df.columns = 'id', 'nazwa kierunku'
            print(df)
        else:
            print("Nie ma zadnych kierunków w bazie")
        

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
        if items:
            df = pd.DataFrame(items)
            df.columns = 'id', 'nazwa przedmiotu', 'id kierunku'
            print(df)
        else:
            print("Nie ma zadnych Przedmiotów w bazie")
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
        if items:
            df = pd.DataFrame(items)
            df.columns = 'id egzaminu', 'nazwa egzaminu', 'nazwa przedmiotu', 'nazwa kierunku'
            print(df)
        else:
            print("Nie ma zadnych egzaminow w bazie")
        # for item in items:
        #     print(item)

    def delete_exam(self, id):
        self.__curr.execute("DELETE FROM exam WHERE id = ?", (id, ))
        Sqlite.commit(self, self.__connection)

    def print_exam_for_student(self):
        self.__curr.execute("SELECT efs.id, efs.student_id, efs.grade, exam.name, course.name, student.first_name, student.last_name FROM exam_for_student as efs INNER JOIN exam ON exam.id = efs.exam_id INNER JOIN student ON efs.student_id = student.id INNER JOIN course ON exam.course_id = course.id")
        items = self.__curr.fetchall()
        print("Oceny z egzaminow")
        if items:
            df = pd.DataFrame(items)
            df.columns = 'id', 'id studenta', 'ocena', 'nazwa egzaminu', 'przedmiot', 'imie studenta', 'nazwisko studenta'
            print(df)
        else:
            print("Nie ma zadnych egzaminow w bazie")

    def add_grade_to_exam(self):
        id = input("Wybierz id egzaminu z opcji nr.13: ")
        student_id = input("Podaj id studenta: ")
        grade = input("Podaj ocene: ")
        self.__curr.execute("UPDATE exam_for_student SET grade = ? WHERE student_id = ? AND id = ?", (grade, student_id, id))
        Sqlite.commit(self, self.__connection)
        print("Zmieniono ocenę")

    def print_avg_grade(self):
        self.__curr.execute("SELECT AVG(efs.grade), course.name, student.first_name, student.last_name FROM exam_for_student as efs INNER JOIN exam ON exam.id = efs.exam_id INNER JOIN student ON efs.student_id = student.id INNER JOIN course ON exam.course_id = course.id GROUP BY student.id, course.id")
        items = self.__curr.fetchall()
        if items:
            df = pd.DataFrame(items)
            df.columns = 'Ocena', 'nazwa przedmiotu', 'imie', 'nazwisko'
            print(df)
        else:
            print("Nie ma zadnych egzaminow w bazie")

    def show_graph(self, course_id):
        self.__curr.execute("SELECT ROUND(AVG(efs.grade),2), course.name, student.first_name, student.last_name FROM exam_for_student as efs INNER JOIN exam ON exam.id = efs.exam_id INNER JOIN student ON efs.student_id = student.id INNER JOIN course ON exam.course_id = course.id GROUP BY student.id, course.id HAVING course.id = ?", (course_id, ))
        items = self.__curr.fetchall()
        courses = []
        avg_grades = []
        for item in items:
            courses.append(f"{item[2]} {item[3]}")
            avg_grades.append(item[0])
        print(avg_grades)
        xpoints = np.array(courses)
        ypoints = np.array(avg_grades)

        plt.bar(xpoints, ypoints)
        plt.ylim(2.0, 5.0)
        plt.show()

    def create_pdf(self, student_id):
        self.__curr.execute("SELECT ROUND(AVG(efs.grade),2), course.name, student.id, student.first_name, student.last_name, student.age, student.phone, student.email, grade_course.name FROM exam_for_student as efs INNER JOIN exam ON exam.id = efs.exam_id INNER JOIN student ON efs.student_id = student.id INNER JOIN course ON exam.course_id = course.id INNER JOIN grade_course ON grade_course.id = student.grade_course_id GROUP BY student.id, course.id HAVING student.id = ?", (student_id, ))
        items = self.__curr.fetchall()
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        # create a cell
        try:
            pdf.cell(200, 10, txt="Akademia Pana Kleksa srednie oceny", 
                    ln=1, align='C')
            pdf.cell(200, 10, txt=f"{items[0][3]} {items[0][4]} | {items[0][8]}", 
                    ln=2, align='C')
            line=3
            for item in items:
                print(item)
                pdf.cell(200, 10, txt=f"{item[1]}: {item[0]}",
                        ln=line)
                line += 1
            pdf.output(f"{items[0][2]}_{items[0][3]}_{items[0][4]}.pdf")
        except:
            print("Id studenta jest nieprawidlowe albo nie ma jeszcze zadnych ocen.")
        
        

    def close_db(self):
        Sqlite.close(self, self.__connection)