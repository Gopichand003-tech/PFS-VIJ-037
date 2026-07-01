Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuple()
a = (4,5.6,"code",5+9j,True,False)
print(a)
(4, 5.6, 'code', (5+9j), True, False)
type(a)
<class 'tuple'>
a.count(5+9j)
1
a.index(True)
4
len(a)
6

 
#sets{}
a = {5,8.9,"gopichand",5+9j,True,False}
a
{False, True, (5+9j), 5, 'gopichand', 8.9}
type
<class 'type'>
type(a)
<class 'set'>

a = {3,4,5,6,7,8,9}
b = {3,4,5,6,7}
b.issubset(a)
True
a.issuperset(b)
True
a.union(b)
{3, 4, 5, 6, 7, 8, 9}

a.intersection(b)
{3, 4, 5, 6, 7}

a.update(b)
a
{3, 4, 5, 6, 7, 8, 9}

a.difference(b)
{8, 9}
b.difference(a)
set()
a.symmetric_difference(b)
{8, 9}
b.symmetric_difference(a)
{8, 9}
>>> a.intersection_update(b)
>>> a
{3, 4, 5, 6, 7}
>>> b.intersection_update(a)
>>> b
{3, 4, 5, 6, 7}
>>> 
>>> a = {3,4,5,6,7,8,9}
... b = {3,4,5,6,7}
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> c = {3,4,5,6,7,8,9}
... d = {3,4,5,6,7}
SyntaxError: multiple statements found while compiling a single statement
>>> a = {2,3,4,5,6,7}
>>> b = {9,8,7,6,4,2}
>>> a.difference_update(b)
>>> a
{3, 5}
>>> b.difference_update(a)
>>> b
{2, 4, 6, 7, 8, 9}
>>> 
>>> a = {11,12,13,14,15,16,17}
>>> b = {13,14,15,16,17,18}
>>> a.symmetric_difference_update(b)
>>> a
{18, 11, 12}
>>> b.symmetric_difference_update(a)
>>> b
{16, 17, 11, 12, 13, 14, 15}
>>> 
>>> 
>>> a = {3,4,5,6,7,8,9}
>>> a.discard(7)
>>> a
{3, 4, 5, 6, 8, 9}
>>> a.clear()
>>> a
set()
>>> b=set()
>>> b.add(20)
>>> b
{20}
>>> 
