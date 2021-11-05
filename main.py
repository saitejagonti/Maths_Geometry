
import math

def squareinfo():
    print("A small deination for Square \n "
          '"Square, in geometry, a plane figure with four equal sides and four right angles."')

def squarearea(a):
    result=a**2
    print(f'Area of Square is: {result}')

def squareperimeter(a):
    result=4*a
    print(f'Peimeter of Square is: {result}')

def squarediagonal(a):
    result=a*math.sqrt(2)
    print(f'Diagonal of Square is: {result}')

def rectangleinfo():
    print("A small defination of Rectangle\n "
          ''"Rectangle is any shape with four sides and four right angles."'')

def rectanglearea(a,b):
    result=a*b
    print(f'Area of Rectangle is: {result}')

def rectangleperimeter(a,b):
    result=(a+b)+(a+b)
    print(f'Perimeter of Rectangle is: {result}')

def rectanglediagonal(a,b):
    result=math.sqrt(a**2 + b**2)
    print(f'Diagonal of Rectangle is: {result}')


name=(input("Enter Your Name: "))
print(f'Hi {name}, Welcome to Geometry operations, We have two options\n'
      f'for Square select option "1" and for Rectangle select option "2". Select accordingly')
se = int(input("Select the option: "))

if se==1:
    squareinfo()
    print("For Area of Square, Select 1\n"
          "For Perimeter of Square, Select 2\n"
          "For Diagonal of Square, Select 3")

    sa = int(input("Select the number: "))

    if sa==1:
        print("Area of Square")
        a = int(input("Enter the value: "))
        squarearea(a)

    elif sa==2:
        print("Perimeter of Square")
        a=int(input("Enter the value: "))
        squareperimeter(a)

    elif sa==3:
        print("Diagonal of Square")
        a=int(input("Enter the value: "))
        squarediagonal(a)

    else:
        print("Invalid Operation")

elif se==2:
    rectangleinfo()
    print("For Area of Rectangle, Select 1\n"
          "For Perimeter of Rectangle, Select 2\n"
          "For Diagonal of Rectangle, Select 3")

    sr = int(input("Select the number: "))

    if sr==1:
        print("Area of Rectangle")
        a = int(input("Enter the value of length: "))
        b = int(input("Enter the value of width: "))
        rectanglearea(a,b)

    elif sr==2:
        print("Perimeter of Rectangle")
        a = int(input("Enter the value of length: "))
        b = int(input("Enter the value of width: "))
        rectangleperimeter(a,b)

    elif sr==3:
        print("Diagonal of Rectangle")
        a = int(input("Enter the value of length: "))
        b = int(input("Enter the value of width: "))
        rectanglediagonal(a,b)

    else:
        print("Invalid Operation")

else:
    print("Invalid Selection, Select Accordingly")

