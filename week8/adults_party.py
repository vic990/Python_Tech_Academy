
lista=[{'name': 'Jose', 'age':17, 'height_cm': 170},{'name': 'Andres', 'age':28, 'height_cm': 170}, 
      {'name': 'Irene', 'age':17, 'height_cm': 170}, {'name': 'Ana' , 'age':18, 'height_cm': 165}, 
      {'name': 'Lupe', 'age':16, 'height_cm': 181}, {'name': 'Jefferson', 'age':24, 'height_cm': 170}, 
      {'name': 'Jesus', 'age':27, 'height_cm': 179} ]
   


filtrado = list(filter(lambda p: True if p['age'] > 17 else False, lista))

for i in filtrado:
    print(i)

