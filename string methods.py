Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#String Methods
#len()
a = "python"
len(a)
6
b = "python course"
len(b)
13
c = ""
len(c)
0
d = " "
len(c)
0
len(d)
1

#count()
a = "python"
count(a)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("python")
1
b = "twinkle twinkle littel star"
b.count("t")
5
b.count("k")
2


#find()
c = "hello"
c.find("l")
2
c[2:4]
'll'
c.find("e")
1
#It prints the index of the given value


#escape sequence
#\n -> new line
#\t -> tab space
a = "name\nmobile\tmaildId\nclg"
print(a)
name
mobile	maildId
clg
b = "name:Gopichand\nmobileno:9154688692\tmaildId:chennapaalligopichand@gmail.com\nclg:Aditya university"

print(b)
name:Gopichand
mobileno:9154688692	maildId:chennapaalligopichand@gmail.com
clg:Aditya university

#replace()
a = "wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b = "wait wait until you succeed"
b.replace("wait","work")
'work work until you succeed'
b.replace("wait","work",1)
'work wait until you succeed'


#upper() & lower()
b = "HI"
b.lower()
'hi'
c = "Carraom"
c.upper()
'CARRAOM'

# capitalize()
c.capitalize()
'Carraom'

#title()
d = "python course"
d.title()
'Python Course'


="java"
SyntaxError: invalid syntax
a = "java"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a.isalpha()
True
b = "python course"
b.isalpha()
False
c="pythoncourse"
c.isalpha()
True
d=1234
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
d="1234"
d.isdigit()
True
d.isalnum()
True
e="gopi123"
e.isalnum()
True
f="gopi@123"
f.isalnum()
False


#startswith & endswith
a = "Gopichand"
a.startswith("G")
True
a.startswith("g")
False


#strip()
a = "         pooja        "
a.strip()
'pooja'
a.lstrip()
'pooja        '
a.rstrip()
'         pooja'


#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b = "ia am in vij"
b.split()
['ia', 'am', 'in', 'vij']
c = "codegnan"
c.split()
['codegnan']


#join()
a="vij hyd vzg"
"".join(a)
'vij hyd vzg'
b="vij","gun","man"
"".join(b)
'vijgunman'


#concatenation
a = "hello"
b = "world"
print(a+b)
helloworld
print(a+" "+b)
hello world
fname = "gopichand"
lname = "ch"
print(fname+" "+lname)
gopichand ch
print(fname.title()+" "+lname.title())
Gopichand Ch
print((fname+" "+lname).title))
SyntaxError: unmatched ')'
print((fname+" "+lname).title())
Gopichand Ch


#Formating
a = 4
>>> b = 8
>>> print(a+b)
12
>>> print("The sum is",a+b)
The sum is 12
>>> x = "vja"
>>> print("city is",x)
city is vja
>>> 
>>> #format Method
>>> a="motu"
>>> b="patlu"
>>> print("hello",a+b)
hello motupatlu
>>> print("hello {}{}".format(a,b))
hello motupatlu
>>> print("hello {} hello{}".format(a,b))
hello motu hellopatlu
>>> 
>>> #fstring
>>> a = "sita"
>>> b = "ram"
>>> print(f"hello {a}{b}")
hello sitaram
>>> print(f"hello {a} {b}")
hello sita ram
>>> 
>>> x = 3
>>> y = 2
>>> result = 3 * 2
>>> print("the result is",result)
the result is 6
>>> 
>>> x =4
>>> y=2
>>> result = x * y
>>> print("the product is: {result}")
the product is: {result}
>>> 
>>> 
... 
... x =4
... y=2
... result = x * y
... print(f"the product is: {result}")
SyntaxError: multiple statements found while compiling a single statement
