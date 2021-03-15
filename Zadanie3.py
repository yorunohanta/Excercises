import math #biblioteka matematyczna

powtorka = "t"
while powtorka == "t":
    dane = input("Podaj dlugosci boków oddzielone spacjami:") #pobranie danych
    lista = [] #definicja pustej listy
    for x in dane.split(" "):
        lista.append(int(x)) #dodanie elementu do listy
    a, b, c = lista
    # mozna to zamienic na wyrazenie a, b, c = [int(x) for x in dane.split(" ")]
    print("Podane długości boków:", a, b, c)

    if a + b > c and a + c > b and b + c > a:
        print("Z podanych boków można zbudować trójkąt.")
        if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
            print("I to prostokątny.")

        print("Obwód trójkąta wynosi:", (a + b + c))
        #obliczanie pola ze wzoru Herona
        p = 0.5 * (a + b+ c) #wspolczynnik
        pole = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("Pole trójkąta wynosi:", pole)
        op = "n"
    else:
        print("Z podanych odcinków nie można utworzyć trójkąta.")
        powtorka = input("Chcesz spróbować jeszcze raz? (t/n):")

