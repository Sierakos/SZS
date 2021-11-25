from tkinter import *
from .student_view import StudentPage
from .grade_course_view import GCoursePage
from .course_view import CoursePage
from .exam_view import ExamPage
from .efs_view import EFSPage

class App(Tk):
    nav_buttons = [
        'Strona studentów',
        'Strona przedmiotów',
        'Strona kierunków',
        'Strona egzaminów',
        'Strona ocen'
    ]

    def __init__(self, controller):
        Tk.__init__(self)
        self.controller = controller

        self._show_main_frame()
        self._show_title_frame()
        self._show_nav_frame()
        self._show_buttons()
        self._show_content_frame()
        self._center_window()

        self.frames = {}
        self.classes = []

        for F in (StudentPage, CoursePage, GCoursePage, ExamPage, EFSPage):
            frame = F(self.content_frame, self.controller)
            self.frames[F] = frame
            frame.place(x=0, y=0, width=1800, height=700)
            frame['bg'] = 'gray'
            self.classes.append(F)


        self.show_frame(StudentPage)	

    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()

    def main(self):
        self.mainloop()

    def _center_window(self):
        width = 1800
        height = 900
        x_offset = (self.winfo_screenwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2
        self.geometry(f'{width}x{height}+{x_offset}+{y_offset}')

    def _show_main_frame(self):
        self.main_frame = Frame(self, bg='yellow')
        self.main_frame.place(x=0, y=0, width=1800, height=900)

    def _show_title_frame(self):
        title_frame = Frame(self.main_frame, bg='green')
        title_frame.place(x=0, y=0, width=1800, height=100)

        title = Label(title_frame, text='System zarządzania studentami',
        bg='green', bd=10, font=('Times New Roman', 40, 'bold'))
        title.pack(side=TOP, fill=X)

    def _show_nav_frame(self):
        self.nav_frame = Frame(self.main_frame)
        self.nav_frame.place(x=0, y=100, width=1800, height=50)

    def _show_buttons(self):
        for button in self.nav_buttons:
            btn = Button(self.nav_frame, width=50, height=3, text=button,
            command=(lambda x=button: self.controller.on_nav_button_click(x)))
            btn.pack(side='left')

    def _show_content_frame(self):
        self.content_frame = Frame(self.main_frame)
        self.content_frame.place(x=0, y=150, width=1800, height=700)








