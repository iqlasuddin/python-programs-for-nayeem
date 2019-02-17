print("""
What is capital of France?

1. San Diego
2. California
3. Paris
""")

flag=True

while(flag):
    answer=int(input("Enter Choice\n"))
    if(answer==3):
        print("Congrats!")
        flag=False
    elif(answer==1 or answer==2):
        print("You are wrong!")
    else:
        print("Not chosen from options")