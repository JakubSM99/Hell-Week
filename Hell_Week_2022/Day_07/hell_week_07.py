# Obliczanie pola figur płaskich

# Napisz program do obliczania pola różnych figur płaskich.

# W pliku figures.txt w podanym formacie zapisane są nazwy figur i odpowiednie dane, potrzebne do obliczenia pola figury.

# Napisz kod, który odczyta dane z pliku i automatycznie obliczy pola figur. Następnie poszczególne pola figur wyświetli na ekranie.

# Figury, dla których Twój kod powinien działać to:
# - kwadrat
# - trójkąt
# - trapez
# - koło.

# Opcjonalnie:
# Dodatkowo stwórz metodę, która poda statystyki przeliczonych figur:
# - ile było poszczególnych rodzajów figur (np. 2 kwadraty, 4 koła itp)
# - minimalna, maksymalna i średnia wartość pola poszczególnych rodzajów figur płaskich (np. kwadrat — min. pole = 1, maks. pole = 64, śr. pole = 30,2 itp)

# UWAGA: Załóż, że w pliku figures.txt mogą znaleźć się figury, których pola program nie potrafi przeliczyć i obsłuż taką sytuację.


def kwadrat(a):
    pole = a*a
    return pole

def trojkat(a,h):
    pole = (a*h)/2
    return pole


def trapez(a,b,h):
    pole = ((a+b)*h)/2
    return pole


def kolo(r):
    pole = r*r*3.14
    return pole

def spr_figur(list_a):
    for x in list_a:
        try:
            if x[0] == "kwadrat":
                a = int(x[1].strip())
                pole = kwadrat(a)
                print("Pole kwadratu jest rowne: ", pole)


            elif x[0] == "trojkat":
                a = int(x[1])
                h = int(x[2].strip())
                pole = trojkat(a,h)
                print("Pole trojkata jest rowne: ", pole)


            elif x[0] == "trapez":
                a = int(x[1])
                b = int(x[2])
                h = int(x[3].strip())
                pole = trapez(a,b,h)
                print("Pole trapezu jest rowne: ", pole)


            elif x[0] == "kolo":
                r = int(x[1].strip())
                pole = kolo(r)
                print("Pole kola jest rowne: ", pole)

                
            else:
                print("Podanej figury nie potrafie policzyc")
        except:
            print("""Podane wartosci, lub liczba argumentow, 
                    nie sa zgodne ze schematem!""")   

def zliczanie_figur(list_a):
    kwadraty = 0
    trojkaty = 0
    trapezy = 0
    kola = 0
    inne = 0

    for x in list_a:
        try:
            if x[0] == "kwadrat":
                kwadraty += 1

            elif x[0] == "trojkat":
                trojkaty += 1

            elif x[0] == "trapez":
                trapezy += 1

            elif x[0] == "kolo":
                kola += 1
                
            else:
                inne += 0
        except:
            print("""Podane wartosci, lub liczba argumentow, 
                    nie sa zgodne ze schematem!""")  

    print("Tyle bylo kwadratow: ", kwadraty)
    print("Tyle bylo trojkatow: ", trojkaty)
    print("Tyle bylo trapezow: ", trapezy)
    print("Tyle bylo Kol: ", kola)
    print("Tyle bylo innych figur: ", inne)


def srednia_wartosc_pola(list_a):

    kwadraty = 0
    trojkaty = 0
    trapezy = 0
    kola = 0

    suma_pol_kwadratow = 0
    suma_pol_trojkatow = 0
    suma_pol_trapezow = 0
    suma_pol_kol = 0

    for x in list_a:
        try:
            if x[0] == "kwadrat":
                a = int(x[1].strip())
                pole = kwadrat(a)
                kwadraty += 1
                suma_pol_kwadratow += pole


            elif x[0] == "trojkat":
                a = int(x[1])
                h = int(x[2].strip())
                pole = trojkat(a,h)
                trojkaty += 1
                suma_pol_trojkatow += pole

            elif x[0] == "trapez":
                a = int(x[1])
                b = int(x[2])
                h = int(x[3].strip())
                pole = trapez(a,b,h)
                trapezy += 1
                suma_pol_trapezow += pole

            elif x[0] == "kolo":
                r = int(x[1].strip())
                pole = kolo(r)
                kola += 1
                suma_pol_kol += pole

            else:
                pass
        except:
            print("""Podane wartosci, lub liczba argumentow, 
                    nie sa zgodne ze schematem!""") 
    
    srednie_pole_kwadratow = suma_pol_kwadratow/kwadraty
    print("Srednie pole Kwadratow to: ", srednie_pole_kwadratow)

    srednie_pole_trojkatow = suma_pol_trojkatow/trojkaty
    print("Srednie pole trojkatow to: ", srednie_pole_trojkatow)

    srednie_pole_trapezow = suma_pol_trapezow/trapezy
    print("Srednie pole trapezow to: ", srednie_pole_trapezow)

    srednie_pole_kol = suma_pol_kol/kola
    print("Srednie pole kol to: ", srednie_pole_kol)

def czytanie_pliku(f):
    list_a = []

    for lines in f.readlines():
        a = lines.split(",")
        list_a.append(a)
    
    spr_figur(list_a)
    zliczanie_figur(list_a)
    srednia_wartosc_pola(list_a)

    

with open("C:/Users/Jakub/Documents/GitHub/Hell-Week/Hell_Week_2022/Day_07/figures.txt") as f:

    czytanie_pliku(f)
