# Single level inheritance  

class College: # parent class  
  def college_name(self): # member function of college  
    print("Modern College")  
    
class Student(College): # child class  
  def student_info(self): # memeber function  
    print("Name:   Prashant Jha")  
    print("Branch: Mechanical")  
     
obj = Student()# object create child class  
obj.college_name()  
obj.student_info()  