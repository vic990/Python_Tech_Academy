

class Persona:
    
    def __init__(self, id, name, last_name):
        self.id=id
        self.name=name
        self.last_name=last_name
     
     
     
    def get_id(self):
          return self.id
    
    def get_name(self):
        return self.name
    
    def get_last_name(self):
        return self.last_name


class Employee(Persona):
    
    def __init__(self, id, name, last_name, Salary_per_Hour):
       Persona.__init__(self, id, name, last_name)       
       self.salary_per_hour = Salary_per_Hour
       
      
    def get_salary_per_hour(self):
        return self.salary_per_hour
   
        

