my_list = ['Guiness', 'Imperial', 'Pilsen', 'Orangeboom', 'Bavaria', 'Moosehead', 'Stella', 'Outtinger' ]
my_list = tuple(my_list)
print(my_list[1:6:2])

my_list=list(my_list)
my_list.remove('Guiness')
print(my_list)
my_list=tuple(my_list)
print(my_list[::-1])


list_of_tuples=[('Guiness', 9), ('Imperial', 6), ('Pilsen', 7), ('Orangeboom', 10), ('Bavaria',7) ]

def convert_to_tuple(tupla):
    dic= {}
    dic = dict(tupla)
    return dic

print('*****************************************')
print(convert_to_tuple(list_of_tuples))
