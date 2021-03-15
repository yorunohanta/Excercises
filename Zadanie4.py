n = input("Co którą grupę mam wyświetlić dane?:")
print("Alfabet w porządku naturalnym:")
x = 0
for i in range(65,91):
    litera = chr(i)
    x += 1
    tmp = litera + "=>" + litera.lower()
    if i > 65 and x % 5 == 0:
        x = 0
        tmp += "\n"
    print(tmp, end=" ") #ten end na koncu powoduje ze dane sa w jednej lini oddzielone spacja, bez tego grupuje po 5 liter ale wypisuje jedna pod druga

print("\nAlfabet w porządku odwróconym:")
y = 0
for j in range(122,96,-1):
    litera2 = chr(j)
    y += 1
    tmp2 = litera2 + "=>" + litera2.upper()
    if y == 5:
        y = 0
        tmp2 += "\n"
    print(tmp2, end=" ")