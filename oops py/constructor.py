'''class Rectangle:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b 

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2* (self.length + self.breadth)
r=Rectangle(10,5)
print(r.area())
print(r.perimeter())

class Cuboid(Rectangle):
    def __init__(self,l,b,h):
        self.height=h
        super().__init__(l,b)

    def volume(self):
        return self.length * self.height * self.breadth
       
c= Cuboid(10,5,2)
print(c.volume())       '''




# METHOD OVERLOADING

'''class Arith:
    def sum(self,a,b,c=None):
        s = a+b
        if c== None:
            return s
        else:
            return s + c

    def sum(self,x,y,z):
        return x + y + z




a=Arith()
print(a.sum(2,8))   
print(a.sum(2,1,1))      '''




# METHOD OVERRIDING
'''class iphone6:
    def home(self):
        print('home button is present')

class iphoneX(iphone6):
    def home(self):
        print("home is touched")
        super().home()

i6 = iphone6()
i6.home()

ix= iphoneX()
ix.home()'''


# OPERATOR OVERLOADING
'''class Rational:
    def __init__(self,p=1,q=1):
        self.p=p 
        self.q=q

    def __add__(self,other):
        s= Rational()
        s.p= self.p * other.q + self.q * other.p
        s.q=self.q * other.q
        return s

r1= Rational(2,3)
r2=Rational(2,5)   
sum=r1+r2
print(sum.p ,'/', sum.q)
'''        

# METHOD RESOLUTION
class A:
    def show(self):
        print('bwahahahahahhahahahhaha')

class B(A):
    pass

b=B()  
b.show()        

print(B.mro())   
