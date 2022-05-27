
#give someone their hogwarts house based on thier answer to a question

ans_lst=[]
num=0

print('Welcome to HOGWART\'s SORTING HAT CEREMONY!')
print('Discover your house by answering a few questions about yourself.')
input('Press ENTER to start: (Enter your choice between 1 and 4 as appropriate)')
q1=input('Once every century, the Flutterby bush produces flowers that adapt their scent to attract the unwary. If it lured you, it would smell of: \n 1) The sea \n 2) Home \n 3) A crackling log fire \n 4) fresh parchment')
ans_lst.append(q1)
q2=input('If you were attending Hogwarts, which pet would you choose to take with you?\n 1) Cats \n 2) Toads  \n 3) Owls \n  4 Dragons ')
ans_lst.append(q2)
q3=input('What would you least liked to be called?\n 1) Ignorant \n  2) Cowardly \n 3) Selfish \n 4) Ordinary')
ans_lst.append(q3)
q4=input('If you could make a potion that would guarantee you one thing, what would it be? \n 1) Love \n 2) Glory \n 3) Wisdom \n 4) Power')
ans_lst.append(q4)
q5=input('Which road tempts you most? \n 1) The wide, sunny, grassy lane \n 2) The narrow, dark, lantern-lit alley \n 3) The twisting, leaf-strewn path through woods \n 4) The cobbled street lined with ancient buildings ')
ans_lst.append(q5)
q6=input('You enter an enchanted garden. What would you be most curious to examine first? \n 1) The silver leafed tree bearing golden apples \n 2) The fat red toadstools that appear to be talking to each other \n 3) The bubbling pool, in the depths of which something luminous is swirling \n 4) The statue of an old wizard with a strangely twinkling eye ')
ans_lst.append(q6)
q7=input('What kind of instrument most pleases your ear? \n 1) The violin \n 2) The trumpet \n 3) The piano \n 4) The drum')
ans_lst.append(q7)

for i in ans_lst:
    num=int(num)
    num+=i

if num<7:
    print('RAVENCLAW!')
elif num<14:
    print('HUFFELPUFF!')
elif num<21:
    print('GRYFINDOR!')
elif num<28:
    print('SLYTHERIN!')


