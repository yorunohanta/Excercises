from random import randint

ile = int(input("Ile liczb wylosować? "))
lista = [] #tworzenie pustej listy
for i in range(0, ile):
    lista.append(randint(0, 100)) #dodawanie loswej wartości do listy

print("Zawartość listy ([index] wartość):")
for i, l in enumerate(lista):
    print("[", i, "]", l)

print("Zawartość listy w odwrotnej kolejności:")
for j in reversed(lista):
    print(j, end=" ")

print("\nPosortowana zawartośc listy:")
for e in sorted(lista):
    print(e, end=" ")

