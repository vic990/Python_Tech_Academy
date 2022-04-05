def multiplier(num):
    return lambda second_number: second_number* num

doubler=multiplier(2)

print(doubler(2))


#userinp = input('Ingrese la hilera:').lower()
string_starts_with_P= lambda : input("Ingrese una hilera ").lower().startswith('p') 
print(string_starts_with_P())