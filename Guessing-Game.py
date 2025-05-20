import random as r

number=r.randint(1,20)
a=0
print('Guess number between 1 and 20')
print()
while a!=number:
    a=int(input('Guess number: '))
    if(a>number):
        print('Guess lower')
    elif(a<number):
        print('Guess Higher')
    elif(a==number):
        print('You Won')
        print('Game Over')
        
