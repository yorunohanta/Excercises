# import funkcji z innego modułu
from Zadanie7ocenyfun import drukuj, srednia, mediana, odchylenie

przedmioty = set() #definicja pustego zbioru
oceny = [] #definicja pustej listy ocen
drukuj(przedmioty, "Lista przedmiotów: ")

#wprowadzanie przedmiotów przez uzytkownika
print("\nWciśnięcie Enter powoduje przerwanie wprowadzania przedmiotów.")
while True:
    przedmiot = input("Podaj nazwę przedmiotu: ")
    if len(przedmiot): #sprawdzamy czy użytkownik wprowadził przedmiot (jezeli nie wprowadzono zadnego znaku to przechodzimy do else)
        if przedmiot in przedmioty: #sprawdzamy czy przedmiot jest juz w zbiorze
            print("Ten przedmiot jest już wprowadzony.")
        przedmioty.add(przedmiot) #dodanie przedmiotu do zbioru
    else:
        drukuj(przedmioty, "\nWprowadzone przedmioty: ")
        przedmiot = input("\nZ ktorego przedmiotu chcesz wprowadzić oceny? ")
        if przedmiot not in przedmioty: #jezeli przedmiotu nie ma w zbiorze
            print("Brak przedmiotu w zbiorze, możesz go dodać.")
        else:
            break #wychodzimy z pętli

print("\nWprowadzenie wartości 0 spowoduje przerwanie wprowadzania ocen.")
ocena = None #zmienna sterująca pętlą

while not ocena:
    try:
        ocena = int(input("Podaj ocenę (1-6): "))
        if (ocena > 0 and ocena < 7): #sprawdzamy czy ocena jest z podanego zakresu
            oceny.append(float(ocena)) #jezeli tak to dodajemy ją do listy, przekształcając na float
        elif ocena == 0: #jezeli zostala wprowadzona wartosc 0 to przerywamy petle
            break
        else:
            print("Wprowadzono błędną ocenę.")
        ocena = None
    except ValueError:
        print("Wprowadzono błędne dane.")

drukuj(oceny, przedmiot.capitalize() + " - wprowadzone oceny: ")
s = srednia(oceny)
m = mediana(oceny)
o = odchylenie(oceny, s)
print("\nŚrednia ocen wynosi: {0:5.2f}".format(s))
print("Mediana wynosi: {0:5.2f}".format(m))
print("Odchylenie wynosi: (1:5.2f)".format(o))


        

