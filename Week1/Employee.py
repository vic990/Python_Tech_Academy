import os
import time

employee={'Victor': float(5000)}


def clean_screen():
    time.sleep(3)
    os.system('cls')  

#set the minimum salary for an employee if it is less than 5000
def setMinumumSalary(user):
    salary= float(5000)
    employee.setdefault(user,salary)
  
    
#add an employee
def addEmployee():
    controller=True  
    while controller:
            try:
                user= input("enter a name: ")  
                salary=float(input("enter salary: "))
                if salary < 5000:
                    setMinumumSalary(user)
                    print("Employee added.\n")
                    controller=False
                    
                else:
                    employee.setdefault(user, salary)        
                    print("Employee added.\n")
                    controller=False
            except:
                os.system('cls')  
                print("type a valid Data")
        

#search an employee 
def search_emp(user):    
    if user in employee.keys():
      print(f"Empleado: {user} \nSalario: {employee[user]} \n")
     
    else:
        print("-->> user not found <--\n")

#Show the whole list of employees   
def Show_employees(): 
    if bool(employee):   
        for users in employee:        
            print(users, ":",employee[users])
    else:
        print("The employee list is empty")
        clean_screen()

def menu():
    
    estate=True
    while estate:    
        
        try:
            os.system('cls') 
            print("1.Add employee:\n2.Search an employee\n3.Show employees\n4.Exit")
            option=int(input())
            if option == 1:
                    addEmployee()
                    clean_screen()          
                    menu()
            elif option==2:
                    user=input("Type a user name to search: ")
                    search_emp(user)
                    clean_screen()          
                    menu()
            elif option== 3:
                Show_employees()
                clean_screen()          
                menu()
                
            elif option == 4:
                print("Session ended\n")
                estate=False
                clean_screen()
                
        except ValueError:
           pass
        
  
menu()