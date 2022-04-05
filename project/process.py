from persona_class import Employee


 #employee1= Employee(503750420,"alonso","carballo sanchez", 8, 2500)



list_of_emps =[]


#add employee
def add_employee(id, name,last_name, salary_per_hour):   
    employee1 =Employee(id,name,last_name,salary_per_hour) 
    if verify_emp(id):
        print("\nEmployee already exist")
    else:
        list_of_emps.append({'ID': employee1.get_id(),
                         'Name': employee1.get_name(),
                         'Last_name': employee1.get_last_name(),                         
                         'Salary_per_hour': employee1.get_salary_per_hour() } )
        print("Employee added")
        
        
 #check if the employee is added and returns a bool   
def verify_emp(id):
    for emp in list_of_emps:
        if id == emp['ID']:
            return True
        else:
            return False
   
#delete Employee 
def delete_emp(id):
      if check_empty():
          print("There are no Employees.")
      else:
          cont=0
          for emp in list_of_emps:
              if emp['ID'] == id :                
                list_of_emps.pop(cont)               
              cont+=1   
          print("Employee deleted")
              
  
#check if list is empty, if not empty return false
def check_empty(listemps=list_of_emps):
    return not listemps 
    
#Search an employee
def search_emp(id):      
    if check_empty():
        print("No employees to show")       
    else:        
        for emp in list_of_emps:
            if emp['ID'] == id:            
                print(f'ID: {emp["ID"]}') 
                print(f'Name: {emp["Name"]}') 
                print(f'Last Name: {emp["Last_name"]}') 
                print(f'Salary per hour: {emp["Salary_per_hour"]}') 
        
         
                
                
#it calculates the salary     
def cal_salary(id):
    
    sub_total= lambda x,y :  x * y
    for emp in list_of_emps:
            if emp['ID'] == id:
              worked_hours=float(input("Amount of hours: "))
              salary = sub_total(worked_hours, emp['Salary_per_hour'])
              create_txt(emp['Name'],emp['Last_name'], salary)
              print("--> file created <--")     
                     
#creates the txt
def create_txt(name,last_name,salary):
    with open('P2 test.text',"w", encoding= 'utf-8') as myfile:
        # myfile.write('Esta es una linea agregada con write\n')
        # myfile.write('Esta otra linea agregada con write\n')        
        
        myfile.write(f'**==== Salary report by employee ======== \n')
        myfile.write(f'** Name: {name}\n')
        myfile.write(f'** Last Name: {last_name}\n')
        myfile.write(f'** Salary per hour: {salary}\n')


add_employee(503750420,"alonso","carballo sanchez", 2500)    
add_employee(234534535,"jose","carballo sanchez", 2500)  
add_employee(537485734,"vero","carballo sanchez", 200) 






#yield
def rango(start1, end, step=1):    
    while start1 <= end:               
        yield start1
        start1+=step
        


def show_all_emps():
    if check_empty():
        print("No employees to show")
    else:
        #comprehension list         
        list_var = [x for x in list_of_emps]
        for i in rango(0,len(list_var)-1):
            print("ID:", list_var[i]['ID'])
            print("Name:", list_var[i]['Name'])
            print("Last name:", list_var[i]['Last_name'])
            print("Salary per hour:", list_var[i]['Salary_per_hour'])
            print("*"*35)  
      
      
      

     
    