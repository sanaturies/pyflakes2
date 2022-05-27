
import random
def roll():
    num=random.randint(1,6)
    return num

def count(days,integer):
    total=0
    for i in range(days):
        for j in range(i):
            if roll()==integer:
                total+=1
    return total
print(count(365,3))

#20 of my friends love rolling dice. 
# They are all going to roll 1 die each tomorrow, 2 dice each two days from now, 3 dice each three days from now, and so on so that they roll a dice each a days from now.
#  But, one of my friends gets tired very quickly and he only rolls dice for 1 day and stops. 
# Another friend only will roll dice for 2 days, and another will roll dice for three days only, and so on up to the fact that my last friend will roll dice for 20 days.
#  In Python, simulate this. 
# How many times does someone roll 3 after everything?

#my answer
def counting(num_days,num):
    totals=0
    for day in range(1,num_days+1):
        people= num_days-(day-1)
        dice=people*day
        for i in range(dice):
            if roll()==num:
                totals+=1
    return totals
print(counting(20,3))

#thier answer
def counts(amount):
    count_ = 0
    for i in range(1, amount+1):
        if roll() == 3:
            count_ += 1
    return count_

def count2(amount):
    total = 0
    for i in range(1, amount + 1):
        total += counts(i)
    return total

def count3(amount):
    total = 0
    for i in range(1, amount + 1):
        total += count2(i)
    return total

print(count3(20))

#365 of my friends love rolling dice. They are all going to roll 1 die each tomorrow, 2 dice each two days from now, 3 dice each three days from now, and so on so that they roll a dice each a days from now.
# But, one of my friends gets tired very quickly and he only rolls dice for 1 day and stops. 
# Another friend only will roll dice for 2 days, and another will roll dice for three days only, and so on up to the fact that my last friend will roll dice for 365 days. 
# In Python, simulate this.
# How many times does someone roll 3 after everything?

#my answer
#print(counting(365,3))

#their answer
#print(count3(365))

