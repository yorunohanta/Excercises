#definicja funkcji wypisującej kolejne wyrazy ciągu Fibonacciego
def fibonacci(n):
    a = 0
    b = 1
    print(a, end=" ") #wypisujemy pierwszy wyraz ciągu
    while n > 1:
        print(b, end=" ") #wypisujemy kolejne wyrazy ciągu
        a, b = b, a + b #wyliczanie kolejnych wartości ciągu i zmiana przypisania
        n -= 1 #pomniejszenie wartości n o 1

#funkcja zwracająca n-ty wyraz ciągu
def Nwyraz(n):
    if n < 1:
        return 0
    if n < 2:
        return 1
    return Nwyraz(n-1) + Nwyraz(n-2)


n = int(input("Podaj ilość wyrazów ciągu: "))
fibonacci(n)
print("\nN-ty wyraz ciągu to: ", Nwyraz(n-1))







