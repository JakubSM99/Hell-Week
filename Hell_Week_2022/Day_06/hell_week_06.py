
# Magiczne kwadraty

# Napisz program, który sprawdzi, czy podany w pliku tekstowym kwadrat, jest kwadratem magicznym.

# To znaczy czy w każdej kolumnie, wierszu i po obu przekątnych suma wartości jest taka sama.

# Załóż, że w podanym pliku tekstowym znajduje się tylko 1 magiczny kwadrat.

# Dodatkowo niech program sprawdzi czy wszystkie wartości w kwadracie są unikalne.


list_a = []


with open("C:/Users/Jakub/Documents/GitHub/Hell-Week/Hell_Week_2022/Day_06/magic_square_1.txt") as f:
    for a in f.read():
        try:
            b = int(a)
            list_a.append(a)
        except:
            pass

lista_1 = []
lista_2 = []
lista_3 = []

for a in list_a[0:3]:
    lista_1.append(a)

for a in list_a[3:6]:
    lista_2.append(a)

for a in list_a[6:]:
    lista_3.append(a)

print(lista_1)
print(lista_2)
print(lista_3)
