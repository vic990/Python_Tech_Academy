class Persona:
    
    def __init__(self,name, last_name, age, weight, height):
        self.name= name
        self.last_name= last_name
        self.age= age
        self.weight = weight
        self.height= height
        
    def __str__(self):
        return f'My name is {self.name} {self.last_name} I am {self.age} my weight is {self.weight}KG and my height is {self.height}cm'

    def say_name(self):
            return print(f'My name is {self.name} {self.last_name}')
        
    def weight(self):
            return print(f'My weight is {self.weight}')
        
    def height(self):
         return print(f'My height is {self.height}')
     
        
        
        
persona_first= Persona('victor', 'carballo', 31, 65, 1.60)
persona_seond= Persona('Jose', 'Mora', 25, 70, 1.90)
persona_third= Persona('Jesus', 'Perez', 18, 90, 1.75)
print(persona_first)

print(persona_first.height)