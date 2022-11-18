
# Metoda range_float

# Napisz metodę range_float, 
# zachowującą się identycznie jak metoda wbudowana range, 
# ale dla liczb zmiennoprzecinkowych.



# "Range" method makes steps by 1 in defalut,
# so I'm making them 0.1 for floats but it can easly be changed back to 1.0
def range_float(a: float, b: float, c=None):
    if c==None:
        list = []
        while a < b:
            d = round(a, 2)
            list.append(d)
            a += 0.1
        return list
    else:
        list = []
        while a<b:
            d = round(a, 2)
            list.append(d)
            a += c
        return list


# TEST: 
# a = range_float(1.0,12.5)
# b = range_float(0.2,10,0.3)

# print(a)
# print(b)

