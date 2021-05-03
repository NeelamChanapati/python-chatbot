import random
greeting1 = ['Oh hey there!!','Hello techie!!','Hi there','Hello programmer']
#greeting2 = []
greeting3 = ['Welcome to the world of technology','Welcome to my world']
print('chat-bot> ' +random.choice(greeting1))
print('chat-bot> Good Afternoon!!')
print('chat-bot> I am a chat-bot, I speak and teach python')
print('chat-bot> May I know your good name please')
dummy = input('You> ')
print("chat-bot> I am sorry I did'nt hear you, Could you please repeat it?")
name = input('You> ')
print('chat-bot> Oh!! Hello ' +name)
ans = input('chat-bot> As I said I teach python. Do you want to learn my language ' +name+ ' ?\nyou> ')
if(ans == 'Yes') or (ans == 'yes') or (ans == 'Yeah') or (ans == 'yeah'):
    print('chat-bot> Great. Looks like a smart one')
else:
    print('chat-bot> Its Okay.') 
    print('chat-bot> Seems like You know everything about it.')
print('chat-bot> Lets check your level in this  language then')
print('chat-bot> What is your current level in python?(Ex. If you are a begginer enter 1 and vice versa.)')
level = int(input('1.Begginner\n2.Intermidiate\n3.Advanced\nyou> '))
if(level == 1 or level == 2 or level == 3):
    print('chat-bot> Perfect, now lets move on to the respective level')
if(level == 1):
    print('chat-bot> As a begginner I suggest you to go through the theory part or introduction part and websites to solve some basic problems like the one below')
    print('Its a simple basic program of calculator\n')
    x = float(input('Enter first number: '))
    y = float(input('Enter second number: '))
    print('Select operation: ')
    print('1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n')
    choice = int(input('Enter choice 1/2/3/4: '))
    if(choice == 1):
        print(str(x)+ ' + ' +str(y)+ ' = ' +str(x+y))
    elif(choice == 2):
        print(str(x)+ ' - ' +str(y)+ ' = ' +str(x-y))
    elif(choice == 3):
        print(str(x)+ ' * ' +str(y)+ ' = ' +str(x*y))
    elif(choice == 4):
        print(str(x)+ ' / ' +str(y)+ ' = ' +str(x/y))
    else:
        print('invalid input')
elif(level == 2):
    print('chat-bot> As you are in Intermidiate level its better to go to application part and polish your knowledge through learning')
    print('chat-bot> I can show you an example if you want(yes or no)\nyou> ')
    ans1 = input()
    if(ans1 == 'Yes') or (ans1 == 'yes'):
        print('chat-bot> Here is a basic python level game to guess a number')
        
        ran_num = random.randint(1, 100)
        print('chat-bot> You have only 7 chances')
        count = 0
        while (count < 7):
            count += 1
            guess = int(input('chat-bot> Guess a number between 1 and 100: '))
            if(ran_num == guess):
                print('chat-bot> Congratulations! You did it in ' +str(count)+ ' try')
                break
            elif(ran_num > guess):
                print('chat-bot> You guessed too small')
            else:
                    print('chat-bot> You guessed too high')
        if(count == 7):
            print('chat-bot> The number is ' +str(ran_num))
            print('chat-bot> Better luck next time!')
        print('chat-bot> So this is application level programming')
elif(level == 3):
    print('chat-bot> Its better for you to contribute to projects as an advanced python developer')
    print('chat-bot> Here is a poem that is written using python')
    bottles = int(input('Enter the number of bottles: '))
    word = 'bottles'
    while(bottles > 0):
        if(bottles == 1):
            word = 'bottle'
        print(str(bottles)+ ' ' +word+ ' of milk on the wall')
        print(str(bottles)+ ' ' +word+ ' of milk.')
        print('Take one down')
        print('Pass it around.')
        bottles = bottles - 1
        if(bottles > 0):
            print(str(bottles)+ ' ' +word+ ' of milk on the wall\n')
        else:
            print('No more bottles of milk on the wall\n')
print('chat-bot> Hope I gave you the required information as a python bot')
print('chat-bot> See you again, Bye!')
        

