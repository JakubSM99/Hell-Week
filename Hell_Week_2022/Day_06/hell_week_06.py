# Magiczne kwadraty

# Napisz program, który sprawdzi, czy podany w pliku tekstowym kwadrat, jest kwadratem magicznym.

# To znaczy czy w każdej kolumnie, wierszu i po obu przekątnych suma wartości jest taka sama.

# Załóż, że w podanym pliku tekstowym znajduje się tylko 1 magiczny kwadrat.

# Dodatkowo niech program sprawdzi czy wszystkie wartości w kwadracie są unikalne.


def spr_kolumn(lista1, lista2, lista3):
    kolumna_1 = int(lista1[0]) + int(lista2[0]) + int(lista3[0])
    kolumna_2 = int(lista1[1]) + int(lista2[1]) + int(lista3[1])
    kolumna_3 = int(lista1[2]) + int(lista2[2]) + int(lista3[2])

    if kolumna_1 == kolumna_2 and kolumna_1 == kolumna_3:
        suma_kolumn = kolumna_1 + kolumna_2 +kolumna_3
        # print(suma_kolumn)
        return suma_kolumn
    else:
        a = "Kwadrat nie jest magiczny"
        return a


def spr_lini(lista1, lista2, lista3):
    suma1 = 0
    suma2 = 0
    suma3 = 0

    for var in lista1:
        suma1 += int(var)
    for var in lista2:
        suma2 += int(var)
    for var in lista3:
        suma3 += int(var)
    
    if suma1 == suma2 and suma1 == suma3:
        suma_wierszy = suma1 + suma2 + suma3
        # print(suma_wierszy)
        return suma_wierszy
    else:
        a = "Kwadrat nie jest magiczny"
        return a


def spr_przekatnych(lista1, lista2, lista3):
    
    suma1 = int(lista1[0]) + int(lista2[1]) + int(lista3[2])
    suma2 = int(lista3[0]) + int(lista2[1]) + int(lista1[2])

    if suma1 == suma2:
        przekatne = suma1*3
        # print(przekatne)
        return przekatne
    else:
        a = "Kwadrat nie jest magiczny"
        return a


def unikalne(lista):
    if len(set(lista)) == len(lista):
        print("Wartosci kwadratu sa unikalne")
    else:
        print("Wartosci kwadratu nie sa unikalne")


def kwadrat_magiczny(lista1, lista2, lista3):
    if spr_kolumn(lista1, lista2, lista3) == spr_lini(lista1, lista2, lista3):
        if spr_kolumn(lista1, lista2, lista3) == spr_przekatnych(lista1, lista2, lista3):
            if spr_kolumn(lista1, lista2, lista3) != "Kwadrat nie jest magiczny":
                print("kwadrat jest Magiczny")
            else:
                print("Kwadrat nie jest magiczny")
        else:
            print("Kwadrat nie jest magiczny")
    else:
        print("Kwadrat nie jest magiczny")


def dzialania_na_kwadracie(f):
    
    list_a = []
    lista1 = []
    lista2 = []
    lista3 = []

    for a in f.read():
        try:
            b = int(a)
            list_a.append(a)
        except:
            pass

    for a in list_a[0:3]:
        lista1.append(a)

    for a in list_a[3:6]:
        lista2.append(a)

    for a in list_a[6:]:
        lista3.append(a)

    kwadrat_magiczny(lista1, lista2, lista3)

    unikalne(list_a)


# Kod działa tylko dla kwadratów 3x3, nie robiłem wersji ogólnej,
# ale jeśli będzie trzeba, lub jak będę miał czasu więcej to z chęcią zrobię

with open("C:/Users/Jakub/Documents/GitHub/Hell-Week/Hell_Week_2022/Day_06/magic_square_1.txt") as f:
    print("Odp. Dla 'Magic_square_1.txt' : ")
    dzialania_na_kwadracie(f)

with open("C:/Users/Jakub/Documents/GitHub/Hell-Week/Hell_Week_2022/Day_06/magic_square_2.txt") as f:
    print("Odp. Dla 'Magic_square_2.txt' : ")
    dzialania_na_kwadracie(f)