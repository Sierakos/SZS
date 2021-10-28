import sqlite3

conn = sqlite3.connect('Student_system_managment.db')
c = conn.cursor()

# c.execute('''CREATE TABLE student(
#     id INTEGER NOT NULL PRIMARY KEY,
#     first_name VARCHAR(120) NOT NULL,
#     last_name VARCHAR(120) NOT NULL,
#     age INTEGER NOT NULL,
#     phone VARCHAR(120),
#     email VARCHAR(120),
#     grade_course_id INTEGER,
#     FOREIGN KEY (grade_course_id) REFERENCES grade_course(id)
# )''')

# c.execute('''CREATE TABLE grade_course(
#     id INTEGER NOT NULL PRIMARY KEY,
#     name VARCHAR(120) NOT NULL
# )''')

# c.execute('''CREATE TABLE course(
#     id INTEGER NOT NULL PRIMARY KEY,
#     name VARCHAR(120) NOT NULL,
#     grade_course_id INTEGER NOT NULL,
#     CONSTRAINT fk_degree_course
#     FOREIGN KEY (grade_course_id)
#     REFERENCES grade_course(id)
#     ON DELETE CASCADE
# )''')

# c.execute('''CREATE TABLE exam(
#     id INTEGER NOT NULL PRIMARY KEY,
#     name VARCHAR(120) NOT NULL,
#     grade INTEGER(10),
#     student_id INTEGER NOT NULL,
#     course_id INTEGER NOT NULL,
#     FOREIGN KEY(student_id) REFERENCES student(id),
#     FOREIGN KEY(course_id) REFERENCES course(id)
# )''')

# c.execute('''ALTER TABLE student ADD id_grade_course INTEGER''')
# c.execute('''DROP TABLE course''')

# c.execute('''INSERT INTO student (first_name, last_name, age, phone, email) VALUES (?, ?, ?, ?, ?)''',
# ('inny', 'student', 22, '938473463', 'inny@email.com'))
conn.commit()
conn.close()