#Exception handling

'''try-> Instructions from which are expecting the exceptions

except -> exceptions are raised in try  block it will be handle by this block

else -> optional(no.expections)

finally -> always it will display'''

'''try:
    a=int(input("a value"))
    b=int(input("b value"))
    c=a//b
    print(c)
except:
      print("Exception raised")
else:
    print("no exceptions")
finally:
       print("program ends...")'''

# regex -> regular expressions are powerful tools (modules,embedded in python which is mainly used to find a
# pattren with in a given string or statements or files and we mainly use it for text manipulation)
'''a="codegnan is in vijayawada"
print(a)'''

'''a="codegnan\nis\tin\nvijayawada"
print(a)'''

#rstring
'''a=r"codegnan\nis\tin\nvij"
print(a)'''

#compile(),search(),findall(),split(),sub()

#sequence characters
'''\w-> it matches alphanumeric
\W-> it matches non-alphanumeric
\d-> it matches any digit
\D -> it matches non-digit
\s -> it represents white spaces
\S -> it represents non-white spaces'''

#compile()
import re
'''a="mat cat cap maths money cash code cup dog donkey mug"
b=re.compile(r"m\w\w\w\w")
print(b)'''

#search()
'''c=b.search(a)
print(c)'''

'''b=re.search(r"m\w+",a)
print(b)'''

#findall()
'''c=re.findall(r"c\w+",a)
print(*c)'''

#split()
'''d=re.split(r"m",a)
print(d)'''

'''e=re.split(r"\s",a)
print(e)'''

#sub()
'''f=re.sub("m","a",a)
print(f)'''

a=" i got 100 rupees and i spent 50 rupees"
b=re.findall(r"\d+",a)
print(*b)
