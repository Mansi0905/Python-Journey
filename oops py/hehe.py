def add(x,y):
 return x+y
def subtract(x,y):
 return x-y
def multiply(x,y):
 return x* y
def divide(x,y):
  if y ==0:
   return "error meiw"
  return x/y

def calculator():
      print("simple calculator")
      print("1: addition")
      print("2: subtraction")
      print("3: multiplication")
      print("4: divide")
calculator( )

choice = input("enter your choice 1,2,3,4:")

if choice in ('1','2','3','4'):
    num1 = float(input("enter first number:"))
    num2= float(input("enter second number:"))

if choice == '1':
      print(num1,"+",num2,"=",add(num1,num2))

elif choice == '2':
      print(num1,"-",num2,"=",subtract(num1,num2))                   
elif choice == '3':
      print(num1,"*",num2,"=",multiply(num1,num2))   
elif choice == '4':
      print(num1,"/",num2,"=",divide(num1,num2))   

else:
      print("invalid choice")  
