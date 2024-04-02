import numpy as np
from random import choice
print("::A KayVeeZ Game::")
#outcome_array, Win = 1, Draw = 0, Lose = -1
# TODO : Add scoring system
a = np.array([[0, 1, -1],[-1 ,0 ,1],[1 ,-1 ,0]])
loop = 'Y'
while loop == 'Y' or loop =='y':
    list = [0, 1, 2] # 0 = snake, 1 = water, 2 = gun
    string_list = ['Rock', 'Scissors', 'Paper']

    cpu_choice = choice(list) #cpu chooses a number from list
    player_choice = input ('Please input your choice, "Rock, Paper or Scissors" : ')

    pc = player_choice.lower()
    pc1= pc.capitalize()
    print('Cpu chose :',string_list[cpu_choice],'And you chose:', pc1)
    ind = string_list.index(pc1)
    b = a [ind][cpu_choice]
    if b==1:
        print("You Win!")
        loop = input('Do you want to play again? Y/N : ')
    elif b==0:
        print("Draw!")
        loop = input('Do you want to play again? Y/N : ')
    elif b==-1:
        print("You Lose!")
        loop = input('Do you want to play again? Y/N : ')
else:
    z = input("Bye! See you later! Press enter to exit.....")
