import math

def srednia(oceny):
    suma = sum(oceny) #obliczamy sume ocen
    return float(suma / (len(oceny))) #zwracamy srednia czyli sume ocen podzielona przez ich ilosc w postaci zmiennopzecinkowej

def mediana(oceny):
    oceny.sort() #sortujemy oceny rosnąco
    if len(oceny) % 2 == 0: #sprawdzamy czy mamy parzysta czy nieparzysta liczbe ocen
        half = int(len(oceny) / 2) #wyznaczamy srodek listy ocen
        return float(oceny[half-1] + oceny[half] / 2.0)
    else:
        half = int(len(oceny) / 2)
        return oceny[half]

def odchylenie(oceny, srednia):
    temp = 0.0
    for ocena in oceny:
        temp += (ocena - srednia)*(ocena - srednia)
    w = temp / len(oceny)
    return math.sqrt(w)

def drukuj (co, kom=""): #funkcja przyjmuje co ma wypisać oraz jaki komentarz ma być przed wypisywanymi danymi
    print(kom)
    for i in co:
        print(i, end=" ")
