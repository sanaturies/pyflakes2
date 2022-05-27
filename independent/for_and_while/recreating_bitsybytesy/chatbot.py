
import random
import datetime

class Actions:   
    def coin():
        rand=random.randint(0,1)
        if rand==0:
            return 'heads'
        else:
            return 'tails'
    def time():
        x = datetime.datetime.now()
        return x.strftime("%X")
    def date():
        x = datetime.datetime.now()
        return x.strftime("%x")
    def flatter():
        rand=random.randint(0,3)
        if rand==0:
            return 'you are so smart!'
        elif rand==1:
            return 'you have great coding skills!'
        elif rand==2:
            return 'you are so nice!'
        elif rand==3:
            return 'you are amazing!'
        else:
            pass
    def joke():
        rand=random.randint(0,2)
        if rand==0:
            input('why did 6 afraid of 7?')
            return'becasue 7 ate 9!'
        elif rand==1:
            input('what do you call a sleeping dinosaur?')
            return 'dinoSNOREus'
        elif rand==2:
            input('how does a scientist freshen her breath?')
            return 'with expriMINTS'
    def age_on_mars():
        age=input('what is your age?')
        return int(age)/1.88
    def rain():
        return 'maybe?'
    def my_age():
        return 'I can\'t reveal that!'
    def horror():
        return 'you were born'
    def precept():
        rand=random.randint(0,2)
        if rand==0:
            return 'honesty is the best policy'
        if rand==1:
            return 'do unto others as you want others done to you'
        if rand==2:
            return 'be the change you want to see in the world'
    def food():
        return 'pizza!'
    def end():
        print('bye!')
    def help(commands1):
        print('Here\'s a list of commands I understand:')
        print('-'*60)
        for i in commands1:
            print(i)
        print('-'*60)

flag=True
name=input('hello, my name is ae! \n what\'s your\'s? ')
commands=['Flip a coin','What\'s the time?','what\'s today\'s date?', 'flatter me','tell me a joke','find my age on mars', 'is it going to rain today?','how old are you?', 'tell me a horror story','print me a precept','what\'s your fav food?','bye','nothing','see you','help']
print('nice to meet you '+name)
print('Here\'s a list of commands I understand:')
print('-'*60)
for i in commands:
    print(i)
print('-'*60)

def repeat(commands): 
    task=input('what can I do for you? ')
    flag=True
    if task==commands[0]:
        print(Actions.coin())
    elif task==commands[1]:
        print(Actions.time())
    elif task==commands[2]:
        print(Actions.date())
    elif task==commands[3]:
        print(Actions.flatter())
    elif task==commands[4]:
        print(Actions.joke())
    elif task==commands[5]:
        print(Actions.age_on_mars())
    elif task==commands[6]:
        print(Actions.rain())
    elif task==commands[7]:
        print(Actions.my_age())
    elif task==commands[8]:
        print(Actions.horror())
    elif task==commands[9]:
        print(Actions.precept())
    elif task==commands[10]:
        print(Actions.food())
    elif task==commands[11] or task==commands[12] or task==commands[13]:
        print(Actions.end())
        flag=False
    elif task==commands[14]:
        print(Actions.help(commands))
    else:
        print('i don\'t understand that')
    return flag

while repeat(commands)==True:
    repeat(commands)
