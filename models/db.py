import sqlite3

conn = sqlite3.connect('models\\baza_danych\\Student_system_managment.db')
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

conn.commit()
conn.close()
