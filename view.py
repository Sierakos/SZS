from model import Student
from controller import Controller

s = Student()
ctr = Controller()

# print('---------START PROGRAMU------------')
# s.setFname(input("Wpisz imie: "))
# s.setLname(input("Wpisza nazwisko: "))
# s.setAge(input("Wpisz wiek: "))
# s.setPhone(input("Wpisz nr. telefonu (opcjonalne): "))
# s.setEmail(input("Wpisz email (opcjonalne): "))
# ctr.Form(s)
# print(s.getMessage())

# ctr.getStudents()

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
    print("q. Wyjdź")
    print("-"*50)
    x = input("Podaj opcje: ")

    # Kod poniżej wymaga małej modyfikacji ale działa
    # Wymyślić sposób na zmienienie typów zmiennych
    if x == "1":
        s.setFname(input("Wpisz imie studenta, którego chcesz utworzyć: "))
        s.setLname(input("Wpisz nazwisko studenta, którego chcesz utworzyć: "))
        s.setAge(input("Wpisz wiek studenta, którego chcesz utworzyć: "))
        s.setPhone(input("Wpisz numer telefonu ucznia, którego chcesz utworzyć: "))
        s.setEmail(input("Wpisz e-mail ucznia, którego chcesz utworzyć: "))
        ctr.Form(s)
        print(s.getMessage())
        if ctr.Form(s) == True:
            fname = str(s.getFname())
            lname = str(s.getLname())
            age = int(s.getAge())
            phone = str(s.getPhone())
            email = str(s.getEmail())
            ctr.add_student_to_db(s, fname, lname, age, phone, email)
        else:
            pass
    elif x == "2":
        ctr.delete_student_from_db()
    elif x == "3":
        ctr.print_info_about_students()


    # Poniższe opcje jeszcze nie działają
    # Trzeba dodać validacje
    elif x == "4":
        kierunek = input("Wpisz nazwę nowego kierunku: ")
        ctr.add_grade_course_to_db(kierunek)
    elif x == "5":
        ctr.print_grade_courses()
    elif x == "6":
        id = input("Wbierz id kierunku, którego chcesz usunąć: ")
        ctr.delete_grade_course(id)
    elif x == "7":
        g_c_id = input("Podaj id kierunku dla którego chcesz dodać przedmiot: ")
        przedmiot = input("Podaj nazwe przedmiotu: ")
        ctr.add_course_to_db(przedmiot, g_c_id)
    elif x == "8":
        ctr.print_courses()
    elif x == "9":
        id = input("Wbierz id przedmiotu, którego chcesz usunąć: ")
        ctr.delete_course(id)
    elif x == "q":
        break

ctr.close_db()