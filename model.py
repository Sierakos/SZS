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

    # getters
    def getName(self):
        return self.__name

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

    # getters
    def getName(self):
        return self.__name

    def getGradeCourseId(self):
        return self.__grade_course_id

class Exam():
    __name = ""
    __grade = 0
    __student_id = 0
    __course_id = 0


    def __init__(self):
        print("Dodano objekt przedmiotu")

    # setters
    def setName(self, par):
        self.__name = par

    def setGrade(self, par):
        self.__grade = par

    def setStudentId(self, par):
        self.__student_id = par

    def setCourseId(self, par):
        self.__course_id = par

    # getters
    def getName(self):
        return self.__name

    def getGrade(self):
        return self.__grade

    def getStudentId(self):
        return self.__student_id

    def getCourseId(self):
        return self.__course_id