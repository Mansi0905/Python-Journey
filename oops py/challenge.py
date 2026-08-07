#  DICE IN GAMES
'''from random import * 
class dice:

    def __init__(self,sides) :
        self.sides = sides


    def roll_dice(self) :
        return randint(1,self.sides)


d1= dice(6)

print(d1.roll_dice())
print(d1.roll_dice())'''


# CLASS FOR CIRCLE
'''import math

class circle:
    def __init__(self,radius) :
        self.radius=radius

    def     area(self):
        return math.pi * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

c1=circle(7)
print('area is',c1.area())      
print('perimtere is',c1.perimeter())      '''


# CLASS BOOK
'''class book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price


    def show_details(self):
        print ('Title',self.title) 
        print('Author',self.author)
        print('price',self.price)


b1=book('lies','meow',123)       
b2=book("haunting","adeline",789)

b1.show_details()
print('')
b2.show_details()'''


# INSTANCE AND CLASS VARIABLE
'''class Employee:

    employee_count=101
    def __init__(self,name,desig,sal):
        self.name=name
        self.designation=desig
        self.salary=sal
        self.eid='e'+str(Employee.employee_count)
        Employee.employee_count +=1


    def show_detail (self):
        print('name',self.name)   
        print('Eid',self.eid)
        print('designation',self.designation)   
        print('salary',self.salary)  

    @classmethod
    def total_emp(cls):
        return cls.employee_count - 101



e1=Employee('nina','dragon',12345)
e2=Employee('rita','zombie',3456789)

e1.show_detail()
print('')
e2.show_detail()

'''

# SIMPLE CLASS FOR CALCULATOR
'''class calculator:
    @staticmethod
    def add(a,b):
        return a+b

    def sub(a,b):
     return a-b    

    def mul(a,b) :
        return a*b

    def div(a,b):
        return a / b

x=9
y=8

print(calculator.add(x,y))
print(calculator.sub(x,y))
print(calculator.mul(x,y))
print(calculator.div(x,y))'''

# CUSTOMER PHONE NUMBER //accessors mutators
'''class customer:
    def __init__(self,name,phoneno):
        self.name=name
        self.phneno=phoneno

    def get_name(self):
        return self.name  

    def get_phoneno(self):
        return self.phneno

    def set_phoneno(self,ph):
        self.phneno=ph

c1=customer("nina",90909090)
print('name',c1.get_name())  
print('phonenumber',c1.get_phoneno())

c1.set_phoneno(9837464784)
print('')
print('name',c1.get_name())  
print('phonenumber',c1.get_phoneno())

'''

# CURRENCY CONVERTOR //accesors and mutators
'''class curency_convertor:
    def __init__(self,name,rate):
     self.currency=name
     self.rate=rate

    def get_currency(self) :
        return self.currency

    def get_rate(self):
        return  self.rate

    def set_currency (self,name):
        self.currency=name 

    def set_rate(self,rate):
        self.rate=rate

    def convertor(self,amount):
        return self.currency + ' convrsion is '+ str(self.rate * amount)    
        
cc=curency_convertor('usd',70)

print(cc.convertor(100))

cc.set_currency('yen')
cc.set_rate(50)
print(cc.convertor(100))'''


# BANK ACCOUNT //minimum balance error
'''class Minimum_balance_error(Exception):
    pass


class Account:
    acc_num=1001
    def __init__(self,name,balance=1000):
        if balance <1000:
            raise Minimum_balance_error("acount can not be created")
        self.name=name
        self.account_number = self.acc_num
        self.acc_num += 1

        self.balance=balance

    def  deposit(self,amt):
        self.balance +=amt

    def withdraw(self,amt):
            if self.balance-amt < 1000:
                raise Minimum_balance_error('amount cannot be withdrawn')
            self.balance -= amt


    def show_detail(self) :
        print('account number;- ', self.acc_num)
        print('name;-',self.name)
        print('balance;-', self.balance)

a1= Account           ('azazel',20090)
a1.show_detail()
print(" ")

a2= Account           ('jeanna',90090)
a2.show_detail()

'''

# INHERITING SHAPES IN POLYNOMIAL
'''import math
class polygon:
    def __init__(self,ns,*sides):
        self.no_of_sides = ns
        self.sides=sides


class triangle(polygon):
    def __init__(self,ns,*sides):
        polygon.__init__(self,ns,*sides)

    def area(self):
        a,b,c=self.sides
        s=(a+b+c)/2
        area=math.sqrt(s * (s-a) * (s-b) * (s-c))  
        return area  

t1=triangle(3,10,15,9)
print('area of triangle is :',t1.area())'''

# ACADEMIC COURSES
'''class course:
    def __init__(self,cn,cd,*books):
        self.course_name=cn 
        self.course_duration = cd 

        self.books=[self.Book(b) for b in books] 
        
    def show_detail(self):
         print('name:', self.course_name)
         print('duration:',self.course_duration)
         print("suggested books")
         for b in self.books:
          print(b)

    class Book:
        def __init__(self,title)   :
            self.title=title

        def __str__(self):
            return self.title

c1 = course('python', 10, 'learn python','python crash course')
c1.show_detail()         

'''

# INNER CLASS
'''class Computer:
    def __init__(self,name,make,os):
        self.name=name
        self.cpu=self.CPU(make)
        self.os= self.OS(os) 

    def __str__(self)   :
        return 'name:' +  self.name + '\nmake:' + self.cpu.get_make() + '\nos name: ' + self.os.get_name()

    class CPU:
         def __init__(self,make )    :
            self.make=make

         def get_make(self):
            return self.make

    class OS:

        def __init__(self,os) :
            self.name= os

        def get_name(self):
            return self.name

c1=Computer('PC101','RYZEN','WNIDOWS')
print(c1)
         '''

# POLYMORPHISM    //PET DETAILS
'''class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print('my name is '+ self.name + ' my age is ' + str(self.age))

    def make_sound(self):
        print        ('mem mew ')


class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print('my name is '+ self.name + ' my age is ' + str(self.age))

    def make_sound(self):
        print        ('woof woof ')

def my_pet(pet):
    pet.info()
    pet.make_sound()

c=Cat('meow-neko', 2)
d= dog('akachan-sumit', 3)

my_pet(c)
my_pet(d)'''

# GREETINGS IN DIFFERENT LANGUAGE
'''class English:
    def greeting(self):
        print('hemloo')

class French:
    def greeting(self):
        print("bonjour")   

def greet(language)  : 
    language.greeting()

e=English()
greet(e)

print('')

f = French()
greet(f)
'''
        #  OPERATOR OVERLOADING      

# MEASURING THE ANGLES
'''class Angle:
    def __init__(self, deg) :
        self.degree =deg

    def __add__(self, ang):
        sum = Angle(self.degree  +  ang.degree)   
        return sum

    def __str__(self) :
        return 'Degree ' + str(self.degree)
    

a1 = Angle(30)    
a2 = Angle(45)
print(a1)
print(a2)

a3 = a1 + a2

print(a3)

         '''


        #  OPERaTOR OVERLOADING

#  POLICE ROBOT       
'''class Robot:
    def __init__(self, name):
        self.name = name

    def say_hi(self):  
        print  ('hi, i am ' + self.name)

class PoliceRobot(Robot):
    def say_hi(self):
       print("hi this is "+self.name+ "i am here to help u")

r1 = PoliceRobot('optimus')         
r1.say_hi()    
'''

#           METHOD OVERRIDING
# DIFFERENT SHAPE CLASS
'''import math
class Shape:
    def __init__(self, name):
        self.name = name 
        
    def area(self):
        pass 


class Rectangle :
    def __init__(self,len,bre):
        self.length = len
        self.breadth = bre

    def area(self):
        return self.length * self.breadth


class Circle:
    def __init__(self,rad):
        self.radius = rad

    def area(self):
        return math.pi * (self.radius ** 2)


r = Rectangle(10,5)
print('Area : ' , r.area())                       
 '''
