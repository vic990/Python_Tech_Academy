import os
import time



def clean_screen():
    time.sleep(5)
    os.system('cls') 
    
    
    
with open('my_py2_file.txt',"w", encoding= 'utf-8') as myfile:
    
    for i in range(1,10):
      myfile.write(f'{i}Prueba\n')
 
    


def read_first_line():
    os.system('cls')
    myfile=open('my_py2_file.txt','r')
    opt=int(input("How many lines do you want to read: "))    
    for i in range(opt):
        print(myfile.readline(),end='')
    clean_screen()
    
def append_lines():
    os.system('cls')
    opt=input("Please write something to add it: ")  
    with open('my_py2_file.txt',"a+", encoding= 'utf-8') as myfile:
     myfile.write(opt+'\n')    
     myfile.seek(0)     
     for i in myfile:
         print(i,end='')
    clean_screen()
    menu()
     
def read_n_lines():
   os.system('cls')
   print("up the last line, how many lines do you wanna see?\n")
   opt3=int(input())   
   with open('my_py2_file.txt',"r+", encoding= 'utf-8') as myfile:
       for line in (myfile.readlines() [-opt3:]):
           print(line, end='')
   

def read_text_list():
    os.system('cls')
    myfile= open('my_py2_file.txt')
    new_list=myfile.readlines()
    lista=len(new_list)
    data_list= new_list[0:lista]
    print(data_list)
    myfile.close()

 
    
    
    
def menu():    
    estate=True
    
    while estate:  
        os.system('cls')
        print("1.Read first lines\n2.add more text to the file\n3.Read a number of lines\n4.Get the whole text into a list\n5.Exit")
        option=int(input())  
        
        try:
            
            if option == 1:
                    read_first_line()    
                    
            elif option==2:                   
                    append_lines()                    
                    menu()
            elif option== 3:
                read_n_lines()
                clean_screen()          
                
                
            elif option == 4:
                read_text_list()
                clean_screen()
            
                
            elif option == 5:
                os.system('cls')
                print("Session ended\n")
                estate=False
                
        except ValueError:
            estate=False
        
        
menu()