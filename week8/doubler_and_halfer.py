lst1 = [3,5,7,8,9]
#doubler
def doubler(x):
    return x*2

resul= list(map(doubler,lst1))

print(resul)

result2 =list(map(lambda x :x*2,lst1))
print(result2)

#halfer
result3 =list(map(lambda x :x/2,lst1))
print(result3)