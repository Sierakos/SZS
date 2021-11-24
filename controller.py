from tkinter import StringVar
from view import App
from model import Student, GradeCourse, Course, Exam, ExamForStudent


class Controller:

    def __init__(self):
        self.view = App(self)
        

    def main(self):
        self.view.main()

    def on_nav_button_click(self, nav_title):
        buttons = self.view.nav_buttons
        classes = self.view.classes
        pages = dict(zip(buttons, classes))
        self.view.show_frame(pages[nav_title])

    # Okno studenta

    def display_all_students_data(self):
        st = Student()
        return(st.getAllStudents())

    # idiotoodporność, która jest do poprawy bo to troche XD

    def add_student(self, fname, lname, age, phone, email, gcourse_id):
        st = Student()
        try:
            age = int(age)
        except:
            pass
        if not isinstance(age, int):
            print("wiek musi byc liczba")
        else:
            st.addStudentToDb(fname, lname, age, phone, email, gcourse_id)

    def delete_student(self, id):
        st = Student()
        st.deleteStudent(id)

    def update_student(self, id, fname, lname, age, phone, email, gcourse_id):
        st = Student()
        st.updateStudent(id, fname, lname, age, phone, email, gcourse_id)

    def search_student_by(self, search_by, search_txt):
        st = Student()
        return(st.getBySearch(search_by, search_txt))

    # Okno kierunku

    def display_all_gcourse_data(self):
        gc = GradeCourse()
        return(gc.getAllGCourse())

    def add_gcourse(self, name):
        gc = GradeCourse()
        gc.addGCourseToDb(name)

    def delete_gcourse(self, id):
        gc = GradeCourse()
        gc.deleteGCourse(id)

    def search_grade_course_by(self, search_by, search_txt):
        gc = GradeCourse()
        return(gc.getBySearch(search_by, search_txt))

    # Okno przedmiotu

    def display_all_course_data(self):
        co = Course()
        return(co.getAllCourse())
    
    def add_course(self, name, g_course_id):
        co = Course()
        co.addCourseToDb(name, g_course_id)

    def update_course(self, name, g_course_id, course_id):
        co = Course()
        co.updateCourse(name, g_course_id, course_id)

    def delete_course(self, id):
        co = Course()
        co.deleteCourse(id)

    def search_course_by(self, search_by, search_txt):
        co = Course()
        return(co.getBySearch(search_by, search_txt))

    # Okno egzaminów

    def display_all_exam_data(self):
        ex = Exam()
        return(ex.getAllExam())

    def add_exam(self, name, course_id):
        ex = Exam()
        efs = ExamForStudent()
        ex.addExamToDb(name, course_id)
        efs.createEFS(name)

    def delete_exam(self, id):
        ex = Exam()
        ex.deleteExam(id)

    def get_course_name(self):
        ex = Exam()
        return(ex.getIdAndNameCourse())

    # Okno ocen
    
    def display_all_efs_data(self):
        efs = ExamForStudent()
        return(efs.getEFS())

    def add_or_update_grade(self, id, grade):
        efs = ExamForStudent()
        efs.add_or_update_grade(id, grade)


if __name__ == '__main__':
    app = Controller()
    app.main()