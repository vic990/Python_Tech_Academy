sample_list=[36, 32, 19, 65, 57, 39, 152, 639, 121, 44, 90, 190,96, 102]
lista_sample= list(filter(lambda divisible: (divisible % 8 == 0 or divisible % 13 ==0), sample_list))
print("Numbers divisible")
print(lista_sample)