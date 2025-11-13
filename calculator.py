import time
def  add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul (a,b):
    return a*b

def div(a,b):
    if b ==0 :
        return "Error! The syntax is invalid"
    return a/b

try:
    Num1 = float(input("Enter 1st number: "))
    Num2 = float(input("Enter 2nd number: "))
except:
    print("!!This syntax is invalid!!")

print("Hey! Welcome to the calculator !!!\nYou have the following options......")
print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division")
try :
    choice = int(input("Enter the operation you desire to perform (1 , 2 , 3, 4 ): "))
except :
    print("INVALID SYNTAX!")
else:
    if choice == 1:
        print("The numbers are being added.....")
        time.sleep(1)
        result1 = add(Num1,Num2)
        print(f"The result is : {result1}")
    elif choice == 2:
        print("The numbers are being subtracted.....")
        time.sleep(1)
        result2 = sub(Num1,Num2)
        print(f"The result is : {result2}")
    elif choice == 3:
        print("The numbers are being multiplied.....")
        time.sleep(1)
        result3 = mul(Num1,Num2)
        print(f"The result is : {result3}")
    elif choice == 4:
        print("The numbers are being divided.....")
        time.sleep(1)
        result4 = div(Num1,Num2)
        print(f"The result is : {result4}")
print("Hurray! The operation is performed successfully")







