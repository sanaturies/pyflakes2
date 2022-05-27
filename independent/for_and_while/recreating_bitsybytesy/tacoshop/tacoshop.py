
#given an order, return the price.

'''
############################################################################################
thoughts for improvement:
    defs would be helpful in making the program shorter
    in each def the parameters would be: 
        the dictionary to cite,
        dish type
        boleen for asking how many (True = ask how many of dish, False = don't ask)
        valid options (list form)
        input question (string)
    each def would return: 
        what kind of dish (fish taco or bean and cheese, guac or rice, etc.)
        how many
        price of dish
    might put everything in a class so that the defs can communicate?????
############################################################################################
'''

tacodict={
    'F':4,
    'C':3,
    'B':2,
}
sidedict={
    'N':2,
    'R':1,
    'G':2,
}
drinkdict={
    'M':2,
    'S':1,
    'J':2,
    'W':0
}

i=0

print('\n---------------------------------\n---- WELCOME TO MY TACO SHOP ----\n---------------------------------\n')
print('\n***** Here\'s Our Menu ******\n')
while True:
    taco=input('Pick your choice of taco:\n(F)ish Taco......................$4\n(C)hicken Taco...................$3\n(B)ean & Cheese Taco.............$2 \n')
    while taco.upper() not in tacodict:
        print('please pick a valid option (F, C, B)')
        taco=input('Pick your choice of taco:\n(F)ish Taco......................$4\n(C)hicken Taco...................$3\n(B)ean & Cheese Taco.............$2 \n')
    taco_num=input('How many tacos?')
    while int(taco_num) <= 0:
        print('please pick a non negitive non zero number')
        taco_num=input('How many tacos?')
    side=input('Please pick a side for your order (every taco come with one side, if you want to have differnt sides with differnt tacos please order it sepertely):\n (N)achos.........................$2\n (R)ice...........................$1\n (G)uacamole......................$2 \n')
    while side.upper() not in sidedict:
        print('please pick a valid option (N, R, G)')
        side=input('Please pick a side for your order (every taco comes with one side, if you want to have differnt sides with differnt tacos please order it sepertely):\n (N)achos.........................$2\n (R)ice...........................$1\n (G)uacamole......................$2 \n')
    drink=input('Pick a drink with your order (every taco comes with one side, if you want to have differnt sides with differnt tacos please order it sepertely):\n(M)ilk...........................$2\n (S)oda...........................$1\n (J)uice..........................$2\n(W)ater..........................$0\n')
    while drink.upper() not in drinkdict:
        print('please pick a valid option (M,S,J,W)')
        drink=input('Pick a drink with your order (every taco comes with one drink, if you want to have differnt drinks with differnt tacos please order it sepertely):\n(M)ilk...........................$2\n (S)oda...........................$1\n (J)uice..........................$2\n(W)ater..........................$0\n')
    total=(drinkdict[drink.upper()]+sidedict[side.upper()]+tacodict[taco.upper()])*int(taco_num)
    i+=1
    print('************************************\nThank you, your total is $',total,'\nYour order number is',i,'\n************************************\n')