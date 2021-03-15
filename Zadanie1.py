
#deklaracja zmiennych
PythonYear = 1989

#pobieranie danych od uzytkownika
name = input("Podaj swoje imie: ")
age = int(input("Twój wiek: "))
actYear = int(input("Podaj aktualny rok: "))

PythonAge = actYear - PythonYear

if PythonAge < age:
    print("Witaj w moim świecie", name)
    print("Mów mi Python, mam", PythonAge, "lat. Jesteś starszy ode mnie.")
else:
    print("Witaj w moim świecie", name)
    print("Mów mi Python, mam", PythonAge, "lat. Jesteś młodszy ode mnie.")


