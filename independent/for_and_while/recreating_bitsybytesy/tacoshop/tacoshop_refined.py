
#given an order, return the price.
#refined according to the thoughts in tacoshop.py

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
def execution(dct,type,boleen,valid,question):
    dish=input(question)
    if dish=='cancel':
            return
    while dish.upper() not in dct:
        print('please pick a valid option',valid)
        dish=input(question)
    if boleen==True:
        print('how many %ss'%(type))
        num=input()
        if num=='cancel':
            return
        while int(num) <= 0:
            print('please pick a non negitive non zero number')
            many='How many ',type,'?'
            num=input(many)
        return dish,num
    else:
        return dish
# attempted to automate total calculation
'''def total_calculation(dicts,dishes):
    total=0
    for i in range(len(dicts)):
        total+=int(dicts[i[dishes[i[0].upper()]]])
    return total
    total=(int(tacodict[taco[0].upper()])+int(sidedict[side.upper()])+int(drinkdict[drink.upper()]))*int(taco[1])'''
while True:
    print('\n---------------------------------\n---- WELCOME TO MY TACO SHOP ----\n---------------------------------\n')
    print('---------------------------------------------\ntype cancel at any point to cancel your order\n---------------------------------------------')
    print('\n***** Here\'s Our Menu ******\n')
    taco=execution(tacodict,'taco',True,['F','C','B'],'Pick your choice of taco:\n(F)ish Taco......................$4\n(C)hicken Taco...................$3\n(B)ean & Cheese Taco.............$2 \n')
    if taco==None:
        print('order canceled')
        break
    side=execution(sidedict,'side',False,['N','R','G'],'Please pick a side for your order (every taco comes with one side, if you want to have differnt sides with differnt tacos please order it sepertely):\n (N)achos.........................$2\n (R)ice...........................$1\n (G)uacamole......................$2 \n')
    if side==None:
        print('order canceled')
        break
    drink=execution(drinkdict,'drink',False,['M','S','J','W'],'Pick a drink with your order (every taco comes with one drink, if you want to have differnt drinks with differnt tacos please order it sepertely):\n(M)ilk...........................$2\n (S)oda...........................$1\n (J)uice..........................$2\n(W)ater..........................$0\n')
    if drink==None:
        print('order canceled')
        break
    total=(int(tacodict[taco[0].upper()])+int(sidedict[side.upper()])+int(drinkdict[drink.upper()]))*int(taco[1])
    print('************************************\nThank you, your total is $',total,'\nYour order number is',i,'\n************************************\n')

    '''
--------------------------------------------------------------------------------------------------------------------
    accept costomer name
    conferming order
    more food!
        main dishes:
            more tacos
            burritos
            salad
            Enchiladas
        more sides:
            chips
            churros
        drinks:
            tea
            horchata
            coffee
            alcohol????
        salsa:
            guac is now in the salsa section
            salsa of various spicyness (why do you even bother, mild, medium, hot, fire, carolina reaper)
            might get rid of the first and second one
    generate a random order number
    give option to have a main dish without a side but no side without main dish
        try to do the thing where you accept the all the tacos side dishes in one order
    drink refills? (charge extra)
    make the second iteration of the menu optional
--------------------------------------------------------------------------------------------------------------------
'''


