# TODO: Zrobić poprawne dodawanie do bazy
# TODO: dodać walidacje (czy dana wartość w bazie danych już istnieje)
#       zwłaszcza dla kierunku

from . import db_connect as db

class Student(db.Sqlite):
    __first_name = ""
    __last_name = ""
    __age = 0
    __phone = 0
    __email = ""
    __message = ""
    __grand_course_id = 0

    def __init__(self):
        self.connect()
        self.c = self.conn.cursor()

    # setters
    def setFname(self, par):
        self.__first_name = par

    def setLname(self, par):
        self.__last_name = par

    def setAge(self, par):
        self.__age = par

    def setPhone(self, par):
        self.__phone = par

    def setEmail(self, par):
        self.__email = par

    def setGCourseId(self, par):
        self.__grand_course_id = par

    def setMessage(self, par):
        self.__message = par

    def addStudentToDb(self, fname, lname, age, phone, email, g_course_id):
        self.c.execute('''INSERT INTO student(first_name, last_name, age, phone, email, grade_course_id)
                       VALUES (?, ?, ?, ?, ?, ?)''',
                       (fname, lname, age, phone, email, g_course_id))
        self.conn.commit()

    def updateStudent(self, id, fname, lname, age, phone, email, g_course_id):
        self.c.execute('''UPDATE student SET first_name = ?, last_name = ?, age = ?, phone = ?, email = ?, grade_course_id = ? WHERE id = (?)''',
                       (fname, lname, age, phone, email, g_course_id, id))
        self.conn.commit()

    def deleteStudent(self, id):
        self.c.execute("DELETE FROM student WHERE id = ?", (id, ))
        self.conn.commit()
        
    # getters
    def getFname(self):
        return self.__first_name

    def getLname(self):
        return self.__last_name

    def getAge(self):
        return self.__age

    def getPhone(self):
        return self.__phone

    def getEmail(self):
        return self.__email

    def getGCourseId(self):
        return self.__grand_course_id
    
    def getMessage(self):
        return self.__message

    def getAllStudents(self):
        self.c.execute('''SELECT student.id, first_name, last_name, age, phone, email, grade_course.name, grade_course.id FROM student
                       INNER JOIN grade_course on grade_course.id = student.grade_course_id''')
        rows = self.c.fetchall()
        return rows

    def getBySearch(self, by, txt):
        self.c.execute(f'''SELECT student.id, first_name, last_name, age, phone, email, grade_course.name FROM student
                       INNER JOIN grade_course on grade_course.id = student.grade_course_id
                       WHERE {by} LIKE "%{txt}%"''')
        rows = self.c.fetchall()
        return rows

    def getInfoForPDF(self, student_id):
        self.c.execute('''SELECT ROUND(AVG(efs.grade),2), course.name, student.id, student.first_name,
                            student.last_name, student.age, student.phone, student.email, grade_course.name 
                            FROM exam_for_student as efs 
                            INNER JOIN exam ON exam.id = efs.exam_id 
                            INNER JOIN student ON efs.student_id = student.id 
                            INNER JOIN course ON exam.course_id = course.id 
                            INNER JOIN grade_course ON grade_course.id = student.grade_course_id 
                            GROUP BY student.id, course.id 
                            HAVING student.id = ?''', (student_id, ))
        return(self.c.fetchall())
        

class GradeCourse(db.Sqlite):
    __name = ""

    def __init__(self):
        self.connect()
        self.c = self.conn.cursor()

    # setters
    def setName(self, par):
        self.__name = par

    def setMessage(self, par):
        self.__message = par

    def addGCourseToDb(self, par):
        self.c.execute("INSERT INTO grade_course(name) VALUES(?)", (par, ))
        self.conn.commit()

    def updateGCourse(self, name, id):
        self.c.execute("UPDATE grade_course SET name = ? WHERE id = ?", (name, id))
        self.conn.commit()

    def deleteGCourse(self, id):
        self.c.execute("DELETE FROM grade_course WHERE id = ?", (id, ))
        self.conn.commit()

    # getters
    def getName(self):
        return self.__name

    def getMessage(self):
        return self.__message

    def getAllGCourse(self):
        self.c.execute("SELECT * FROM grade_course")
        rows = self.c.fetchall()
        return rows

    def getBySearch(self, by, txt):
        self.c.execute(f"SELECT * FROM grade_course WHERE {by} LIKE '%{txt}%'")
        return self.c.fetchall()

class Course(db.Sqlite):
    __name = ""
    __grade_course_id = 0

    def __init__(self):
        self.connect()
        self.c = self.conn.cursor()

    # setters
    def setName(self, par):
        self.__name = par

    def setGradeCourseId(self, par):
        self.__grade_course_id = par

    def setMessage(self, par):
        self.__message = par

    def addCourseToDb(self, name, g_course_id):
        self.setName(name)
        self.setGradeCourseId(g_course_id)
        self.c.execute("INSERT INTO course(name, grade_course_id) VALUES(?, ?)", (self.getName(), self.getGradeCourseId()))
        self.conn.commit()

    def updateCourse(self, name, g_course_id, id):
        self.c.execute("UPDATE course SET name = ?, grade_course_id = ? WHERE id = ?", (name, g_course_id, id))
        self.conn.commit()

    def deleteCourse(self, id):
        self.c.execute("DELETE FROM course WHERE id = ?", (id, ))
        self.conn.commit()

    # getters
    def getName(self):
        return self.__name

    def getGradeCourseId(self):
        return self.__grade_course_id

    def getMessage(self):
        return self.__message

    def getAllCourse(self):
        self.c.execute('''SELECT course.id, course.name, grade_course.name, grade_course.id
                        FROM course INNER JOIN grade_course on grade_course.id = course.grade_course_id''')
        return self.c.fetchall()

    def getAllNameGcourse(self):
        self.c.execute("SELECT id, name FROM grade_course")
        return self.c.fetchall()

    def getBySearch(self, by, txt):
        self.c.execute(f'''SELECT course.id, course.name, grade_course.name, grade_course.id FROM course
                        INNER JOIN grade_course on grade_course.id = course.grade_course_id
                        WHERE {by} LIKE "%{txt}%"''')
        return self.c.fetchall()

    def getInfoForChart(self, course_id):
        self.c.execute('''SELECT ROUND(AVG(efs.grade),2), course.name, student.first_name, student.last_name 
                        FROM exam_for_student as efs 
                        INNER JOIN exam ON exam.id = efs.exam_id 
                        INNER JOIN student ON efs.student_id = student.id 
                        INNER JOIN course ON exam.course_id = course.id 
                        GROUP BY student.id, course.id 
                        HAVING course.id = ?''', (course_id, ))
        return(self.c.fetchall())

class Exam(db.Sqlite):
    __name = ""
    __course_id = 0


    def __init__(self):
        self.connect()
        self.c = self.conn.cursor()
        
    # setters
    def setName(self, par):
        self.__name = par

    def setCourseId(self, par):
        self.__course_id = par

    def setMessage(self, par):
        self.__message = par

    def addExamToDb(self, name, course_id):
        self.c.execute('INSERT INTO exam(name, course_id) VALUES(?,?)', (name, course_id))
        self.conn.commit()

    def deleteExam(self, id):
        self.c.execute('DELETE FROM exam WHERE id = ?', (id,))
        self.conn.commit()

    # getters
    def getName(self):
        return self.__name

    def getCourseId(self):
        return self.__course_id

    def getMessage(self):
        return self.__message

    def getAllExam(self):
        self.c.execute('''SELECT exam.id, exam.name, course.name, grade_course.name, course.id FROM exam 
                        INNER JOIN course on course.id = exam.course_id
                        INNER JOIN grade_course on grade_course.id = course.grade_course_id''')
        return self.c.fetchall()

    def getIdAndNameCourse(self):
        self.c.execute('SELECT course.id, course.name, grade_course.name FROM course INNER JOIN grade_course on grade_course.id = course.grade_course_id')
        return self.c.fetchall()

    def getBySearch(self, by, txt):
        self.c.execute(f'''SELECT exam.id, exam.name, course.name FROM exam
                       INNER JOIN course on course.id = exam.course_id
                       WHERE {by} LIKE "%{txt}%"''')
        rows = self.c.fetchall()
        return rows

class ExamForStudent(db.Sqlite):
    __student_id = 0
    __exam_id = 0
    __grade = 0

    def __init__(self):
        self.connect()
        self.c = self.conn.cursor()

    # setters
    def setStudentId(self, par):
        self.__student_id = par

    def setExamId(self, par):
        self.__exam_id = par

    def setGrade(self, par):
        self.__grade = par

    def setMessage(self, par):
        self.__message = par

    def add_or_update_grade(self, id, grade):
        self.c.execute("UPDATE exam_for_student SET grade = ? WHERE id = ?", (grade, id))
        self.conn.commit()

    # getters
    def getStudentId(self):
        return self.__student_id

    def getExamId(self):
        return self.__exam_id

    def setGrade(self):
        return self.__grade

    def getMessage(self):
        return self.__message

    def getEFS(self):
        self.c.execute('''SELECT efs.id, student.last_name, exam.name, efs.grade, student.id, course.id 
                        FROM exam_for_student as efs 
                        INNER JOIN exam ON exam.id = efs.exam_id 
                        INNER JOIN student ON efs.student_id = student.id 
                        INNER JOIN course ON exam.course_id = course.id''')
        return self.c.fetchall()

    ### Za kazdym razem jak program dodaje egzamin to dla kazdego studenta danego kierunku w innej tabeli tworzy wiersz
    ### laczacy danego studenta i egzamin
    def createEFS(self, exam):

        egz = self.c.execute("SELECT * FROM exam WHERE name = ?", (exam, ))
        id_egzaminu = egz.fetchall()[-1][0]

        id_kierunkow = self.c.execute('''SELECT grade_course.id FROM exam 
                                           INNER JOIN course ON course.id = exam.course_id 
                                           INNER JOIN grade_course ON course.grade_course_id = grade_course.id 
                                           WHERE exam.name = ?''', (exam, ))
        id_kierunku = id_kierunkow.fetchall()[0][0]
        studenci = self.c.execute('''SELECT * FROM student 
                                       INNER JOIN grade_course ON student.grade_course_id = grade_course.id 
                                       WHERE grade_course.id = ?''', (id_kierunku, ))
        items = studenci.fetchall()
        id_studentow = []
        for item in items:
            id_studentow.append(item[0])
        number_of_items = len(items)

        for i in range(number_of_items):
            self.c.execute("INSERT INTO exam_for_student(student_id, exam_id) VALUES (?, ?)", (items[i][0], id_egzaminu))
            self.conn.commit()
