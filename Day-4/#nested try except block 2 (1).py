try:
    a = int(input("enter first integer no:"))
    b = int(input("enter second integer no:"))
    print(a/b)
except ZeroDivisionError as message:
    print(message)
except ValueError as message:
    print(message)