Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#In integer String and complex will not work
int(4)
4
int("code")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    int("code")
ValueError: invalid literal for int() with base 10: 'code'
int(4 + 3j)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int(4 + 3j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(true)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
int(True)
1
int(False)
0
#Float
float(4)
4.0
float(4.5)
4.5
float("string)
      
SyntaxError: unterminated string literal (detected at line 1)
float("str")
      
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("str")
ValueError: could not convert string to float: 'str'
float(4 + 3j)
      
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(4 + 3j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
      
1.0
float(False)
      
0.0
#string
      
str(3)
      
'3'
str("400")
      
'400'
str(4.5)
      
'4.5'
str(3 + 4j)
      
'(3+4j)'
str(True)
      
'True'
str(False)
      
'False'

#complex
...       
>>> complex(4)
...       
(4+0j)
>>> complex(4.5)
...       
(4.5+0j)
>>> complex("string")
...       
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    complex("string")
ValueError: complex() arg is a malformed string
>>> complex(True)
...       
(1+0j)
>>> complex(False)
...       
0j
>>> 
>>> #Bool
...       
>>> bool(1)
...       
True
>>> bool(2)
...       
True
>>> bool(0)
...       
False
>>> bool(2.3)
...       
True
>>> bool("hello")
...       
True
>>> bool(3 + 4j)
...       
True
>>> bool(True)
...       
True
>>> bool(False)
...       
False
