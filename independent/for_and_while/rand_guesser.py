
#Write a program that generates a random number (0-10) and ask you to guess it. You have three guesses.
def r():
    import random
    rand=random.randint(0,10)
    print('rand=',rand)
    guess_count=3
    found = False
    for i in range(guess_count,0,-1):
        guess=input('number? ')
        print('guess=',guess)
        guess=int(guess)
        if (guess == rand):
            found = True
            break
     
     
    if found:
        print ("you won")
    else:
        print ('you lost!')
        
    return
                
#r()

#rand guesser enhanced
def r():
    import random
    rand=random.randint(0,10)
    print('rand=',rand)
    guess_count=3
    found = False
    for i in range(guess_count,0,-1):
        guess=input('number? ')
        print('guess=',guess)
        guess=int(guess)
        if (guess == rand):
            found = True
            break
        elif guess<rand:
            print('guess higher')
        else:
            print('guess lower')
     
     
    if found:
        print ("you won")
    else:
        print ('you lost!')
        
    return
                
r()
