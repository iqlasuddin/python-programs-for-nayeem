import random
randomNumber=(random.randint(1,100))

flag=True

while(flag):
    num=int(input(('Guess a number between 1 & 100\n')))
    if(num<1 or num >100):
        print('Error! Please choose number between 1 & 100')
        continue
    if(num==randomNumber):
        print('Congrats, you guessed it right!')
        flag=False
    if(num<randomNumber):
        print("\nYour guess was too low!")
    if(num>randomNumber):
        print("\nYour guess was too high")

