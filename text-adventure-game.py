
def dining():
    print()
    print('You chose the dining room')
    print('You see a vase on the table')
    
    vaseChoice=input('Do you want to open the vase ?: ')
    while vaseChoice!='yes' or vaseChoice!='no':
        if(vaseChoice=='yes'):
            print('You have opened the vase, you see a pile of bones')
            print()
            rooms()
        elif(vaseChoice=='no'):
            print('You have decided not to open the vase')
            print('As you leave, you hear a cracking sound from the corner')
            print('You see a dark figure with glowing eyes')
            print('The dark figure then attacks you')
            print()
            print('YOU WAKE UP AND REALISE IT WAS ALL JUST A DREAM')
            print()
            input('GAME OVER. press enter to restart')
            print()
            rooms()
        else:
            vaseChoice=input("invalid choice, Type in 'yes' or 'no': ")

def living():
    print()
    print('As you walk in you see a sleeping pitbull, guarding a gold watch')
    pitbullChoice=input('Do you want to take the watch from the pitbull: ')
    while pitbullChoice!='yes' or pitbullChoice!='no':
        if(pitbullChoice=='yes'):
            print('You attempted to steal the watch, and now it attacks you')
            print('YOU ARE NOW DEAD')
            print()
            rooms()
        elif(pitbullChoice=='no'):
            print('You decided not to take the watch')
            print('You will leave to see another day')
            print()
            rooms()
        else:
            pitbullChoice=input("Invalid choice, Type in 'yes' or 'no': ")

def rooms():
    print('WELCOME TO THE HAUNTED MANSION')
    print()
    print('You are distant family member of a rich millionaire who has passed away, leaving the mansion to you')
    print()
    print('As the new owner, you decide to pay a visit')
    print()
    print('The house is dated, and it is falling apart. You walk in the front door')
    print()

    choice=input('Do you want to enter the living room or the dining room ?: ')
    while choice!='living room' or choice!='dining room':
        if(choice=='living room'):
            print('YOU HAVE ENTERED THE LIVIING ROOM')
            living()
        elif(choice=='dining room'):
            print('YOU HAVE ENTERED THE DINING ROOM')
            dining()
        else:
            choice=input('INVALID CHOICE, TYPE IN living room OR dining room: ')
rooms=rooms()



