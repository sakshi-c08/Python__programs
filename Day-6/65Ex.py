# WAP to understand why directly method overloading not supported in python

class Arithmatic:  
    def add(self,a):  
        print(a)  
    def add(self,a,b):  
        print(a+b)  
    def add(self,a,b,c):  
        print(a+b+c)  
obj = Arithmatic()  
obj.add(10)  
obj.add(10,20)  
obj.add(1,2,3) 