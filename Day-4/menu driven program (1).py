#WAP to do menu driven program using atithmetic operation
import sys
def addition():#called function
    a = int(input("enter the value of a:"))
    b = int(input("enter the value of b:"))
    print("Addition=",a+b)
def substraction():
    a = int(input("enter the value of a:"))
    b = int(input("enter the value of b:"))
    print("substraction=",a-b) 
def multiplication():
    a = int(input("enter the value of a:"))
    b = int(input("enter the value of b:"))
    print("multiplication=",a*b) 
def division():
    a = int(input("enter the value of a:"))
    b = int(input("enter the value of b:"))
    print("division=",a/b) 
while True:
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.division")
    print("5.Exit")
    choice = int(input("enter your choice :"))
    if choice == 1:
        addition()
    elif choice == 2:
        substraction()
    elif choice == 3:
        multiplication()
    elif choice == 4:
        division()
    elif choice == 5:
        sys.exit()