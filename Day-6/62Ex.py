# Multilevel inheritance 
 
class College:   #first class  first- level  
  def college_name(self):  
    print("Modern College")  
#============================================  
class Student(College): #second class second - level  
  def student_info(self):  
    print("Name:   Prashant Jha")  
    print("Branch: Mechanical")  
#=============================================  
class Exam(Student): #child class  
  def subject(self):  
    print("Subject1: Designe Engineering")  
    print("Subject2: Math")  
    print("Subject3: C-Language")  
obj = Exam()  
obj.college_name()  
obj.student_info()  
obj.subject()  
