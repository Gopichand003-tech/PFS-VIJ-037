 #Global and local variables
'''variables inside and out side of the function is callled Global and Local variables.
A variable is designed above the function is accessible to the entire global space is called global variable.
variable in side the function is called local variable is function'''

#First case
'''a=4
def check1():
    print("inside value is",a)
check()
print("outside value is",a)'''

#second case
'''a=2
def check2():
    a=5
    a=a**2
    print("inside values is",a)
check2()
print("outside values is",a)'''

#third case
'''a=6
def check3():
    a=8
    print("inside values is",a)
    a=10
    print("updated value is",a+5)
    b=13 #local variable
    b=b+a
    print("value of b is",b)
    b=b+a
    print("values of b is",b)
check3()
print("a value is",a)
print("b vaalue is",b)'''


#when user wants to access the global variable inside the function directly and carry forward the updated value even outside the function the we need global keyword

'''a=4
def final():
    global a,b
    print("inside the value is",a)
    a=15
    print("updated value is",a)
    b=20
    b=b+a
    print("the value is",b)
final()
print("a value is",a)
print("b value is",b)'''


# task
'''while True:
    def Attendance():
        students=int(input("Enter number of students: "))
        count_present = 0
        count_abscent = 0
        for i in range(1,students+1):
            Attend=input("Enter the Attendance: ")
            if Attend == 'p':
                count_present += 1
            elif Attend == 'a':
                 count_abscent += 1
            else:
                 print("In valid")
        print(f"number of students present {count_present}")
        print(f"number of students abscent {count_abscent}")
    Attendance()'''


a=int(input())
b=int(input())
for i in range(1,a+1):
    c =
    print(c

           
