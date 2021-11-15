import tkinter as tk
from tkinter import ttk

class GCoursePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        print('gcourse object')

        self.controller = controller

        self.id_var = tk.StringVar()
        self.name_var = tk.StringVar()

        self.search_by_var = tk.StringVar()
        self.search_txt_var = tk.StringVar()

        form_frame = tk.Frame(self, bd=4, relief=tk.GROOVE, bg='crimson')
        form_frame.place(x=20, y=50, width=600, height=600)

        self.content_frame = tk.Frame(self, bd=4, relief=tk.GROOVE, bg='crimson')
        self.content_frame.place(x=640, y=50, width=1120, height=600)

        label = tk.Label(form_frame, text="Formularz kierunku", bg='crimson', bd=10, fg='white', font=('Times New Roman', 20, 'bold'))
        label.grid(row=0, columnspan=2, pady=10, padx=(100,10), sticky="N")

        #==Form=labels==#

        id_label = tk.Label(form_frame, text="Id", bg='crimson', bd=10, fg='white', font=('Times New Roman', 20, 'bold'))
        id_label.grid(row=1, column=0, pady=10, padx=(100,10), sticky="W")

        name_label = tk.Label(form_frame, text="Nazwa kierunku", bg='crimson', bd=10, fg='white', font=('Times New Roman', 20, 'bold'))
        name_label.grid(row=2, column=0, pady=10, padx=(100,10), sticky="W")

        #==Form=entry==#

        id_entry = tk.Entry(form_frame, textvariable=self.id_var, font=('times new roman', 15, 'bold'), state=tk.DISABLED)
        id_entry.grid(row=1, column=1, pady=10, padx=10, sticky="W")

        name_entry = tk.Entry(form_frame, textvariable=self.name_var, font=('times new roman', 15, 'bold'))
        name_entry.grid(row=2, column=1, pady=10, padx=10, sticky="W")

        #==Form=buttons==#

        btn_frame=tk.Frame(form_frame, bd=4, relief=tk.RIDGE, bg="gray")
        btn_frame.place(x=120, y=530, width=310, height=50)

        add_btn=tk.Button(btn_frame, text="Dodaj", width=10, command=self.add_gcourse)
        add_btn.grid(row=0, column=0, padx=10, pady=10)

        update_btn=tk.Button(btn_frame, text="Zaktualizuj", width=10, command=self.update_gcourse)
        update_btn.grid(row=0, column=1, padx=10, pady=10)

        delete_btn=tk.Button(btn_frame, text="Usuń", width=10, command=self.delete_gcourse)
        delete_btn.grid(row=0, column=2, padx=10, pady=10)

        #==Content==#

        search_label=tk.Label(self.content_frame,text="Szukaj", bd=10, bg="crimson", fg="white", font=('times new roman', 15, 'bold'))
        search_label.grid(row=0, column=0, pady=10, padx=10)

        search_by=ttk.Combobox(self.content_frame, textvariable=self.search_by_var, font=('times new roman', 13, 'bold'), width=10, state='readonly')
        search_by['values']=['name']
        search_by.grid(row=0, column=1, padx=10, pady=10)

        search_txt=tk.Entry(self.content_frame, textvariable=self.search_txt_var, font=('times new roman', 14, 'bold'), width=12, bd=5, relief=tk.GROOVE)
        search_txt.grid(row=0, column=3, pady=10, padx=10)

        search_btn=tk.Button(self.content_frame, text="Szukaj", width=13, command=self.search_gcourse)
        search_btn.grid(row=0, column=4, padx=10, pady=10)

        show_btn=tk.Button(self.content_frame, text="Pokaż wszystko", width=13, command=self.show_gcourse_data)
        show_btn.grid(row=0, column=5, padx=10, pady=10)
        

        table_frame=tk.Frame(self.content_frame,bd=4,relief=tk.RIDGE,bg='gray')
        table_frame.place(x=10,y=70,width=1000,height=460)

        scroll_x=ttk.Scrollbar(table_frame,orient=tk.HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=tk.VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=('id','name'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=tk.BOTTOM,fill=tk.X)
        scroll_y.pack(side=tk.RIGHT,fill=tk.Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading('id',text='id')
        self.student_table.heading('name',text='nazwa kierunku')
        self.student_table['show']='headings'
        self.student_table.column('id',width=50)
        self.student_table.column('name',width=100)
        self.student_table.pack(fill=tk.BOTH,expand=True)
        self.student_table.bind('<ButtonRelease-1>', self.get_cursor)
        self.show_gcourse_data()

    def add_gcourse(self):
        self.controller.add_gcourse(self.name_var.get())
        self.show_gcourse_data()

    def show_gcourse_data(self):
        rows = self.controller.display_all_gcourse_data()
        for i in self.student_table.get_children():
            self.student_table.delete(i)
        for row in rows:
            self.student_table.insert('', 'end', values=row)

    def update_gcourse(self):
        self.controller.update_gcourse(self.name_var.get(), self.id_var.get())
        self.show_gcourse_data()

    def delete_gcourse(self):
        self.controller.delete_gcourse(self.id_var.get())
        self.show_gcourse_data()

    def get_cursor(self, ev):
        try:
            cursor_row=self.student_table.focus()
            content=self.student_table.item(cursor_row)
            row=content['values']

            self.id_var.set(row[0])
            self.name_var.set(row[1])
        except:
            pass

    def search_gcourse(self):
        rows = self.controller.search_by(self.search_by_var.get(), self.search_txt_var.get())
        for i in self.student_table.get_children():
            self.student_table.delete(i)
        for row in rows:
            self.student_table.insert('', 'end', values=row)
            