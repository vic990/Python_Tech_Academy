
while True:

    try:

        num1 = int(input('introduzca el numero: '))
        num2 = int(input('introduzca el otro numero:'))
        print(f'{num1}/{num2} = {num1/num2}')
    except(TypeError, ValueError): # puedo meter varios tipos dentro del mismo parentesis separados por comas
        print('valor inmvalido')
    except ZeroDivisionError: # o los puedo poner por separados para enviar un mensaje error especifico.
        print("no se puede dividir entre cero")
    else:
        print("nada")










