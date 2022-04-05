class Person:
    def __init__(self,first_name, last_name,phone_numer,hobbies):
        self.first_name=first_name
        self.last_name=last_name
        self.phone_number=phone_numer
        self.hobbies=hobbies
        
    def get_full_name(self):        
        return self.first_name, self.last_name
    
    def get_additional_info(self):
         
        return {'phone_number': self.phone_number,'hobbies': self.hobbies}
    
class Developer(Person):
    def __init__(self,first_name, last_name,phone_numer,hobbies,github_username, area_of_expertise):
        Person.__init__(self,first_name, last_name,phone_numer,hobbies)
        self.github_username=github_username
        self.area_of_expertise=area_of_expertise

    def welcome_developer(self):
     print(f"Developer's name: {self.first_name} {self.last_name},\nArea of expertise: {self.area_of_expertise},\nGithub Username: {self.github_username}")
        
        
developer1 = Developer("victor", "Carballo", 83702578, "beer", "vic990", "CX support")

print(developer1.get_full_name())