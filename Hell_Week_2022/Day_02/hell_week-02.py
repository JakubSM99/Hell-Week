
# Prosta analiza tekstu

# Do zadania będziesz potrzebować pliku tekstowego o nazwie content.txt. Do pliku możesz wpisać jakikolwiek, wieloliniowy tekst, który będziesz analizować.
# Ale jak nie chcesz wymyślać to tutaj proszę trochę treści dla Ciebie.

# Tom started to learn Python five months ago.
# He lives in London. He wants to be a programmer.
# Python is all he can think off right now.

# Zadanie 1.
# Z pliku tekstowego wypisz w konsoli, tylko linie ze słowem Python.

# Zadanie 2.
# Z pliku tekstowego wypisz w konsoli, słowa rozpoczynające się na literę podaną przez użytkownika.



list_a = []
list_b = []

# Gdy prubowałem zrobić po prostu open("hell_week_02.txt") to wyskakuje błąd,
# o nie możliwości znalezienia pliku lub directory, stąd takie rozwiązanie.

with open("C:/Users/Jakub/Documents/GitHub/Hell-Week/Hell_Week_2022/Day_02/hell_week_02.txt") as f:
    [list_a.append(line) for line in f.readlines()]
    
with open("C:/Users/Jakub/Documents/GitHub/Hell-Week/Hell_Week_2022/Day_02/hell_week_02.txt") as f: 
    [list_b.append(word) for word in f.read().split()]

for x in list_a:
    a = x.split()
    for i in a:
        if(i=="Python"):
            print(x)

def answer(letter):
    try:
        s = int(letter)
        print("wrong answer. Try again!")
        answer(input())
    except:
        y = letter.capitalize()
        for x in list_b:
            z = [*x]
            a = z[0].capitalize()
            if(a==y):
                print(x)


print("Give me a letter on which u want the words to begin:")
answer(input())

# tak wiem, nie jest według PEP8, 
# pierwsze zadanie poprawiłem by wyglądało zgodnie ze standardem 
# (przynajmniej tak mi się zdaje), niestety za to się za późno zabrałem,
# a nie skonfigurowałem jeszcze poprawnie Auto Formattera. Przepraszam!!!