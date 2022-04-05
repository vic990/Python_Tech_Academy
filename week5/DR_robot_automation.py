from random import randint


class Robot:
    def __init__(self, name):
        self.name=name
        self.health_lvl= randint(1,100)
    
    def salute(self):
        print(f"Hello, I am robot called {self.name}")
        
    def i_need_a_doctor(self):
        if self.health_lvl >= 75:
            return True
        else:
            return False

class Doctor_robot(Robot):
    def __init__(self, name):
        super().__init__(name)
        
        
        
    def salute(self):
        print(f"I am a the Robot-DR {self.name} and I will help you today")
        
    def heal(self, robot2):
        robot2.health_lvl+=randint(1,15)
        if robot2.health_lvl > 100:
            robot2.health_lvl=100
        while robot2.health_lvl < 75:
            self.heal(self,robot2)
            
    
Dr_robot= Doctor_robot("Jose")
 
Dr_robot.salute()

all_robots={}

print("let's create 3 robots")

for i in range(0,3):
    
    name=input(f"Enter the name of the robot number {i}: ")
        
    robot= Robot(name)
    print(robot.health_lvl)
    print(robot.i_need_a_doctor())
    while robot.i_need_a_doctor() ==False:
     
      Doctor_robot.heal(Doctor_robot,robot)
      all_robots.setdefault(robot.name,robot.health_lvl)   
       
    all_robots.setdefault(robot.name,robot.health_lvl)
     

        
for robots in all_robots:
    print(robots, ":", all_robots[robots])
    
    

