import random

dice = [1,2,3,4,5,6]

a = 0

user = int(input('How many dice do you want to roll: '))

while a < user :

      print(random.choice(dice))

      a = a + 1

      

