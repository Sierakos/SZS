from model import Student, Course, Exam, GradeCourse
from controller import Controller
import pandas as pd

ctr = Controller()

while True:
    print("-"*50)
    print("Dziennik zarządzania studentami")
    print("1. Dodaj studenta")
    print("2. Usuń studenta")
    print("3. Wypisz studentów")
    print("4. Dodaj kierunek studiów")
    print("5. Wypisz kierunki studiów")
    print("6. Usuń kierunek studiów")
    print("7. Dodaj przedmiot")
    print("8. Wypisz przedmioty")
    print("9. Usuń przedmiot")
    print("10. Dodaj egzamin")
    print("11. Wyświetl egzaminy")
    print("12. Usuń egzamin")
    print("13. Pokaz oceny z egzaminow")
    print("14. Pokaż wykres studenta")
    print("q. Wyjdź")
    print("-"*50)
    x = input("Podaj opcje: ")

    # Kod poniżej wymaga małej modyfikacji ale działa
    # Wymyślić sposób na zmienienie typów zmiennych
    if x == "1":
        s = Student()
        s.setFname(input("Wpisz imie studenta, którego chcesz utworzyć: "))
        s.setLname(input("Wpisz nazwisko studenta, którego chcesz utworzyć: "))
        s.setAge(input("Wpisz wiek studenta, którego chcesz utworzyć: "))
        s.setPhone(input("Wpisz numer telefonu ucznia, którego chcesz utworzyć: "))
        s.setEmail(input("Wpisz e-mail ucznia, którego chcesz utworzyć: "))
        if ctr.studentForm(s) == True:
            fname = str(s.getFname())
            lname = str(s.getLname())
            age = int(s.getAge())
            phone = str(s.getPhone())
            email = str(s.getEmail())
            ctr.add_student_to_db(s, fname, lname, age, phone, email)
        else:
            print(s.getMessage())
    elif x == "2":
        ctr.delete_student_from_db()
    elif x == "3":
        ctr.print_info_about_students()
    elif x == "4":
        kierunek = input("Wpisz nazwę nowego kierunku: ")
        ctr.add_grade_course_to_db(kierunek)
    elif x == "5":
        ctr.print_grade_courses()
    elif x == "6":
        id = input("Wbierz id kierunku, którego chcesz usunąć: ")
        ctr.delete_grade_course(id)
    elif x == "7":
        course = Course()
        course.setGradeCourseId(input("Podaj id kierunku dla którego chcesz dodać przedmiot: "))
        course.setName(input("Podaj nazwe przedmiotu: "))
        if ctr.courseForm(course) == True:
            ctr.add_course_to_db(course.getName(), course.getGradeCourseId())
            print(course.getMessage())
        else:
            print(course.getMessage())
    elif x == "8":
        ctr.print_courses()
    elif x == "9":
        id = input("Wbierz id przedmiotu, który chcesz usunąć: ")
        ctr.delete_course(id)
    elif x == "10":
        exam = Exam()
        exam.setCourseId(input("Podaj id przedmiotu dla którego chcesz stworzyć egzamin: "))
        exam.setName(input("Podaj nazwe egzaminu: "))
        if ctr.examForm(exam) == True:
            ctr.add_exam_to_db(exam.getName(), exam.getCourseId())
            print(exam.getMessage())
        else:
            print(exam.getMessage())
    elif x == "11":
        ctr.print_exams()
    elif x == "12":
        id = input("wybierz id egzaminu, który chcesz usunąć: ")
        ctr.delete_exam(id)
    elif x == "13":
        ctr.print_exam_for_student()
    elif x == "q":
        break

ctr.close_db()