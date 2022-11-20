
# Magiczne kwadraty

# Napisz program, który sprawdzi, czy podany w pliku tekstowym kwadrat, jest kwadratem magicznym.

# To znaczy czy w każdej kolumnie, wierszu i po obu przekątnych suma wartości jest taka sama.

# Załóż, że w podanym pliku tekstowym znajduje się tylko 1 magiczny kwadrat.

# Dodatkowo niech program sprawdzi czy wszystkie wartości w kwadracie są unikalne.

# def suma_w_lini(lista):
#     suma = 0
#     for var in lista:
#         suma += int(var)
#     return suma


# def suma_w_kolumnie(lista1, lista2, lista3, kolumna:int):
#     a = kolumna-1
#     suma = int(lista1[a]) + int(lista2[a]) + int(lista3[a])
#     return suma 

# def suma_przekatnej00x22(lista1, lista2, lista3):
#     suma = int(lista1[0]) + int(lista2[1]) + int(lista3[2])
#     return suma


# def suma_przekatnej20x02(lista1, lista2, lista3):
#     suma = int(lista3[0]) + int(lista2[1]) + int(lista1[2])
#     return suma

def spr_kolumn(lista1, lista2, lista3):
    kolumna_1 = int(lista1[0]) + int(lista2[0]) + int(lista3[0])
    kolumna_2 = int(lista1[1]) + int(lista2[1]) + int(lista3[1])
    kolumna_3 = int(lista1[2]) + int(lista2[2]) + int(lista3[2])

    if kolumna_1 == kolumna_2 and kolumna_1 == kolumna_3:
        suma_kolumn = kolumna_1 + kolumna_2 +kolumna_3
        print(suma_kolumn)
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
        print(suma_wierszy)
        return suma_wierszy
    else:
        a = "Kwadrat nie jest magiczny"
        return a
    
def spr_przekatnych(lista1, lista2, lista3):
    suma1 = int(lista1[0]) + int(lista2[1]) + int(lista3[2])
    suma2 = int(lista3[0]) + int(lista2[1]) + int(lista1[2])

    if suma1 == suma2:
        przekatne = suma1*3
        print(przekatne)
        return przekatne
    else:
        a = "Kwadrat nie jest magiczny"
        return a

with open("C:/Users/Jakub/Documents/GitHub/Hell-Week/Hell_Week_2022/Day_06/magic_square_1.txt") as f:
    
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

    if spr_kolumn(lista1, lista2, lista3) == spr_lini(lista1, lista2, lista3):
        if spr_kolumn(lista1, lista2, lista3) == spr_przekatnych(lista1, lista2, lista3):
            if spr_kolumn != "Kwadrat nie jest magiczny":
                print("kwadrat jest Magiczny")
            else:
                print("Kwadrat nie jest magiczny")
        else:
            print("Kwadrat nie jest magiczny")
    else:
        print("Kwadrat nie jest magiczny")

# kolumna_1 = suma_w_kolumnie(lista1, lista2, lista3, 1)
# kolumna_2 = suma_w_kolumnie(lista1, lista2, lista3, 2)
# kolumna_3 = suma_w_kolumnie(lista1, lista2, lista3, 3)

# linia_1 = suma_w_lini(lista1)
# linia_2 = suma_w_lini(lista2)
# linia_3 = suma_w_lini(lista3)

# przekatna_1 = suma_przekatnej00x22(lista1, lista2, lista3)
# przekatna_2 = suma_przekatnej20x02(lista1, lista2, lista3)

# print(kolumna_1)
# print(kolumna_2)
# print(kolumna_3)
# print(linia_1)
# print(linia_2)
# print(linia_3)
# print(przekatna_1)
# print(przekatna_2)
