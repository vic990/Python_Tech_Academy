import os
import time

def clean_screen():
    time.sleep(3)
    os.system('cls') 
    

def convert_ascii(name):
    name_asci=[]
    for i in name:
         name_asci.append(ord(i))    
    return name_asci

def convert_uni(numbers):
    lista=list(numbers.split(" "))
    lista2=[]   
    for i in lista:
        lista2.append(chr(int(i)))
    print("".join(str(i)for i in lista2))

def menu():
    
    estate=True
    while estate:    
        
        try:
            os.system('cls') 
            print("1.convert To Ascii\n2.convert to unicode\n3.exit")
            option=int(input())
            if option == 1:
                    os.system('cls')
                    name=input("type a name to convert\n")
                    convert=convert_ascii(name)
                    print(convert)
                    clean_screen()          
                    menu()
            elif option==2:
                    numbers=input("Enter number by space\n")
                    convert_uni(numbers)
                    clean_screen()          
                    menu()
            elif option== 3:
                print("Session ended\n")
                estate=False
                clean_screen()              
           
               
                
        except ValueError:
           pass
       
menu()