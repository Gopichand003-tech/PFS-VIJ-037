# Comparison and Logical Operators 

a = 20
b = 10
age = 22
citizen = True
holiday = False
logged_in = False

a=10
b=10
if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")

a=10
b=20
if a != b:
    print("a is not equal to b")
else:
    print("a is equal to b")

a=20
b=10
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")

a=10
b=20
if a < b:
    print("a is less than b")
else:
    print("a is not less than b")

a=12
b=10
if a >= b:
    print("a is greater than or equal to b")
else:
    print("a is not greater than or equal to b")

a=10
b=12
if a <= b:
    print("a is less than or equal to b")
else:
    print("a is not less than or equal to b")

# AND
age=20
if age >= 18 and citizen:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")

# OR
age=15
holiday = False
if holiday or age < 18:
    print("Enjoy your day!")
else:
    print("Go to Office")

# NOT
if not logged_in:
    print("Please Login")
else:
    print("Welcome")

# Combination of Comparison + Logical 
marks = 75
attendance = 80

if marks >= 35 and attendance >= 75:
    print("Student Passed")
else:
    print("Student Failed")
