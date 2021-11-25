import tkinter as tk
from tkinter import ttk

class ExamPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.id_var=tk.StringVar()
        self.name_var=tk.StringVar()
        self.course_var=tk.StringVar()

        self.search_by_var=tk.StringVar()
        self.search_txt_var=tk.StringVar()

        form_frame = tk.Frame(self, bd=4, relief=tk.GROOVE, bg='crimson')
        form_frame.place(x=20, y=50, width=600, height=600)

        content_frame = tk.Frame(self, bd=4, relief=tk.GROOVE, bg='crimson')
        content_frame.place(x=640, y=50, width=1120, height=600)

        label = tk.Label(form_frame, text="Formularz egzaminu", bg='crimson', bd=10, fg='white', font=('Times New Roman', 20, 'bold'))
        label.grid(row=0, columnspan=2, pady=10, padx=(100,10), sticky="N")

        #==Form=labels==#

        fname_label = tk.Label(form_frame, text="Nazwa egzaminu", bg='crimson', bd=10, fg='white', font=('Times New Roman', 20, 'bold'))
        fname_label.grid(row=1, column=0, pady=10, padx=(100,10), sticky="W")

        lname_label = tk.Label(form_frame, text="Przedmiot", bg='crimson', bd=10, fg='white', font=('Times New Roman', 20, 'bold'))
        lname_label.grid(row=2, column=0, pady=10, padx=(100,10), sticky="W")


        #==Form=entry==#

        name_entry = tk.Entry(form_frame, textvariable=self.name_var, font=('times new roman', 15, 'bold'))
        name_entry.grid(row=1, column=1, pady=10, padx=10, sticky="W")

        self.course_combo = ttk.Combobox(form_frame, textvariable=self.course_var, font=('times new roman', 13, 'bold'), state='readonly', postcommand=self.update_courses_combobox)
        self.course_combo['values']=self.controller.get_course_name()
        self.course_combo.grid(row=2, column=1, pady=10, padx=10, sticky="W")

        #==Form=buttons==#

        btn_frame=tk.Frame(form_frame, bd=4, relief=tk.RIDGE, bg="gray")
        btn_frame.place(x=120, y=530, width=310, height=50)

        add_btn=tk.Button(btn_frame, text="Dodaj", width=17, command=self.add_exam)
        add_btn.grid(row=0, column=0, padx=10, pady=10)

        delete_btn=tk.Button(btn_frame, text="Usuń", width=17, command=self.delete_exam)
        delete_btn.grid(row=0, column=2, padx=10, pady=10)

        #==Content==#

        search_label=tk.Label(content_frame,text="Szukaj", bd=10, bg="crimson", fg="white", font=('times new roman', 15, 'bold'))
        search_label.grid(row=0, column=0, pady=10, padx=10)

        search_by=ttk.Combobox(content_frame, textvariable=self.search_by_var, font=('times new roman', 13, 'bold'), width=10, state='readonly')
        search_by['values']=['Egzamin', 'Przedmiot']
        search_by.grid(row=0, column=1, padx=10, pady=10)

        search_txt=tk.Entry(content_frame, textvariable=self.search_txt_var, font=('times new roman', 14, 'bold'), width=12, bd=5, relief=tk.GROOVE)
        search_txt.grid(row=0, column=3, pady=10, padx=10)

        search_btn=tk.Button(content_frame, text="Szukaj", width=13, command=self.search_exam)
        search_btn.grid(row=0, column=4, padx=10, pady=10)

        show_btn=tk.Button(content_frame, text="Pokaż wszystkich", width=13, command=self.show_exam_data)
        show_btn.grid(row=0, column=5, padx=10, pady=10)


        table_frame=tk.Frame(content_frame,bd=4,relief=tk.RIDGE,bg='gray')
        table_frame.place(x=10,y=70,width=1000,height=460)

        scroll_x=ttk.Scrollbar(table_frame,orient=tk.HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=tk.VERTICAL)
        self.exam_table=ttk.Treeview(table_frame,columns=('id','name','course_name','grade_course_name','course_id'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=tk.BOTTOM,fill=tk.X)
        scroll_y.pack(side=tk.RIGHT,fill=tk.Y)
        scroll_x.config(command=self.exam_table.xview)
        scroll_y.config(command=self.exam_table.yview)
        self.exam_table.heading('id',text='id')
        self.exam_table.heading('name',text='Nazwa egzaminu')
        self.exam_table.heading('course_name',text='Przedmiot')
        self.exam_table.heading('grade_course_name',text='Kierunek')
        self.exam_table.heading('course_id',text='Id przedmiotu')
        self.exam_table['show']='headings'
        self.exam_table.column('id',width=50)
        self.exam_table['displaycolumns']=('id','name','course_name','grade_course_name')
        self.exam_table.pack(fill=tk.BOTH,expand=True)
        self.exam_table.bind('<ButtonRelease-1>', self.get_cursor)
        self.show_exam_data()

    def show_exam_data(self):
        rows = self.controller.display_all_exam_data()
        for i in self.exam_table.get_children():
            self.exam_table.delete(i)
        for row in rows:
            self.exam_table.insert('', 'end', values=row)

    def add_exam(self):
        course_id = ''
        for i in self.course_var.get():
            if i == ' ':
                break
            course_id += i

        self.controller.add_exam(self.name_var.get(), course_id)
        self.show_exam_data()

    def delete_exam(self):
        self.controller.delete_exam(self.id_var.get())
        self.show_exam_data()

    def get_cursor(self, ev):
        try:
            cursor_row=self.exam_table.focus()
            content=self.exam_table.item(cursor_row)
            row=content['values']

            self.id_var.set(row[0])
            self.name_var.set(row[1])
            self.course_var.set(str(row[4]) + " " + str(row[2] + " " + str(row[3])))
        except:
            pass

    def update_courses_combobox(self):
        self.course_combo['values']=self.controller.get_course_name()

    def search_exam(self):
        convert = {'Egzamin': 'exam.name',
                   'Przedmiot': 'course.name'}
        rows = self.controller.search_exam_by(convert[self.search_by_var.get()], self.search_txt_var.get())
        for i in self.exam_table.get_children():
            self.exam_table.delete(i)
        for row in rows:
            self.exam_table.insert('', 'end', values=row)
            