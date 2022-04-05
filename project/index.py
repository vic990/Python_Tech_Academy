from pandas import value_counts
import process
import os
import time


def clean_screen():
    time.sleep(3)
    os.system('cls')  

def menu():
    
    estate=True
    while estate:    
        
        try:
            os.system('cls') 
            print("1.Add employee:\n2.Search an employee\n3.Delete employee\n4.Calculate Salary\n5.Show Employee list\n6.Exit")
            option=int(input())
            if option == 1:
                    os.system('cls')
                    print("=====Add employee======")
                    try:
                        id = int(input("ID: "))
                    except ValueError:
                        print("type only numbers")
                        time.sleep(3)                                                
                        menu()
                    name= input("name: ")
                    last_name = input("Last Name: ")
                    try:
                        Salary_hour = float(input("Salary per hour: "))
                    except ValueError:
                        print("\ntype only numbers")
                        time.sleep(4)                                                
                        menu()
                    process.add_employee(id, name, last_name, Salary_hour)
                    time.sleep(3)         
                    menu()
            elif option==2:                      
                    os.system('cls')
                    try:
                        print("=====Search Employee====")
                        id=int(input("Employee's ID: "))
                        process.search_emp(id)
                        time.sleep(3)           
                        menu()
                    except ValueError:
                        print("type only numbers")
                        time.sleep(3)                                                
                        menu()
            elif option == 3:
                os.system('cls')
                print("=====Delete employee======")
                try:
                    id = int(input("ID: ")) 
                    process.delete_emp(id)
                    time.sleep(3)           
                    menu()
                except ValueError:
                    print("type only numbers")
                    time.sleep(3)                                                
                    menu()
            elif option== 4:
                os.system('cls') 
                print("=====Create a Salary File======")
                try:
                    id = int(input("ID: "))
                    process.cal_salary(id) 
                    time.sleep(3)        
                    menu()
                except ValueError:
                    print("type only numbers")
                    time.sleep(3)                                                
                    menu()
            elif option == 5:
                os.system('cls')
                print("=====Employee List======")
                process.show_all_emps()
                time.sleep(5)                                                
                menu()
            elif option == 6:
                print("Session ended\n")
                estate=False            
                       
        except ValueError:
           pass
       
       
menu()