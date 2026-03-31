# WAP to take the examples of constructor overriding. 
# (Here when we create the object of child class that time child class constructor override the parent class constructor)
# Constructor overriding  

class Father:  
    def __init__(self):  
        print("Father:= i am on time at breakfast table")  
  
class Child(Father):  
    def __init__(self):  
        print("Child:= i will be late for breakfast")  
  
obj = Child()  



#if we add super() method then
#Constructor overriding 
 
class Father:  
    def __init__(self):  
        print("Father:= i am on time at breakfast table")  
  
class Child(Father):  
    def __init__(self):  
        print("Child:= i will be late for breakfast") 
        super().__init__()
  
obj = Child()  
