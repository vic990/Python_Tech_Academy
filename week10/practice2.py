
#lst = [i // i for i in range(0,4)] #(create a try-except for the ZeroDivisionError)
lst2 = [[c for c in range(r)] for r in range(3)]
lst3 = [2 ** x for x in range(0, 11)]

#1
lista1=[]
for i in range(0,4):
    try:
        lista1.append(i//i)
        
    except(ZeroDivisionError):
        print("not divisible by ")
print(lista1)       
print("*" * 15)
#2
lista2=[]
for r in range(3):
    for c in range(r):
        lista2.append(c)
print(lista2)

print("*" * 15)

lista3=[]
for x in range(0,11):
    lista3.append(2 ** x)
    
print(lista2)