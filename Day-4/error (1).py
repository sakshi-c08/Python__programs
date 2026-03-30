try:
    a = int(input("enter first integer no:"))
    b = int(input("enter second integer no:"))
    print(a/b)
except  (ValueError, ZeroDivisionError) as message:
    print(message)