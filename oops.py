#OOPS

'''1. A class contains attributes,variables,methods and functions that can the manipulate the data
2. A class is the Blue print of an object
3. Methods are functions that can be define inside the body of the class
4. An object is an initiation of a class '''

#Four Pillars of Oops
'''
1. Polymorphism -> In polymorphism we have four type
    1.Operator overloading ,operator over ridding
    2.Method overloading , Method over ridding

2.Inheritance -> single Inheritance
                 Multiple Inheritance
                 Multi Level Inheritance
                 Hybrid Inheritance
                 Heirachical Inheritance

                 
3. Encapsulation -> Public_data
                    _Protected_data
                    __private_data

4.Abstaction -> Abstract class , Abstract Method '''

#syntax

'''class classname():
    #attributes
    name="pooja"
    age=28
    place="vij"
    def fname(method_name):
        print("statements....")
a=classname()
a.fname()'''

#class declaration

'''class Details():
      name="pooja"
      age=28
      place="vja"
      def display(gopi):
          print(gopi.name,gopi.age,gopi.place)
a=Details()
print(dir(a))
a.display()'''

#object instantiation
'''class Details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
b=Details()
print(dir(a))
a.data("gopi",22,"Vja")
b.data("mallesh",22,"gun")
a.display()
b.display()'''


#object initialization
'''class Details():
     #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details("gopi",22,"vij")
a.display()'''

#Run time method 1
'''class Details():
     #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
name=input("Enter the name: ")
age=input("Enter age: ")
place=input("Enter the place: ")
a=Details(name,age,place)
a.display()'''

# Run time method 2
'''
class Details():
     #creating a constructor
    def __init__(self):
        self.name=input("name")
        self.age=int(input("age"))
        self.place=input("place")
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
a.display()'''

#diff b/w _ and __

"definition -> When user wants to create a variable with __ our python interpreter treats it as a special vairable to avoid name conflicts with methods and inner classes"

'''class employee1():
     def __init__(self):
         self.name="gopi"
         self._mailid="Gopichand@gmail.com"
         self.__salary=100000
         
class employee2():
     def __init__(self):
         self.name="Sai"
         self._mailid="Sai@gmail.com"
         self.__salary=50000
         
class employee3():
     def __init__(self):
         self.name="Gupta"
         self._mailid="Gupta@gmail.com"
         self.__salary=80000'''


'''a=employee1()
b=employee2()
c=employee3()
#print(dir(a))'''
'''print(a.name)
print(a._mailid)
print(a._employee1__salary)'''

'''print(b.name)
print(b._mailid)
print(b._employee2__salary)'''

'''print(c.name)
print(c._mailid)
print(c._employee3__salary)'''

#operator overloading
'''a=2;b=4
print(a+b)
print(a.__add__(b))
print(a.__add__(5))
print(a.__sub__(1))
print(a.__mul__(10))
print(a.__mul__(10))
print(a.__pow__(2))
print(a.__ge__(2))
print(a.__le__(10))
print(a.__eq___(2))

a=[2,3,4,5,6,7,8];
b=[4,5,6,7,8,9,10]
print(a.__add__(b))
print(a.__getitem__(2))
print(b.__getitem__(5))
a="code";b="gnan"
print(a+b)
print(a.__add__(" "+b).title())
print("gopi".__add__("ch"))'''


#operator overloading
'''class A():
     def __init__(self,a):
         self.a=a
     def __add__(self,value):
         return self.a*value.b
class B():
     def __init__(self,b):
         self.b=b
x=A(5)
y=B(4)
#x=5
#y=4
print(x+y)'''

#method overloading
'''class new():
     def sum(self,a=None,b=None,c=None):
         if a!=None and b!=None and c!=None:
             print("the sum is",a+b+c)
         elif a!=None and b!=None:
             print("the product is",a*b)
         else:
              print("program ends")
a=new()
a.sum()
a.sum(2,4,6)
a.sum(2,4)'''

#method overriding
'''class Animal():
     def speak(self):
         print("animals can make sounds")
class dog():
     def speak(self):
         print("dog barks")
a=Animal()
b=dog()
a.speak()
b.speak()'''


'''class car():
      def sound(self):
           print("beeep")
class bike():
      def sound(self):
           print("beep")
a=bike()
b=car()
b.sound()'''

#Single Inheritance

'''class RBI():
     cash = 100000
     def available_cash(cls):
          print("available_cash is",cls.cash)
          print("available_cash is",RBI.cash)
class SBI(RBI):
     pass
class HDFC(RBI):
      cash = 50000
      def new_cash(cls):
           print("new cash is",cls.cash+cls.cash)
           #print("new cash is",cls.cash + RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()'''

#Multiple Inheritance
'''class Father():
     height = 163
     def Height(cls):
           print("The height is ",cls.height)
class mother():
      weight = 57
      def Weight(cls):
           print("The weight",cls.weight)
class kid(Father,mother):
      dob = "dec 3"
      def Dob(cls):
           print("Date of birth",cls.dob)
           print("Kid height",Father.height)
           print("kid weight",mother.weight)
a=kid()
a.Dob()'''

'''class grandparent():
     prop1 = "10 acers"
     def grand(cls):
           print("I have propert of ",cls.prop1)
class parent(grandparent):
      prop2 = "House"
      def parents(cls):
           print("I have property of ",cls.prop2)
class kid(parent):
     prop3 = "car"
     def kid_prop(cls):
           print("I have property of ",grandparent.prop1)
           print(parent.prop2)
           print(kid.prop3)
a=kid()
a.kid_prop()'''

#hierarchical -> Means one parent class is inherited by multiple child classes

'''class Employee():
     a = "I am working in Codegnan"
     def company(cls):
          print(cls.a)
class Trainer(Employee):
     def teach(cls):
          print("Iam Trainer and ",Employee.a)
class Developer(Employee):
      def develop(cls):
           print("Iam developer and",Employee.a)
a=Trainer()
a.teach()
b=Developer()
b.develop()'''

#Hybrid Inheritance -> It means combining more than one type of inheritance ex - hierarical + multiple inheritance

'''class Person:
       name = "gopi"
       def details(cls):
           print("The Person details is - ",cls.name)         
class Trainer(Person):
      def Teaching(cls):
          print("I teach Python ")
class student(Person):
      def Study(cls):
           print("I came to learn Python")
class Program_manager(student,Trainer):
      def manger(cls):
           print("I am managing the schedule")
a=Program_manager()
a.details()
a.Teaching()
a.Study()
a.manger()'''

#Super()
'''class parent():
     def __init__(self,name):
          self.name = name
          print("parent constructor")
class child(parent):
     def __init__(self,name,age):
          self.age=age
          super().__init__(name)
          print("child constructor")
a=child("gopi",22)
print(dir(a))
print(a.name)
print(a.age)'''

#Encapsulation
#public data
'''class parent():
     publicdata = 10
     def method1(self):
          print(self.publicdata)
class child(parent):
     def method2(self):
          print(self.publicdata)
obj1=child()
obj1.method1()
obj1.method2()'''

#_protecteddata
'''class parent():
     _protecteddata = 10
     def method1(self):
          print(self._protecteddata)
class child(parent):
     def method2(self):
          print(self._protecteddata)
obj1=child()
obj1.method1()
obj1.method2()
print(obj1._protecteddata)'''

#__privatedata
'''class parent():
     __privatedata = 10
     def method1(self):
          print(self.__privatedata)
class child(parent):
     def method2(self):
          print(self._parent__privatedata)
obj1=child()
obj1.method1()
obj1.method2()'''

#Abstraction -> Hiding unnesesary information from user is called Abstraction
# abstarct class
"In abstract class we have one more abstract methods is called abstract class"
# abstract method
"The method declared without implementation is called abstract method"

'''class A():
    def method1(self):
        pass
obj=A()
obj.method()'''

'''class A():
    def method1(self):
        print("python")
obj=A()
obj.method()'''

'''from abc import ABC,abstractmethod
class A():
    def method1(self):
         print("Data")
obj=A()
obj.method1()'''

'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
         print("Data")
obj=A()
obj.method1()'''

'''from abc import ABC,abstractmethod
class A(ABC):
     @abstractmethod
     def method1(self):
         pass
     def method2(self):
         print("python course")
     @abstractmethod
     def method3(self):
         pass
class B(A):
     def method1(self):
         print("Data science")
     def method3(self):
         print("machine learning")
obj=B()
obj.method1()
obj.method2()
obj.method3()'''



