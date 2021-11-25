import sqlite3

conn = sqlite3.connect('C:\\Users\\Sebastian\\Desktop\\studia\\ZPO\\test\\SZS\\SZS_console\\Student_system_managment.db')
c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS student(
    id INTEGER NOT NULL PRIMARY KEY,
    first_name VARCHAR(120) NOT NULL,
    last_name VARCHAR(120) NOT NULL,
    age INTEGER NOT NULL,
    phone VARCHAR(120),
    email VARCHAR(120),
    grade_course_id INTEGER,
    FOREIGN KEY (grade_course_id) REFERENCES grade_course(id) ON DELETE SET NULL
)''')

c.execute('''CREATE TABLE IF NOT EXISTS grade_course(
    id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(120) NOT NULL
)''')

c.execute('''CREATE TABLE IF NOT EXISTS course(
    id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    grade_course_id INTEGER NOT NULL,
    FOREIGN KEY (grade_course_id) REFERENCES grade_course(id) ON DELETE CASCADE
)''')

c.execute('''CREATE TABLE IF NOT EXISTS exam(
    id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    course_id INTEGER NOT NULL,
    FOREIGN KEY(course_id) REFERENCES course(id) ON DELETE CASCADE
)''')

c.execute('''CREATE TABLE IF NOT EXISTS exam_for_student(
    id INTEGER NOT NULL PRIMARY KEY,
    student_id INTEGER NOT NULL,
    exam_id INTEGER NOT NULL,
    grade INTEGER(10),
    FOREIGN KEY(student_id) REFERENCES student(id) ON DELETE CASCADE,
    FOREIGN KEY(exam_id) REFERENCES exam(id) ON DELETE CASCADE
)''')

# c.execute('''ALTER TABLE student ADD id_grade_course INTEGER''')
# c.execute('''DROP TABLE exam_for_student''')

# c.execute('''INSERT INTO student (first_name, last_name, age, phone, email) VALUES (?, ?, ?, ?, ?)''',
# ('inny', 'student', 22, '938473463', 'inny@email.com'))

# egzaminy = c.execute("SELECT * FROM exam")
# items = egzaminy.fetchall()
# for item in items:
#     print(item)

# c.execute("INSERT INTO exam_for_student(student_id, exam_id) VALUES(8, 3)")
# c.execute("UPDATE student SET grade_course_id = 1 WHERE id=1")
# conn.commit()

# wypisuje studentow, ktorzy sa na informatyce (kierunku o id = 1)
# studenci = c.execute("SELECT * FROM student INNER JOIN grade_course ON student.grade_course_id = grade_course.id WHERE grade_course.id = 1")
# items = studenci.fetchall()
# id_studentow = []
# for item in items:
#     print(item)
#     id_studentow.append(item[0])
# print(id_studentow)
# ilosc_informatykow = len(items)

# nowy_egzamin = "Pierwszy egzamin z matematyki II"
# c.execute("INSERT INTO exam(name, course_id) VALUES (?, ?)", (nowy_egzamin, 1))
# egz = c.execute("SELECT * FROM exam WHERE name = ?", (nowy_egzamin, ))
# items = egz.fetchall()
# for item in items:
#     print(item)
# id_egzaminu = egz.fetchall()[0][0]
# print(id_egzaminu)

# for i in range(ilosc_informatykow):
#     # print(f"id studenta: {items[i][0]}, id egzaminu: {id_egzaminu}")
#     c.execute("INSERT INTO exam_for_student(student_id, exam_id) VALUES (?, ?)", (items[i][0], id_egzaminu))


# egzaminy_dla_studentow = c.execute("SELECT efs.id, efs.exam_id, efs.grade, exam.name, course.name, student.first_name FROM exam_for_student as efs INNER JOIN exam ON exam.id = efs.exam_id INNER JOIN student ON efs.student_id = student.id INNER JOIN course ON exam.course_id = course.id")
# items = egzaminy_dla_studentow.fetchall()
# for item in items:
#     print(item)

# id_kierunku = c.execute("SELECT grade_course.id FROM exam INNER JOIN course ON course.id = exam.course_id INNER JOIN grade_course ON course.grade_course_id = grade_course.id WHERE exam.name = ?", (nowy_egzamin, ))
# items = id_kierunku.fetchall()[-1][0]
# print(items)

# c.execute("UPDATE exam_for_student SET grade = 3.5 WHERE student_id = 2 AND exam_id = 5")

# c.execute("SELECT AVG(efs.grade), course.name, student.first_name, student.last_name FROM exam_for_student as efs INNER JOIN exam ON exam.id = efs.exam_id INNER JOIN student ON efs.student_id = student.id INNER JOIN course ON exam.course_id = course.id GROUP BY student.id, course.id")
# items = c.fetchall()
# for item in items:
#     print(item)
#     if not isinstance(item[0], int) and not isinstance(item[0], float):
#         continue
#     else:
#         iterate += 1
#         grades += item[0]
#         print('a')
# print(f"Średnia ocen z przedmiotu 'Komputery' dla studenta {item[2]} {item[3]}: {grades/iterate}")

c.execute("Select * FROM student")
items = c.fetchall()
for item in items:
    print(item)

# c.execute("SELECT ROUND(AVG(efs.grade),2), course.name, student.first_name, student.last_name, student.age, student.phone, student.email, grade_course.name FROM exam_for_student as efs INNER JOIN exam ON exam.id = efs.exam_id INNER JOIN student ON efs.student_id = student.id INNER JOIN course ON exam.course_id = course.id INNER JOIN grade_course ON grade_course.id = student.grade_course_id GROUP BY student.id, course.id HAVING efs.student_id = 2")
# items = c.fetchall()
# print(items)



conn.commit()
conn.close()