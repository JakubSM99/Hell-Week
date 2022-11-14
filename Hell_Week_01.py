# Gra w zgadywanie

# System losuje liczbę całkowitą z przedziału 1 do 256. Następnie prosi użytkownika o zgadnięcie liczby.
# Po każdorazowym wpisaniu liczby przez gracza system pokazuje informację:
# - "za mało", gdy podana liczba jest za niska
# - "za dużo", gdy podana liczba jest za wysoka

# Runda kończy się, gdy użytkownik poda poprawną liczbę. Użytkownik powinien mieć możliwość wyboru, czy chce zagrać jeszcze raz.

import random 

def Home():
    print("I have a number from 1 to 256. Do you want to take a guess?! (Yes/No)")
    Answer(input())

def Answer(Yes_Or_No):
    
    Answer = Yes_Or_No.capitalize()

    try:
        if(Answer == "Yes"):
            Random_Number = random.randrange(1, 257)
            print("Now take your guess:")
            Count = 1
            try:
                Guessed_Number = int(input())
                Game(Random_Number, Guessed_Number, Count)
            except:
                SmartAss()

        elif(Answer == "No"):
            print("OK, goodbye!")
        else:
            SmartAss()
    except:
        SmartAss()
    
def SmartAss():
    print("That's not what I've asked for!!! Do you really want to play? (Yes/No)")
    Answer(input())

def Game(Random_Number, Guessed_Number, Counting):

    try:

        if(Guessed_Number < Random_Number):
            print("It's to Small, sorry... Try again!!!")
            New_Guessed_Number = int(input())
            New_Counting = Counting + 1
            Game(Random_Number, New_Guessed_Number, New_Counting)

        elif(Guessed_Number > Random_Number):
            print("It's to Big, sorry... Try again!!!")
            New_Guessed_Number = int(input())
            New_Counting = Counting + 1
            Game(Random_Number, New_Guessed_Number, New_Counting)

        elif(Guessed_Number == Random_Number):
            print("Wow, you guessed it!!! And it took you only:", Counting, "times !!!")
            print("Do you want to play again? (Yes/No)")
            Answer(input())

    except:
        print("That's a wrong answer. Try again!")
        New_Guessed_Number = int(input())
        New_Counting = Counting + 1
        Game(Random_Number, New_Guessed_Number, New_Counting)

Home()
