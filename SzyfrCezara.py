# funkcja ord() zwraca numer w kodzie ASCII danego znaku
# funkcja chr() zwraca znak przypisany do danego numeru w kodzie ASCII

def szyfruj(tekst, klucz):
    zaszyfrowany = "" #na wstepie zaszyfrowana wiadomosc jest pusta
    for i in range(len(tekst)):
        if ord(tekst[i]) > 122 - klucz:
            zaszyfrowany += chr(ord(tekst[i]) + klucz - 26)
        else:
            zaszyfrowany += chr(ord(tekst[i]) + klucz)
    return zaszyfrowany

def deszyfruj(szyfr, klucz):
    odszyfrowany = ""
    for i in range(len(szyfr)):
        if (ord(szyfr[i]) - klucz < 97):
            odszyfrowany += chr(ord(szyfr[i]) - klucz + 26)
        else:
            odszyfrowany += chr(ord(szyfr[i]) - klucz)
    return odszyfrowany


tekst = input("Podaj wiadomosc do zaszyfrowania:\n")
klucz = int(input("Podaj klucz szyfrowania: "))
print("Zaszyfrowana wiadomość:\n", szyfruj(tekst, klucz))
zaszyfrowany = szyfruj(tekst, klucz)
print("Odszyfrowana wiadomość:\n", deszyfruj(zaszyfrowany, klucz))
