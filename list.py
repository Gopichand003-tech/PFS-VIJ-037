Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a = [2,5.6,"python",6+9j,True,False]
print(a)
[2, 5.6, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b = 5
type(b)
<class 'int'>
c=[5]
type(c)
<class 'list'>


#append
a = ["iot","Aiml","ds","mech"]
a.append("ECE")
a
['iot', 'Aiml', 'ds', 'mech', 'ECE']

#With the help of append we can add only one value to the list

#extend
a = ["ml","Ai","Ds"]
a.extend("Py","c++","c"]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
a.extend("Py","c++","c")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.extend("Py","c++","c")
TypeError: list.extend() takes exactly one argument (3 given)
a.extend(["Py","c++","c"])
a
['ml', 'Ai', 'Ds', 'Py', 'c++', 'c']

#insert
b = ["vij","hyd"]
b.insert("man","gun")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    b.insert("man","gun")
TypeError: 'str' object cannot be interpreted as an integer
b.insert(["man","gun"])
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    b.insert(["man","gun"])
TypeError: insert expected 2 arguments, got 1



b.insert(1,"man")
b
['vij', 'man', 'hyd']


#index()
a = ["black","white","red"]
a.index("white")
1


>>> #copy()
>>> a.copy()
['black', 'white', 'red']
>>> b = a.copy()
>>> b
['black', 'white', 'red']
>>> 
>>> b.count("pink")
0
>>> 
>>> #sort()
>>> a = ["grapes","apple","mango","banana"]
>>> a.sort()
>>> a
['apple', 'banana', 'grapes', 'mango']
>>> 
>>> sai = ["ssaiii"]
>>> for ch in sai:
...     if ch.find('i')
...     
SyntaxError: expected ':'
>>> sai = ["ssaiii"]
... for ch in sai:
...     if ch.find('i'):
...         
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> a = ["c","c++","py"]
>>> a.pop()
'py'
>>> a
['c', 'c++']
>>> a.pop(1)
'c++'
>>> a
['c']
>>> 
>>> b = ["c","c++","py"]
>>> b.remove("c++")
>>> b
['c', 'py']
>>> b.clear()
>>> b
[]
>>> len(a)
1
