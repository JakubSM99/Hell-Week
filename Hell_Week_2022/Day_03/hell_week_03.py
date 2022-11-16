# Gra w darta

# Dane wejściowe
# Plikiem wsadowym do zadania jest scores.csv. Pokazany pod treścią zadania.

# Treść

# Darek, Zdzisiek i Edek grali w rzutki i zapisali wyniki z 10 rozgrywek.

# Napisz program, który przeanalizuje tabelę z wynikami 
# poszczególnych rozgrywek zapisanych w pliku scores.csv 
# (1 linijka pliku = 1 rozgrywka).

# Osoba z największą liczbą punktów wygrywa.

# Punkty zdobywane za 1 rundę:
# +3 pkt — za wygraną (najwięcej punktów) w danej rozgrywce
# -1 pkt — za najgorszy wynik
# 0 pkt — w innych przypadkach

# Każda rozgrywka powinna być opisana, kto ile zdobył punktów.

# Po przeanalizowaniu wszystkich wyników program powinien 
# wyświetlić podsumowanie z końcowymi wynikami.

from csv import reader

list_darek = []
list_zdzisiek = []
list_edek = []

darek = 0
zdzisiek = 0
edek = 0

x = 0
y = 0

round = 1

with open("C:/Users/Jakub/Documents/GitHub/Hell-Week/Hell_Week_2022/Day_03/scores.csv", "r") as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    
    if header != None:
        for row in csv_reader:
            x += 1
            try:
                a = int(row[0])
                list_darek.append(a)
            except:
                a = 0 
                list_darek.append(a)
            try:
                a = int(row[1])
                list_zdzisiek.append(a)
            except:
                a = 0
                list_zdzisiek.append(a)
            try:
                a = int(row[2])
                list_edek.append(a)
            except:
                a = 0
                list_edek.append(a)


while y < x :
    print("Runda Nr: ", y+1)
    if(list_darek[y]>list_zdzisiek[y] and list_darek[y]>list_edek[y]):
        darek += 3
        print("Darek wygral runde")
        if(list_zdzisiek[y]>list_edek[y]):
            edek += -1
            print("Edek przegral runde")
            y += 1
        elif(list_edek[y]>list_zdzisiek[y]):
            zdzisiek += -1
            print("Zdzisiek przegral runde")
            y += 1
        else:
            print("Nikt nie przegral rundy")
            y += 1
    
    elif(list_zdzisiek[y]>list_darek[y] and list_zdzisiek[y]>list_edek[y]):
        zdzisiek += 3
        print("Zdzisiek wygral runde")
        if(list_darek[y]>list_edek[y]):
            edek += -1
            print("Edek przegral runde")
            y += 1
        elif(list_edek[y]>list_darek[y]):
            darek += -1
            print("Darek przegral runde")
            y += 1
        else:
            print("Nikt nie przegral rundy")
            y += 1

    elif(list_edek[y]>list_darek[y] and list_edek[y]>list_zdzisiek[y]):
        edek += 3
        print("Edek wygral runde")
        if(list_darek[y]>list_zdzisiek[y]):
            zdzisiek += -1
            print("Zdzisiek przegral runde")
            y += 1
        elif(list_zdzisiek[y]>list_darek[y]):
            darek += -1
            print("Darek przegral runde")
            y += 1
        else:
            print("Nikt nie przegral rundy")
            y += 1

    else:
        print("Nikt nie wygral rundy")
        if(list_darek[y]<list_zdzisiek[y] and list_darek[y]<list_edek[y]):
            darek += -1
            print("Darek przegral runde")
            y += 1
        elif(list_zdzisiek[y]<list_darek[y] and list_zdzisiek[y]<list_edek[y]):
            zdzisiek += -1
            print("Zdzisiek przegral runde")
            y += 1
        elif(list_edek[y]<list_darek[y] and list_edek[y]<list_zdzisiek[y]):
            edek += -1
            print("Edek przegral runde")
            y += 1
        else:
            print("Nikt nie przegral rundy")
            y += 1

print("Darek zdobył: " , darek , "punktów")
print("Zdzisiek zdobył: " , zdzisiek , "punktów")
print("Edek zdobył: " , edek , "punktów")

if(darek>zdzisiek and darek>edek):
    print("Darek wygral gre")
    if(zdzisiek>edek):
        print("Edek przegral gre")
    elif(zdzisiek<edek):
        print("Zdzisiek przegrał gre")
    else:
        print("Zdzisiek i Edek maja to samo miejsce")

elif(zdzisiek>darek and zdzisiek>edek):
    print("Zdzisiek wygral gre")
    if(darek>edek):
        print("Edek przegral gre")
    elif(darek<edek):
        print("Darek przegral gre")
    else:
        print("Darek i Edek maja to samo miejsce")

elif(edek>darek and edek>zdzisiek):
    print("Edek wygral gre")
    if(darek>zdzisiek):
        print("Zdzisiek przegral gre")
    elif(darek<zdzisiek):
        print("Darek przegral gre")
    else:
        print("Darek i Zdzisiek maja to samo miejsce")

else:
    if(darek<zdzisiek and darek<edek):
        print("Darek przegral gre")
        print("Zdzisiek i Edek maja to samo miejsce")
    elif(zdzisiek<darek and zdzisiek<edek):
        print("Zdzisiek przegral gre")
        print("Darek i Edek maja to samo miejsce")
    elif(edek<darek and edek<zdzisiek):
        print("Edek przegral gre")
        print("Darek i Zdzisiek maja to samo miejsce")
    else:
        print("Wszyscy maja to samo miejsce")
# 130x = 0 pkt. jako kara za nie prawidłowy zapis danych o zdobytych punktach.

# '' = 0 pkt. jako brak danych o zdobytych punktach.

# gdy 1 osoba ma więcej pkt., a pozostałe dwie mają tyle samo,
# to obie dostają 0 pkt., jako że żadna z nich nie ma najgorszego wyniku.

# gdy 1 osoba ma mniej pkt., a pozostałe dwie mają tyle samo, 
# to obie dostają 0 pkt., jako że żadna z nich nie ma najwięcej ponktów.