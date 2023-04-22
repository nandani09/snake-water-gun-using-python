import random

def gamewin(comp , your):
    if comp == your:
        return None
    if comp == 's':
        if your == 'w':
            return False
        elif your == 'g':
            return True
    elif comp == 'w':
        if your == 's':
            return False
        elif your == 'g':
            return True
    elif comp == 'g':
        if your == 's':
            return False
        elif your == 'w':
            return True
    
    pass

print("comp's turn: snake(s) water (w) gun(g)?")
randNo =  random.randint(1,3)  
print(randNo)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
    
your =  input("player's  turn: snake(s) water (w) gun(g)?")
a= gamewin(comp,your)
print(f"computer choose {comp}")
print (f"you choose {your}")
if a == None:
    print("the game is a tie !")
elif a:
    print("you winn!")
else :
    print ("you loose")
        