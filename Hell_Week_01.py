# Gra w zgadywanie

# System losuje liczbę całkowitą z przedziału 1 do 256. Następnie prosi użytkownika o zgadnięcie liczby.
# Po każdorazowym wpisaniu liczby przez gracza system pokazuje informację:
# - "za mało", gdy podana liczba jest za niska
# - "za dużo", gdy podana liczba jest za wysoka

# Runda kończy się, gdy użytkownik poda poprawną liczbę. Użytkownik powinien mieć możliwość wyboru, czy chce zagrać jeszcze raz.

import random 

x = random.randrange(1, 256)

print(x)