#Built-in Functions

#print(dir())

#print(dir("__builtins__"))

#fromkeys()
'''a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))
# print(dict(a)) it will raise an error that keys required  values
b=dict.fromkeys(a)
print(b)
c=dict.fromkeys(a,"pooja")
print(c)
c["d"]="python"
print(c)'''

#eval()
'''while True:
     a=int(input("a value"))
     b=int(input("b value"))
     print(a+b)'''

'''while True:
     a=float(input("a value"))
     b=float(input("b value"))
     print(a+b)'''

'''while True:
     a=input("a value")
     b=input("b value")
     print(a+b)'''

'''while True:
     a=int(input("a value"))
     b=int(input("b value"))
     print(a+b)'''

'''while True:
     a=eval(input("a value"))
     b=eval(input("b value"))
     print(a+b)'''

# zip()-> we can combine multiple collections
#into one collection
'''a=[10,20,30,40,50,60]
names=["Khushal","manoj","harsha","sumanth","gopi"]
print(a+names)

b=zip(a,names)
print(b)
c=list(zip(a,names))
print(c)

c=tuple(zip(a,names))
print(c)

c=set(zip(a,names))
print(c)'''

#enumerate() -> we can give counter to the collection
'''names=["nikitha","taruni","siri","kalyani","prameela"]
for i in range(len(names)):
    print(i,names[i])'''

'''b=list(enumerate(names))
print(b)

b=list(enumerate(names,10))
print(b)

b=dict(enumerate(names,100))
print(b)

b=tuple(enumerate(names,100))
print(b)'''


#ASCII
#chr()
#ord()
'''print(chr(65))
print(chr(90))
print(chr(92))
print(ord("a"))
print(ord("z))'''
#print(chr("y"))


'''for i in range(65,91):
    print(chr(i),end=" ")'''

'''for i in range(97,123):
    print(chr(i),end=" ")'''

#task
'''n=input()
for i in n:
    print(i,"-",ord(i))'''

height=eval(input("Enter Your height: "))
weight=eval(input("Enter your weight: "))
formula = ((weight) / (height ** 2))*10000
print(f"your BMI:{formula}")
if formula < 18.5:
    print("Under weight")
elif 18.5<= formula <=24.5:
    print("healthy")
elif 24.5<= formula <=29.5:
    print("over weight")
elif formula >= 30:
     print("obesity")
else:
    print("wrong")

