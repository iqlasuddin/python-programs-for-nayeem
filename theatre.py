import os

while(1):   #using while(1) to let next customer continue use ctrl+z or ctrl+c to stop execution
    os.system('clear') #use os.system('cls') if using on windows machine
    age=int(input('Enter your age\n'))
    if(age<=12):
        print("Congrats, you got free pass for your kid!")
    if(age>12 and age <18):
        print("Please pay 10$")
    if(age>=18 and age <65):
        isMember=int(input('Do you have a membership card? Enter 1 for Yes and 0 for No\n'))
        if(isMember==1):
            print("Please pay $18")
        elif(isMember==0):
            print("Please pay $20")
        else:
            print("Invalid Entry")
    if(age>=65):
        print("You have Senior Discount, please pay $15")
    
    input("\n Press any key to continue..")

