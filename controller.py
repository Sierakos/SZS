from tkinter import StringVar
from view import App
from model import Student, GradeCourse


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


    # Okno kierunku

    def display_all_gcourse_data(self):
        gc = GradeCourse()
        return(gc.getAllGCourse())

    def add_gcourse(self, name):
        gc = GradeCourse()
        gc.addGCourseToDb(name)



if __name__ == '__main__':
    app = Controller()
    app.main()