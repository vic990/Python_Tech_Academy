
import process
import os
import time


def clean_screen():
    time.sleep(15)
    os.system('cls')  

def menu():
    estate = True
    
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
                       
                    name= input("name: ")
                    last_name = input("Last Name: ")
                    try:
                        Salary_hour = float(input("Salary per hour: "))
                    except ValueError:
                        print("\ntype only numbers for salary hours")
                        time.sleep(4)                                                
                        
                    process.add_employee(id, name, last_name, Salary_hour)
                    time.sleep(3)         
                    
            elif option==2:                      
                    os.system('cls')
                    print("=====Search Employee====")
                    if process.check_empty():
                        print("No employees to show")
                        
                        time.sleep(3)
                        
                    else:
                        try:                        
                            id=int(input("Employee's ID: "))
                            process.search_emp(id)
                            time.sleep(3) 
                            
                        except ValueError:
                            print("type only numbers")
                            time.sleep(3) 
                            
            elif option == 3:
                os.system('cls')
                print("=====Delete employee======")
                if process.check_empty():
                    print("No employees to show")
                    time.sleep(3)
                else:
                    try:
                        id = int(input("ID: ")) 
                        process.delete_emp(id)
                        time.sleep(3)
                        
                    except ValueError:
                        print("type only numbers")
                        time.sleep(3) 
                        
            elif option== 4:
                os.system('cls') 
                print("=====Create a Salary File======")
                if process.check_empty():
                    print("No employees to show")
                    time.sleep(3)
                else:
                    try:
                        id = int(input("ID: "))
                        process.cal_salary(id) 
                        time.sleep(3) 
                        
                    except ValueError:
                        print("type only numbers")
                        time.sleep(3)
                        
            elif option == 5:
                os.system('cls')
                print("=====Employee List======")
                process.show_all_emps()
                time.sleep(5)                                                
                
            elif option == 6:                            
                os.system('cls')
                print("Session ended\n")
                estate=False                                                              
               
                
                       
        except ValueError:
           os.system('cls') 
           time.sleep(3)
           print("type a valid option")
       
       
menu()