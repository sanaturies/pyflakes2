
#like other taco shops but  A D V A N C E D  
#refined according to the thoughts in tacoshop_refined.py
import random
maindict={
    'tacodict':{
        'T':0,
        'F':4,
        'C':3,
        'B':2,
        'P':3,
        'BE':3},
    'shelldict':{
        'SH':0,
        'S':2,
        'H':3},
    'burritodict':{
        'BU':0,
        'B':2,
        'V':4,
        'C':3,
        'P':3,
        'BE':3},
    'saladdict':{
        'S':0,
        'C':4,
        'M':3,
        'CH':2,
        'G':3},
    'enchiladasdict':{
        'E':0,
        'BE':4.50,
        'C':3,
        'V':3,},
    'quesadillasdict':{
        'Q':0,
        'C':2,
        'V':3}
}
#mainlst=[maindict['tacodict'],maindict['shelldict'],burritodict,saladdict,enchiladasdict,quesadillasdict]
sidedict={
    'N':2,
    'R':1,
    'C':3,
    'CH':5
}
drinkdict={
    'M':2,
    'S':1,
    'J':2,
    'W':0,
    'T':1,
    'C':1,
    'H':3
}
salsadict={
    'G':3.50,
    'S':0.50
}
i=random.randint(0,50)
def execution(group,boleen,valid,question):
    dish=input(question)
    if dish=='cancel':
            return
    while dish.upper() not in valid:
        print('please pick a valid option',valid)
        dish=input(question)
        if dish=='cancel':
                return
    if boleen==True:
        num=input('how many %ss\n'%(dish))
        if num=='cancel':
            return
        else:
            while int(num) <= 0:
                print('please pick a non negitive non zero number')
                num=input('how many %ss\n'%(dish))
                if num=='cancel':
                    return
        return num
            #an idea:
            #try:
                #num = int("string")
            #except ValueError:
                    #raise ValueError("ValueError exception thrown")
    else:
        dish=dish.upper()
        return dish,group[dish]

def third_sub_dish(dct,question1,boleen):
    dish=input(question1)
    if dish=='cancel':
            return
    #purpose: find subdict
    for i in dct:
        for j in dct[i]:
            if dish.upper() in dct[i]:
                print(dct[i])
                break
        break
    
    while dish.upper() not in dct[i[j]]:
        print('please pick a valid option',j)
        dish=input(question1)
        if dish=='cancel':
            return
    sub_dish=input('what type of %s ? [%s]'%(dish,j))
    if boleen==True:
        num=input('how many %ss\n'%(dct[j[sub_dish]]))
        if num=='cancel':
            return
        else:
            while int(num) <= 0:
                print('please pick a non negitive non zero number')
                num=input('how many %ss\n'%(dct[j[sub_dish]]))
                if num=='cancel':
                    return
    else:
        sub_dish=sub_dish.upper()
        return sub_dish,dct[j[sub_dish]]

    '''if type(group)==dict:
            dish=dish.upper()
            return dish,num,group[dish]
        elif type(group)==list:
            i=valid.index(dish.upper())
            return dish,num,valid[i]'''



while True:
    print('\n---------------------------------\n---- WELCOME TO MY TACO SHOP ----\n---------------------------------\n')
    print('---------------------------------------------\ntype cancel at any point to cancel your order\n---------------------------------------------')
    print('\n***** Here\'s Our Menu ******\n')

    maincourse=third_sub_dish(maindict,'what would you like for your main dish?[(T)aco, (B)urrito, (S)alad, (E)nchilada, or (Q)uesadilla]\n',True)
    print(maincourse)
    #if maincourse[0]==

    ''' main=input('what would you like for your main dish?[(T)aco, (B)urrito, (S)alad, (E)nchilada, or (Q)uesadilla]\n')
    if main=='taco':
        taco=execution(tacodict,'taco',True,['F','C','B'],'Pick your choice of taco:\n(F)ish Taco......................$4\n(C)hicken Taco...................$3\n(B)ean & Cheese Taco.............$2 \n')
        if taco==None:
            print('order canceled')
            break
        else:
            shell=execution(shelldict,'shell',False,['S','H'],'Pick your choice of taco shell:\n(S)oft Taco Shell......................$2\n(H)ard Taco Shell...................$3\n')
    elif main=='burrito':
        burrito=execution(burritodict,'burrito',True,['B','V','C','P','Be'],'Pick your choice of burrito:\n(B)ean and Cheese Burrito......................$2\n(V)eggi Burrito...................$4\n(C)hicken Burrito .............$3 \n(P)ork Burrito.............$3\n (BE)ef Burrito.............$3')
        if burrito==None:
            print('order canceled')
            break
    elif main=='salad':
        salad=execution(saladdict,'salad',True,['c','M','CH','G',],'Pick your choice of salad:\n(C)hicken Salad......................$4\n(M)exican Salad...................$3\n(CH)icken Salad .............$2 \n(G)arden Salad.............$3\n')
        if salad==None:
            print('order canceled')
            break
    elif main=='enchilada':
        enchilada=execution(enchiladasdict,'enchilada',True,['BE','C','V'],'Pick your choice of enchilada:\n(BE)ef enchilada......................$4.50\n(C)hicken enchilada...................$3\n(V)eggi enchilada .............$3\n')
        if enchilada==None:
            print('order canceled')
            break
    elif main=='quesadilla':
        quesadilla=execution(quesadillasdict,'quesadilla',True,['C','V'],'Pick your choice of quesidilla:\n(C)hicken quesidilla......................$2\n(V)eggi quesadilla...................$3\n(CH)icken Salad .............$2\n')
        if quesadilla==None:
            print('order canceled')
            break'''
    side=execution(sidedict,True,['N','R','C','CH'],'Please pick a side for your order (every taco comes with one side, if you want to have differnt sides with differnt tacos please order it sepertely):\n (N)achos.........................$2\n (R)ice...........................$1\n (C)hips......................$3 \n (CH)urro......................$5\n')
    if side==None:
        print('order canceled')
        break
    drink=execution(drinkdict,False,['M','S','J','W','T','C','H'],'Pick a drink with your order (every taco comes with one drink, if you want to have differnt drinks with differnt tacos please order it sepertely):\n(M)ilk...........................$2\n (S)oda...........................$1\n (J)uice..........................$2\n(W)ater..........................$0\n(T)ea......................$1\n(C)offee......................$1\n(H)orchata......................$3\n ')
    if drink==None:
        print('order canceled')
        break
    print(side,drink)
    #total=(int(tacodict[taco[0].upper()])+int(sidedict[side.upper()])+int(drinkdict[drink.upper()]))*int(taco[1])
    #print('************************************\nThank you, your total is $',total,'\nYour order number is',i,'\n************************************\n')