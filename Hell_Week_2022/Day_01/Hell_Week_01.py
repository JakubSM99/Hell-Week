# 
# Gra w zgadywanie

# System losuje liczbę całkowitą z przedziału 1 do 256. Następnie prosi użytkownika o zgadnięcie liczby.
# Po każdorazowym wpisaniu liczby przez gracza system pokazuje informację:
# - "za mało", gdy podana liczba jest za niska
# - "za dużo", gdy podana liczba jest za wysoka

# Runda kończy się, gdy użytkownik poda poprawną liczbę. Użytkownik powinien mieć możliwość wyboru, czy chce zagrać jeszcze raz.
# 

import random 


def home():
    print("I have a number from 1 to 256. Do you want to take a guess?! (Yes/No)")
    answer(input())


def answer(yes_or_no):
    
    answer = yes_or_no.capitalize()

    try:
        if(answer == "Yes"):
            random_number = random.randrange(1, 257)
            print("Now take your guess:")
            count = 1
            try:
                guessed_number = int(input())
                game(random_number, guessed_number, count)

            except:
                smart_ass()

        elif(answer == "No"):
            print("OK, goodbye!")

        else:
            smart_ass()

    except:
        smart_ass()


def smart_ass():
    print("That's not what I've asked for!!! Do you really want to play? (Yes/No)")
    answer(input())


def game(random_number, guessed_number, counting):

    try:

        if(guessed_number < random_number):
            print("It's to Small, sorry... Try again!!!")
            new_guessed_number = int(input())
            new_counting = counting + 1
            game(random_number, new_guessed_number, new_counting)

        elif(guessed_number > random_number):
            print("It's to Big, sorry... Try again!!!")
            new_guessed_number = int(input())
            new_counting = counting + 1
            game(random_number, new_guessed_number, new_counting)

        elif(guessed_number == random_number):
            print("Wow, you guessed it!!! And it took you only:", counting, "times !!!")
            print("Do you want to play again? (Yes/No)")
            answer(input())

    except:
        print("That's a wrong answer. Try again!")
        new_guessed_number = int(input())
        new_counting = counting + 1
        game(random_number, new_guessed_number, new_counting)


home()