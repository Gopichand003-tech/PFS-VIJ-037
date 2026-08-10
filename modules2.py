#math module

'''import math
print(math.pi)
print(math.pi*4)
print(math.sqrt(2))
print(math.log(2))
print(math.tan(45))
print(math.cos(60))
print(math.sin(30))
print(math.pow(2,4))
print(math.ceil(3.9))
print(math.floor(3.11))'''

'''from math import pi,sqrt,log,tan
print(pi)
print(sqrt(4))
print(log(6))
print(tan(45))'''

#import sys
#print(sys.version)
#print(sys.path)

# os module
'''import os
print(os.path)
print(os.getcwd())
print(os.listdir())
print(os.chdir("C:\\Users\\chgop\\Downloads"))
print(os.listdir())'''

#Random module -> Random module is used to generate a random numbers in python , randint  function is used and this function is defined in random module
'''import random
a=random.sample(range(10,40),40)
print(a)'''

#randint()
'''import random
a=random.randint(50,60)
print(a)'''

#choice()
'''import random
a=[10,20,30,40,50,60]
b=random.choice(a)
print(b)'''


# task
import random
while True:
    dice=int(input("Enter any number:" ))
    n=random.randint(1,6)
    print(n)
    option = int(input('''Roll again?
                 1.yes
                 2.No'''))
    if option == 1:
        continue
    elif option == 2:
         break
    else:
         print("Enter correct option")

