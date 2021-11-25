# TODO: Dodać walidacje

from views.view import App
from models.model import Student, GradeCourse, Course, Exam, ExamForStudent
from views.view_console.view_console import ConsoleView

import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF

import os

class Controller:
    def __init__(self):
        self.st = Student()
        self.gc = GradeCourse()
        self.co = Course()
        self.ex = Exam()
        self.efs = ExamForStudent()

    def main(self):
        self.view = App(self)
        self.view.main()

    def main_console(self):
        self.console_view = ConsoleView(self)
        self.console_view.main()

    def on_nav_button_click(self, nav_title):
        buttons = self.view.nav_buttons
        classes = self.view.classes
        pages = dict(zip(buttons, classes))
        self.view.show_frame(pages[nav_title])

    # Okno studenta

    def display_all_students_data(self):
        return(self.st.getAllStudents())

    def add_student(self, fname, lname, age, phone, email, gcourse_id):
        try:
            age = int(age)
        except:
            pass
        if not isinstance(age, int):
            print("wiek musi byc liczba")
        else:
            self.st.addStudentToDb(fname, lname, age, phone, email, gcourse_id)

    def delete_student(self, id):
        self.st.deleteStudent(id)

    def update_student(self, id, fname, lname, age, phone, email, gcourse_id):
        self.st.updateStudent(id, fname, lname, age, phone, email, gcourse_id)

    def search_student_by(self, search_by, search_txt):
        return(self.st.getBySearch(search_by, search_txt))

    def create_PDF(self, student_id):
        rows = self.st.getInfoForPDF(student_id)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)

        try:
            os.makedirs("pliki_pdf")
        except FileExistsError:
            # folder już istnieje
            pass
       
        try:
            pdf.cell(200, 10, txt="Akademia Pana Kleksa srednie oceny", 
                    ln=1, align='C')
            pdf.cell(200, 10, txt=f"{rows[0][3]} {rows[0][4]} | {rows[0][8]}", 
                    ln=2, align='C')
            line=3
            for row in rows:
                pdf.cell(200, 10, txt=f"{row[1]}: {row[0]}",
                        ln=line)
                line += 1
            pdf.output(f"pliki_pdf\\{rows[0][2]}_{rows[0][3]}_{rows[0][4]}.pdf")
        except:
            print("Id studenta jest nieprawidlowe albo nie ma jeszcze zadnych ocen.")

    # Okno kierunku

    def display_all_gcourse_data(self):
        return(self.gc.getAllGCourse())

    def add_gcourse(self, name):
        self.gc.addGCourseToDb(name)

    def delete_gcourse(self, id):
        self.gc.deleteGCourse(id)

    def search_grade_course_by(self, search_by, search_txt):
        return(self.gc.getBySearch(search_by, search_txt))

    # Okno przedmiotu

    def display_all_course_data(self):
        return(self.co.getAllCourse())
    
    def add_course(self, name, g_course_id):
        self.co.addCourseToDb(name, g_course_id)

    def update_course(self, name, g_course_id, course_id):
        self.co.updateCourse(name, g_course_id, course_id)

    def delete_course(self, id):
        self.co.deleteCourse(id)

    def search_course_by(self, search_by, search_txt):
        return(self.co.getBySearch(search_by, search_txt))

    def show_graph(self, course_id):
        rows = self.co.getInfoForChart(course_id)
        courses = []
        avg_grades = []
        for row in rows:
            courses.append(f"{row[2]} {row[3]}")
            avg_grades.append(row[0])
        xpoints = np.array(courses)
        ypoints = np.array(avg_grades)

        plt.bar(xpoints, ypoints)
        plt.ylim(1.5, 5.0)
        plt.show()

    # Okno egzaminów

    def display_all_exam_data(self):
        return(self.ex.getAllExam())

    def add_exam(self, name, course_id):
        self.ex.addExamToDb(name, course_id)
        self.efs.createEFS(name)

    def delete_exam(self, id):
        self.ex.deleteExam(id)

    def get_course_name(self):
        return(self.ex.getIdAndNameCourse())

    def search_exam_by(self, search_by, search_txt):
        return(self.ex.getBySearch(search_by, search_txt))

    # Okno ocen
    
    def display_all_efs_data(self):
        return(self.efs.getEFS())

    def add_or_update_grade(self, id, grade):
        self.efs.add_or_update_grade(id, grade)
