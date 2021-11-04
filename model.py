class Student():
    __first_name = ""
    __last_name = ""
    __age = 0
    __phone = 0
    __email = ""
    __message = ""

    def __init__(self):
        print("Dodano objekt studenta")

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

    def setMessage(self, par):
        self.__message = par

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
    
    def getMessage(self):
        return self.__message

class GradeCourse():
    __name = ""

    def __init__(self):
        print("Dodano objekt kierunku studiów")

    # setters
    def setName(self, par):
        self.__name = par

    def setMessage(self, par):
        self.__message = par

    # getters
    def getName(self):
        return self.__name

    def getMessage(self):
        return self.__message

class Course():
    __name = ""
    __grade_course_id = 0


    def __init__(self):
        print("Dodano objekt przedmiotu")

    # setters
    def setName(self, par):
        self.__name = par

    def setGradeCourseId(self, par):
        self.__grade_course_id = par

    def setMessage(self, par):
        self.__message = par

    # getters
    def getName(self):
        return self.__name

    def getGradeCourseId(self):
        return self.__grade_course_id

    def getMessage(self):
        return self.__message

class Exam():
    __name = ""
    __course_id = 0


    def __init__(self):
        print("Dodano objekt egzaminu")

    # setters
    def setName(self, par):
        self.__name = par

    def setCourseId(self, par):
        self.__course_id = par

    def setMessage(self, par):
        self.__message = par

    # getters
    def getName(self):
        return self.__name

    def getCourseId(self):
        return self.__course_id

    def getMessage(self):
        return self.__message

class ExamForStudent():
    __student_id = 0
    __exam_id = 0
    __grade = 0

    def __init__(self):
        print("Utworzono obiekt egzaminu dla studentow")

    # setters
    def setStudentId(self, par):
        self.__student_id = par

    def setExamId(self, par):
        self.__exam_id = par

    def setGrade(self, par):
        self.__grade = par

    def setMessage(self, par):
        self.__message = par

    # getters
    def getStudentId(self):
        return self.__student_id

    def getExamId(self):
        return self.__exam_id

    def setGrade(self):
        return self.__grade

    def getMessage(self):
        return self.__message

    