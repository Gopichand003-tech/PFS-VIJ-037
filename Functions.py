#Functions
#1.A function is block of organized,re usable code and that is used to perform a single or  multiple task
#2.python gives inbuilt functions like print,you can make your own function also and these are called user defined functions
#3.python block begin with keyword def followed by the function name and paranthesis(())

'''a=10
b=20
print("the sum is",a+b)
print("the sub is",a-b)
print("the mul is",a*b)
a=100
b=200
print("the sum is",a+b)
print("the sub is",a-b)
print("the mul is",a*b)
a=1000
b=2000
print("the sum is",a+b)
print("the sub is",a-b)
print("the mul is",a*b)'''

'''def cal(a,b):
    print("the sum is",a+b)
    print("the sub is",a-b)
    print("the mul is",a*b)
    print("the pow is",a**b)
    print("the modules is",a%b)
    print("the division is",a/b)
    print("the integer division is",a//b)
cal(100,200)'''

'''def add(a,b):
    print(a+b)
add(4,5)'''

'''while True:
    def cal():
        a=int(input())
        b=int(input())
        print(a+b)
    cal()'''

#recusion

'''def cal():
        a=int(input())
        b=int(input())
        print(a+b)
        cal()
cal()'''

'''def fullname():
    fname=input("first name")
    lname=input("last name")
    print((fname+" "+lname).title())
fullname()'''

#Diffrence btw print and return
'''print just show the human user input in a console
return will terminate the function and gives back you the value of the function'''

'''def mul(a,b):
    print(a*b)
mul(3,5)'''

'''def mul(a,b):
    return a*b
print(mul(2,3))'''

#print v/s return
'''def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
add(5,6)'''

'''def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c,d,e
    
print(add(10,20),end="")'''

#TASK splitbill

'''def splitbill():
    amount=int(input("Enter amount: "))
    count = int(input("Enter count: "))
    split = amount / count
    return split
print(splitbill())'''

'''def splitbill():
    amount=int(input("Enter amount: "))
    count = int(input("Enter count: "))
    split = amount // count
    print(f"the amount is : {split}")
splitbill()'''


def task():
    a = int(input())
    b = int(input())
    option = int(input())
    if option == 1:
        print(a+b)
    elif option == 2:
        print(a-b)
    elif option == 3:
        print(a*b)
    else:
        print("choose correct option")

task()
