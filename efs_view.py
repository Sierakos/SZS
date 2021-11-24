import tkinter as tk
from tkinter import ttk

class EFSPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.id_var=tk.StringVar()
        self.student_var=tk.StringVar()
        self.exam_var=tk.StringVar()
        self.grade_var=tk.StringVar()
        self.student_id_var=tk.StringVar()
        self.exam_id_var=tk.StringVar()

        self.search_by_var=tk.StringVar()
        self.search_txt_var=tk.StringVar()

        form_frame = tk.Frame(self, bd=4, relief=tk.GROOVE, bg='crimson')
        form_frame.place(x=20, y=50, width=600, height=600)

        content_frame = tk.Frame(self, bd=4, relief=tk.GROOVE, bg='crimson')
        content_frame.place(x=640, y=50, width=1120, height=600)

        label = tk.Label(form_frame, text="Formularz ocen", bg='crimson', bd=10, fg='white', font=('Times New Roman', 20, 'bold'))
        label.grid(row=0, columnspan=2, pady=10, padx=(100,10), sticky="N")

        #==Form=labels==#

        student_label = tk.Label(form_frame, text="Student", bg='crimson', bd=10, fg='white', font=('Times New Roman', 20, 'bold'))
        student_label.grid(row=1, column=0, pady=10, padx=(100,10), sticky="W")

        exam_label = tk.Label(form_frame, text="Egzamin", bg='crimson', bd=10, fg='white', font=('Times New Roman', 20, 'bold'))
        exam_label.grid(row=2, column=0, pady=10, padx=(100,10), sticky="W")

        grade_label = tk.Label(form_frame, text="Ocena", bg='crimson', bd=10, fg='white', font=('Times New Roman', 20, 'bold'))
        grade_label.grid(row=3, column=0, pady=10, padx=(100,10), sticky="W")

        #==Form=entry==#

        student_combo = tk.Entry(form_frame, textvariable=self.student_var, font=('times new roman', 15, 'bold'), state='readonly')
        student_combo.grid(row=1, column=1, pady=10, padx=10, sticky="W")

        exam_combo = tk.Entry(form_frame, textvariable=self.exam_var, font=('times new roman', 15, 'bold'), state='readonly')
        exam_combo.grid(row=2, column=1, pady=10, padx=10, sticky="W")

        # grade_entry = tk.Entry(form_frame, textvariable=self.grade_var, font=('times new roman', 15, 'bold'))
        # grade_entry.grid(row=3, column=1, pady=10, padx=10, sticky="W")

        grade_combo = ttk.Combobox(form_frame, textvariable=self.grade_var, font=('times new roman', 13, 'bold'), state='readonly')
        grade_combo['values']=('2', '3', '3.5', '4', '4.5', '5')
        grade_combo.grid(row=3, column=1, pady=10, padx=10, sticky="W")

        #==Form=buttons==#

        btn_frame=tk.Frame(form_frame, bd=4, relief=tk.RIDGE, bg="gray")
        btn_frame.place(x=120, y=530, width=310, height=50)

        add_btn=tk.Button(btn_frame, text="Dodaj ocenę", width=10, command=self.add_or_update_grade)
        add_btn.grid(row=0, column=0, padx=10, pady=10)

        update_btn=tk.Button(btn_frame, text="Zaktualizuj ocenę", width=10)
        update_btn.grid(row=0, column=1, padx=10, pady=10)

        delete_btn=tk.Button(btn_frame, text="Usuń", width=10)
        delete_btn.grid(row=0, column=2, padx=10, pady=10)

        #==Content==#

        search_label=tk.Label(content_frame,text="Szukaj", bd=10, bg="crimson", fg="white", font=('times new roman', 15, 'bold'))
        search_label.grid(row=0, column=0, pady=10, padx=10)

        search_by=ttk.Combobox(content_frame, textvariable=self.search_by_var, font=('times new roman', 13, 'bold'), width=10, state='readonly')
        search_by['values']=['Student', 'Egzamin']
        search_by.grid(row=0, column=1, padx=10, pady=10)

        search_txt=tk.Entry(content_frame, textvariable=self.search_txt_var, font=('times new roman', 14, 'bold'), width=12, bd=5, relief=tk.GROOVE)
        search_txt.grid(row=0, column=3, pady=10, padx=10)

        search_btn=tk.Button(content_frame, text="Szukaj", width=13)
        search_btn.grid(row=0, column=4, padx=10, pady=10)

        show_btn=tk.Button(content_frame, text="Pokaż wszystkich", width=13)
        show_btn.grid(row=0, column=5, padx=10, pady=10)

        refresh_btn=tk.Button(content_frame, text="Odśwież", width=13, command=self.show_efs_data)
        refresh_btn.grid(row=0, column=6, padx=10, pady=10)



        table_frame=tk.Frame(content_frame,bd=4,relief=tk.RIDGE,bg='gray')
        table_frame.place(x=10,y=70,width=1000,height=460)

        scroll_x=ttk.Scrollbar(table_frame,orient=tk.HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=tk.VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=('id','student','exam','grade','student_id','course_id'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=tk.BOTTOM,fill=tk.X)
        scroll_y.pack(side=tk.RIGHT,fill=tk.Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading('id',text='id')
        self.student_table.heading('student',text='Student')
        self.student_table.heading('exam',text='Egzamin')
        self.student_table.heading('grade',text='ocena')
        self.student_table.heading('student_id',text='Id studenta')
        self.student_table.heading('course_id',text='Id przedmiotu')
        self.student_table['show']='headings'
        self.student_table.column('id',width=50)
        self.student_table['displaycolumns']=('id','student','exam','grade')
        self.student_table.pack(fill=tk.BOTH,expand=True)
        self.student_table.bind('<ButtonRelease-1>', self.get_cursor)
        self.show_efs_data()

    def add_or_update_grade(self):
        self.controller.add_or_update_grade(self.id_var.get(), self.grade_var.get())
        self.show_efs_data()

    def show_efs_data(self):
        rows = self.controller.display_all_efs_data()
        for i in self.student_table.get_children():
            self.student_table.delete(i)
        for row in rows:
            self.student_table.insert('', 'end', values=row)

    def get_cursor(self, ev):
        try:
            cursor_row=self.student_table.focus()
            content=self.student_table.item(cursor_row)
            row=content['values']

            self.id_var.set(row[0])
            self.student_var.set(row[1])
            self.exam_var.set(row[2])
            self.grade_var.set(row[3])
            if self.grade_var.get() == 'None':
                self.grade_var.set("")
            self.student_id_var.set(row[4])
            self.exam_id_var.set(row[5])
        except:
            pass