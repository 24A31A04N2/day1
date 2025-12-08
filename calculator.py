a = int(input("enter first number :"))
b = int(input("enter second number :"))
op =input()
if(op=="sum"):
    print(a+b)
elif(op=="sub"):
    print(a-b)
elif(op=="mul"):
    print(a*b)
elif(op=="div"):
    print(a/b)
else:
    print("invalid")