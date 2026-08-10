#List comprehension
a=["codegnan","python","course"]
#["CODEGNAN","PYTHON","COURSE"]
#print(a.upper())

'''b=str(a)
print(b.upper())'''

'''for i in a:
    print(i.upper(),end=",")'''

'''b=[]
for i in a:
    b.append(i.upper())
print(b)'''

#syntax
#a=[expr for var in collection/range]
'''a=[i.upper() for i in a]
print(a)'''

'''b = ["vja","hyd","vzg"]
b=[i.title() for i in b]
print(b)'''

'''c=[1,2,3,5,6,8,12,13]
c=[(i ** 2) for i in c]
print(c)'''

'''a = 16
a=[i for i in range(16)]
print(a)'''

'''a = 16
a=[i for i in range(16) if i % 2 == 0]
print("Even")
print(a)'''

'''a = 16
a=[i for i in range(16) if i % 2 != 0]
print("Odd")
print(a)'''

'''a=21
a=[i**2 for i in range(0,21) if i % 2 == 0]
print(a)'''

'''a=["apple","banana","grapes","mango","kiwi","dragon","berry"]
b=[a for a in a if "a" in a]
print(b)'''

'''a=["apple","banana","grapes","mango","kiwi","dragon","berry"]
b=[a for a in a if "a" not in a]
print(b)'''

'''a=31
#even squares odd multiple by 5
a=[i**2 if i%2==0 else i*5  for i in range(1,31)]
print(a)'''

'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range(len(a))]
print(c)'''
