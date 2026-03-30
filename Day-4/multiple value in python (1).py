# can a function return multiple value in python(yes)
def add():
    a = int(input("enter value of a:"))
    b = int(input("enter value of b:"))
    add = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return add, sub, mul, div #it wll return in tuple
result=add()
print("result=",result)