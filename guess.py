from random import *

a = int(input("What is the highest number the system can generate: "))
b = randint(1, a)


d = 3

while d > 0:
    c = int(input("Guess what the system generated: "))
    if c == b:
        print(f"Congrats, {c} is the correct answer")
        exit()
    else:
        print("Wrong answer")
        d -= 1

print("Game over")