import getpass
import os
import time

class Player:
    
    def __init__(self,choice=0):
        self.choice=choice
        self.score=0
        
    def set_score(self,score):
        self.score+= score
    
        
    def get_score(self):
        return self.score
   
    
    def get_choice(self):
       return self.choice
   
    def set_choice(self,choice):
      Player.choice=choice
 
        
  

def clean_screen():
    time.sleep(3)
    os.system('cls') 

    
score_t=1    
def Players_option(): 
       
        #print(f"Score player 1: {player1.get_score()}\nScore player 2: {player2.get_score()}")
        print("1.Paper \n2.Rock\n3.Scissors\n")
        op1= int(getpass.getpass("Player 1: "))
        global player1
        player1.set_choice(op1)  
        print(player1.choice)
        op2= int(getpass.getpass("Player 2: "))
        global player2
        player2.set_choice(op2)  
        #os.system('cls')        
        
        if  player1.get_choice() == 1 and  player2.get_choice() == 2:
                print('paper Player1 wins')        
                player1.score+=score_t 
                              
                print (player1.get_score()) 
                clean_screen()       
        elif player2.get_choice() == 1 and player1.get_choice() == 2:
                print('paper Player2 wins')
                
                player2.set_score(score_t)   
                print (player2.get_score())
                clean_screen()
        elif player1.get_choice()  == 2 and  player2.get_choice() == 3:
                print('rock Player1 wins')
                player1.set_score(score_t)
                print (player1.get_score())
                clean_screen()
        elif player2.get_choice() == 2 and player1.get_choice()  == 3:
            print('rock Player2 wins')        
            player2.set_score(score_t)
            print (player2.get_score())
            clean_screen()
        elif player1.get_choice() == 3 and  player2.get_choice() == 1:
                print('Scissors Player1 wins')
                player1.set_score(score_t)
                print (player1.get_score())
                clean_screen()
        elif player2.get_choice() == 3 and player1.get_choice()  == 1:
            print('Scissor Player2 wins')
            player2.set_score(score_t)
            print (player2.get_score())
            clean_screen()
        
      




def menu():
   estate=True
   player1=Player()
   player2=Player()
   while estate:
    try:
        os.system('cls')
        print("1.Play \n2.exit ")
        option=int(input())
        if option==1:
           #os.system('cls')
           Players_option()
          
        else:
            estate=False
    except:
           pass
    
menu()