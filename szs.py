from grade_course_view import GCoursePage
from model import Student, GradeCourse, Course, Exam, ExamForStudent
from view import App, CoursePage, EFSPage, ExamPage, StudentPage, GCoursePage

class Controller:
    def __init__(self):
        self.st = Student()
        self.gc = GradeCourse()
        self.course = Course()
        self.ex = Exam()
        self.efs = ExamForStudent()
        self.view = App(self)

    def on_nav_button_click(self, button):
        
        options = {'Strona studentów': StudentPage,
                   'Strona przedmiotów': CoursePage,
                   'Strona kierunków': GCoursePage,
                   'Strona egzaminów': ExamPage,
                   'Strona ocen': EFSPage}

        self.view.show_frame(options[button])
        print(button)

    def main(self):
        self.view.main()

    #==Kontroller=dla=studentów==#

    def add_student(self, fname, lname, age, phone, email, g_course_id):
        self.st.addStudentToDb(fname, lname, age, phone, email, g_course_id)

    def display_all_students_data(self):
        rows = self.st.getAllStudents()
        return rows

    def delete_student(self, id):
        self.st.deleteStudent(id)

    def search_student_by(self, by, txt):
        return self.st.getBySearch(by, txt)

    #==Kontroller=dla=kierunków==#

    def display_all_gcourse_data(self):
        return self.gc.getAllGCourse()
        
    def add_gcourse(self, name):
        self.gc.addGCourseToDb(name)

    def search_by(self, by, txt):
        return self.gc.getBySearch(by, txt)

    def update_gcourse(self, name, id):
        self.gc.updateGCourse(name, id)

    def delete_gcourse(self, id):
        self.gc.deleteGCourse(id)

    #==Kontroller=dla=przedmiotów==#

    def display_all_course_data(self):
        return self.course.getAllCourse()

    def add_course(self, name, g_course):
        self.course.addCourseToDb(name, g_course)

    def delete_course(self, id):
        self.course.deleteCourse(id)

    def search_course_by(self, by, txt):
        return self.course.getBySearch(by, txt)

    #==Kontroller=dla=egzaminów==#

    def display_all_exam_data(self):
        return self.ex.getAllExam()

    def get_courses(self):
        return self.ex.getIdAndNameCOurse()

    def add_exam(self, name, course_id):
        self.ex.addExamToDb(name, course_id)
        self.efs.createEFS(name)

    def delete_exam(self, id):
        self.ex.deleteExam(id)

    #==Kontroler=dla=ocen==#

    def display_all_efs_data(self):
        return self.efs.getEFS()

if __name__ == "__main__":
    szs = Controller()
    szs.main()
    