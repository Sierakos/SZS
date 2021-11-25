# TODO: Dodać możliwość modyfikowania danych
# TODO: Być może jakoś to uporządkować

import pandas as pd

class ConsoleView():
    def __init__(self, controller):
        self.controller = controller
        print("Aplikacja stworzona przez Sebastiana Sieradzkiego na potrzeby projektu")
        print("-"*50)

    def main(self):
        while True:
            print("System zarządzania studentami w wersji konsolowej")
            print("-"*50)
            print("1. Dodaj studenta")
            print("2. Usuń studenta")
            print("3. Wypisz aktywnych studentów")
            print("4. Dodaj kierunek studiów")
            print("5. Wypisz kierunki studiów")
            print("6. Usuń kierunek studiów")
            print("7. Dodaj przedmiot")
            print("8. Wypisz przedmioty")
            print("9. Usuń przedmiot")
            print("10. Dodaj egzamin")
            print("11. Wyświetl egzaminy")
            print("12. Usuń egzamin")
            print("13. Pokaż oceny z egzaminow")
            print("14. Zmień ocenę z egzaminu")
            print("15. Pokaż wykres przedmiotu")
            print("16. Stwórz plik o ocenach")
            print("q. Wyjdź")
            print("-"*50)
            x = input("Podaj opcje: ")

            if x == "1":
                fname = (input("Wpisz imie studenta, którego chcesz utworzyć: "))
                lname = (input("Wpisz nazwisko studenta, którego chcesz utworzyć: "))
                age = (input("Wpisz wiek studenta, którego chcesz utworzyć: "))
                phone = (input("Wpisz numer telefonu studenta, którego chcesz utworzyć: "))
                email = (input("Wpisz e-mail studenta, którego chcesz utworzyć: "))
                gcourse_id = (input("Wpisz id kierunku do którego chcesz dodać studenta: "))

                self.controller.add_student(fname, lname, age, phone, email, gcourse_id)
                print("Dodano studenta")

            elif x == "2":
                id = input("Wpisz id studenta, którego chcesz usunąć: ")
                self.controller.delete_student()
                print("Usunięto studenta")

            elif x == "3":
                rows = self.controller.display_all_students_data()
                print('Wszyscy studenci')
                print('-'*50)
                if rows:
                    df = pd.DataFrame(rows)
                    df.columns = ['id studenta', 'imie', 'nazwisko', 'wiek', 'nr_tel', 'email', 'kierunek', 'id kierunku']
                    df.drop('id kierunku', 1, inplace=True)
                    print(df)
                else:
                    print("Nie ma zadnych studentoww w bazie")
            elif x == "4":
                name = (input("Wpisz nazwę nowego kierunku: "))
                self.controller.add_gcourse(name)
                print("Dodano kierunek")
            elif x == "5":
                rows = self.controller.display_all_gcourse_data()
                print('Wszystkie kierunki')
                print('-'*50)
                if rows:
                    df = pd.DataFrame(rows)
                    df.columns = ['id kierunku', 'kierunek']
                    print(df)
                else:
                    print("Nie ma zadnych kierunkow w bazie")
            elif x == "6":
                id = input("Wbierz id kierunku, którego chcesz usunąć: ")
                self.controller.delete_gcourse(id)
                print("Usunięto kierunek")
            elif x == "7":
                gcourse_id = (input("Podaj id kierunku dla którego chcesz dodać przedmiot: "))
                name = (input("Podaj nazwe przedmiotu: "))
                self.controller.add_course(name, gcourse_id)
                print("Dodano przedmiot")

            elif x == "8":
                rows = self.controller.display_all_course_data()
                print('Wszystkie przedmioty')
                print('-'*50)
                if rows:
                    df = pd.DataFrame(rows)
                    df.columns = ['id przedmiotu', 'przedmiot', 'kierunek', 'id kierunku']
                    df.drop('id kierunku', 1, inplace=True)
                    print(df)
                else:
                    print("Nie ma zadnych przedmiotow w bazie")
            elif x == "9":
                id = input("Wbierz id przedmiotu, który chcesz usunąć: ")
                self.controller.delete_course(id)
                print("Usunieto przedmiot")
            elif x == "10":
                course_id = (input("Podaj id przedmiotu dla którego chcesz stworzyć egzamin: "))
                name = (input("Podaj nazwe egzaminu: "))
                self.controller.add_exam(name, course_id)
                print("Dodano egzamin")
              
            elif x == "11":
                rows = self.controller.display_all_exam_data()
                print('Wszystkie egzaminy')
                print('-'*50)
                if rows:
                    df = pd.DataFrame(rows)
                    df.columns = ['id egzaminu', 'egzamin', 'przedmiot', 'kierunek', 'id kierunku']
                    df.drop('id kierunku', 1, inplace=True)
                    print(df)
                else:
                    print("Nie ma zadnych egzaminow w bazie")
            elif x == "12":
                id = input("wybierz id egzaminu, który chcesz usunąć: ")
                self.controller.delete_exam(id)
                print("Usunieto egzamin")
            elif x == "13":
                rows = self.controller.display_all_efs_data()
                print('Wszystkie przedmioty')
                print('-'*50)
                if rows:
                    df = pd.DataFrame(rows)
                    df.columns = ['id', 'nazwisko studenta', 'egzamin', 'ocena', 'id studenta', 'id przedmiotu']
                    df.drop(['id studenta', 'id przedmiotu'], 1, inplace=True)
                    print(df)
                else:
                    print("Nie ma zadnych egzaminow w bazie")
            elif x == "14":
                id = input("Podaj id oceny: ")
                grade = input("Podaj ocenę z egzaminu[2.0, 3.0, 3.5, 4.0, 4.5, 5.0]: ")
                self.controller.add_or_update_grade(id, grade)
                print("Zmieniono ocene")
            elif x == "15":
                course_id = input("Wpisz id przedmiotu: ")
                self.controller.show_graph(course_id)
            elif x == "16":
                student_id = input("Podaj id studenta: ")
                self.controller.create_PDF(student_id)
            elif x == "q":
                break
