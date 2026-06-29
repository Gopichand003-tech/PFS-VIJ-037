Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Arthematic
a =2
b = 4
print(a+b)
6
print(a - b)
-2
print(a*b)
8
print(a**b)
16
print(a//b)
0
print(a/b)
0.5
print(a%b)
2

#Assignment
a = 3
b = 5
a + b
8
a += b
a
8
a -= b
a
3
a *= b
a
15
a **= b
a
759375
a //= b
a
151875
a /= b
a
30375.0
a %= b
\
a
0.0
b
5
b %= a
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    b %= a
ZeroDivisionError: division by zero
a %= b
b
5


#comparison
a = 4
b = 9
a > b
False
a < b
True
a >= b
False
a <= b
True
a != b
True
>>> a == b
False
>>> a = b

>>> #Logical
>>> a =3
>>> b = 6
>>> a < b and b > a
True
>>> a <= b and b >= a
True
>>> a!=b and a==b
False
>>> a<b or b>a
True
>>> a!=b or a==b
True
>>> a<=b or b<=a
True
>>> not True
False
>>> not False
True
>>> 
>>> #identity
>>> a=4
>>> type(a) is int
True
>>> type (a) is not int
False
>>> b = 6.7
>>> type(b) is float
True
>>> type(b) is str
False
>>> 
>>> # Membership
>>> a = 1,23,3,4,5,6
>>> 20 in a
False
>>> 23 in a
True
>>> 40 is not a
True
>>> 40 not in a
True
