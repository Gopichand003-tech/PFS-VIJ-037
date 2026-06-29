Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Bitwise operators
a&b
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a&b
NameError: name 'a' is not defined
a=5
b=7
a&b
5
bin(1)
'0b1'
bin(2)
'0b10'
bin(3)
'0b11'
bin(4)
'0b100'
bin(5)
'0b101'
bin(6)
'0b110'
bin(7)
'0b111'
bin(8)
'0b1000'
bin(9)
'0b1001'
o
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    o
NameError: name 'o' is not defined

bin(10)
'0b1010'
a=5
~a
-6
a=-5
~a
4
a=9
-(a+1)
-10
a=5
b=7
a^b
2
a=4
b=3
a^b
7
a=10
b=15
a^b
5
a=43
b=34
a^b
9
a = "vijayawada"
>>> a[4]
'y'
>>> a[-3]
'a'
>>> 
>>> 
>>> #Indexing
>>> #Positive method
>>> a = "Gopichand"
>>> a[0]+1[1]+a[2]+a[3]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a[0]+1[1]+a[2]+a[3]
TypeError: 'int' object is not subscriptable
>>> a[0]+a[1]+a[2]+a[3]+a[4]
'Gopic'
>>> a[4]+a[5]+a[6]+a[7]+a[8]
'chand'
>>> a =
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a="I am  learning  python  course"
>>> a[6]+a[7]+a[8]+a[9]+a[10]
'learn'
>>> a[16]+a[17]+a[18]+a[19]+a[20]+a[21]
'python'
>>> a[24]+a[25]+a[26]+a[27]+a[28]+a[29]
'course'
>>> b="Time  is  very  precious"
>>> b[16]+b[17]+b[18]+b[19]+b[20]+b[21]+b[22]+b[23]
'precious'
>>> b[10]+b[11]+b[12]+b[13]
'very'
>>> b[0]+b[1]+b[2]+b[3]
'Time'
>>> c = "simple is better than complex"
>>> c[-6]+c[-5]+c[-4]+c[-3]+c[-2]+c[-1]
'omplex'
>>> c[-7]+c[-6]+c[-5]+c[-4]+c[-3]+c[-2]+c[-1]
'complex'
>>> c[-11]+c[-10]+c[-9]+c[-8]
'han '
