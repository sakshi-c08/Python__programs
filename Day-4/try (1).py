try:
    a = int(input("enter the value of a:"))
    b = int(input("enter the value of b:"))
    print(a/b)
except ZeroDivisionError:
    print("cant devide by zero")#zero division error
except ValueError:
    print("enter only integer value")#value error
    