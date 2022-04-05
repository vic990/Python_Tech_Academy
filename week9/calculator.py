


def is_num(numeros2):
  
  try:    
      
    var5=int(numeros2[0])
    var6= int(numeros2[2])
    
    operacion(var5, var6)
    
  except ValueError:
    print("ingrese numeros validos")
    
 
      


   
def operacion(numero1,numero2):
   
     if operando == "+":
      result=numero1+numero2
      print(result)
     elif operando ==  "-":
        result=numero1-numero2
        print(result)
     elif operando ==  "*":
        result=numero1*numero2
        print(result)
     elif operando == "/":
         try:
            result=numero1/numero2
            print(result)
         except ZeroDivisionError:
            print("Operation not supported") 
     else:
        print("ingrese un numero valido")
    
    
numeros2 = input("ingrese los numeros y el operando: ").split(" ",2)
operando = numeros2[1]
is_num(numeros2)