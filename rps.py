import random

 

foo = ['rock', 'paper', 'scissors']

 

play = random.choice(foo)

 

player = str(input("Enter your choice: "))

player = player.lower()

 

print(play)

 

if player == 'rock':

    if play == 'rock':

        print('It is a tie!')

    elif play == 'paper':

        print('You lost!')

    else:

        print('You won!')       

 

elif player == 'paper':

    if play == 'rock':

        print('You won!')

    elif play == 'paper':

        print('Its a tie!')

   else:

        print('You lost!') 

  

elif player == 'scissors':

    if play == 'rock':

        print('You lost!')

    elif play == 'paper':

        print('You won!')

    else:

        print('Its a tie!') 

    

else:

    print('input error')         

 

#print(player)

#print(play)

 

#if play == 'rock':

#    print(1)

#   

#elif play == 'paper':

#    print(2)

#   

#else:

#    print(3)       

    

