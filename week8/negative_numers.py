lst=[-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7]


     
    
numeros = list(filter(lambda x: True if x < 0 or x> 4 else False, lst))
num=filter(lambda x: True if x < 0 or x> 4 else False, lst)

print(numeros)
print(num)


