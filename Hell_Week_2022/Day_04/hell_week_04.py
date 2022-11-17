
# Zadanie 1

# Napisz metodę, która sprawdzi, czy podana wartość val znajduje się w liście liczb digits. Szkielet funkcji znajdziesz poniżej.


# from typing import List
# def f(val: int, digits: List[int]) -> bool
# # write code here
# pass

# W celu ułatwienia Ci zadania, poniżej masz kawałek kodu, który przygotuje Ci losowe liczby do testowania Twojej metody.
# from random import randint
# n = 10 # Liczba elementów do wylosowania
# digits_example = [randint(-1000, 1000) for _ in range(n)]


# * Możesz zaszaleć i zobaczyć jak długo Twój kod wykonuje się przy np. milionie elementów w liście. - Czy Twoje podejście jakkolwiek się zmieni, jeżeli wiesz, że liczba elementów będzie duża?


from typing import List
from random import randint

n = 1000 # Liczba elementów do wylosowania
digits_example = [randint(-1000, 1000) for _ in range(n)]

test = [1,2,3,4,5,6,7,8,9,10]

class Solution:
    def f(self, digits: List[int], var: int) -> str:
            for i in digits:
                if(var == i):
                    a = "Wartosc znajduje sie w liscie!"
                    return a
                else:
                    a = "Wartosc nie znajduje sie w liscie!"
                    return a
print("Wprowadz wartosc, ktora chcesz sprawdzic czy znajduje sie w liscie: ")
answer = int(input())
var = answer
s = Solution()
print(s.f(digits_example,var))
# print(s.f(test,var))


# Zadanie 2

# Użytkownik podaje liczbę w zakresie od 101 - 99999.
# Napisz program, który zamieni kolejnością cyfry w podanej liczbie.

# Przykład

# 365 -> 563
# 90238 -> 83209

print("Wprowadz liczbe, ktora chcesz odwrocic: ")

a = input()
b = ""

for i in reversed(a):
    b += i

print("Oto twoja odwrucona liczba: ", b)