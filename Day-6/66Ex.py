#  WAP to understand why directly constructor overloading not supported in python. Constructor overloading is not
#  possible in Python If we define multiple constructors then the last constructor will be considered.

class Arithmatic:  
    def __init__(self):  
        print("There is no argument")  
    def __init__(self,a):  
        print("passing one argument")  
    def __init__(self,a,b):  
        print("passing two arguments")  
  
obj = Arithmatic()  
obj = Arithmatic(10)  
obj = Arithmatic(2,2)  