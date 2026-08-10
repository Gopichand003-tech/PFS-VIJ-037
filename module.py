# diff btw modules library package

'''module -> A module in python is a single python file it consist a python code
          It typically consist of functions, classes and variables that can be used in other python scripts or programs
          ex: math.py,random.py or my_module.py

Package -> A package in python is a directory containing one or more python modules and an __init__.py file
           The __init__.py file can be empty or contain initialization code for the package
           ex:numpy,pandas,requests,Django

Library -> It consits of both modules and packages
           ex: numpy,pandas,matplotlib'''

# Note: Every python file is module and import is keyword and every python file is saved internally with variable as __main__

'''def greetings(name):
    print("Welcome",name)'''

'''a=4
b=8
print(a+b)'''

'''a=int(input("a value"))
b=int(input("b value"))
print(a+b)'''

'''details={"idnos":[10,20,30],
         "names":["gopi","mallesh","karthik"],
         "marks":[40,50,60]}'''

def dummy():
    if __name__=="__main__":
        print("This program run as script")
    else:
        print("this program run as module")

dummy()
