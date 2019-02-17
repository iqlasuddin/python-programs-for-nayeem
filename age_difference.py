flag=True
while(flag):
    age1=int(input('Enter age of person1 \n'))
    if(age1<=0 or age1>150):
        print("Error!, Please enter the age between 0 and 150")
        continue
    innerFlag=True
    while(innerFlag):
        age2=int(input('Enter age of Person2 and older than 1 \n'))
        if(age2<=0 or age2>150):
            print("Error!, enter age 2 between 0 and 150")
            continue
        age_diff=age2-age1
        if(age_diff<=0):
            continue
        innerFlag=False
    flag=False
print('Difference between ages: ', age_diff)