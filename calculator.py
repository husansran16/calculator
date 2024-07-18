def add_history(entery):
    file = open("History.txt","a")
    Add = file.write(entery + "\n")

def show():
    file = open("History.txt","r")
    his = file.readlines()
    if his:
        for line in his:
            print(line.strip())
    else:
        print("no history found:")





print("1-Addition\n2-Subtraction\n3-Division\n4-Multiplication\n5-Power\n6-Rounded\n7-show history\n-8-exit")
hus = True
while hus is True:
    Operator = int(input("Enter the operator:"))

    if Operator==0:
        exit()
    elif Operator == 8:
        print("history:")
        show()
    First = int(input("Enter First Number:"))
    if First == 00:
        print("closing the app")
        exit()
    Second = int(input("Enter Second Number:"))
    if Second == 00:
        print("closing the app")
        exit()
   
    elif Operator==1:
        Sum = First + Second
        Total = f"{First}+{Second}={Sum}"
        add_history(Total)
        print(Sum)
    elif Operator==2:
        Sum = First - Second
        Total = f"{First}-{Second}={Sum}"
        print(Sum)
    elif Operator==3:
        Sum = First/Second
        Total = f"{First}/{Second}={Sum}"
        print(Sum)
    elif Operator==4:
        Sum = First*Second
        Total = f"{First}x{Second}={Sum}"
        print(Sum)
    elif Operator==5:
        Sum = First**Second
        Total = f"{First}^{Second}={Sum}"
        print(Sum)
    elif Operator==6:
        Sum = First//Second
        Total = f"{First}//{Second}={Sum}"
        print(Sum)
    elif Operator==7:
        Sum = First%Second
        Total = f"{First}%{Second}={Sum}"
        print(Sum)
   
    else:
        print("Wrong Input Try again")