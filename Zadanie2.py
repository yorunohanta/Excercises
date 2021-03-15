
#pobieranie danych od uzytkownika
#poprzednie rozwiązanie
#number1 = int(input("Podaj pierwszą liczbę: "))
#number2 = int(input("Podaj drugą liczbę: "))
#number3 = int(input("Podaj trzecią liczbę: "))

powtorka = "t"
while powtorka == "t":
    number1, number2, number3 = input("Podaj trzy liczby oddzielone spacjami:").split(" ")
    print("Wprowadzone liczby:", number1, number2, number3)

    if number1 < number2:
        if number1 < number3:
            print("Najmniejsza liczba:", number1)
        else:
            print("Najmniejsza liczba:", number3)
    else:
        if number2 < number3:
            print("Najmniejsza liczba:", number2)
        else:
            print("Najmniejsza liczba:", number3)

    powtorka = input("Jeszcze raz (t/n)?")

