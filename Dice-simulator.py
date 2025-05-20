import random as r

repeat=True
while repeat:
    roll=input('press R to roll and enter to exit: ')
    if(roll.lower()=='r'):
        print(r.randint(1,6))
    else:
        break
