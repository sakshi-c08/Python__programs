# Multiple inheritance 
 
class SubjMarks: # class-1  
  math = int(input("Enter paper marks of math :"))  
  DE = int(input("Enter paper marks of design engineering :"))  
  c = int(input("Enter paper marks of c language :"))  
  english = int(input("Enter paper marks of English :"))  
#================================= parent class -1  
class PractMarks: # class- 2  
  cpract = int(input("Enter practicals marks of c language :"))    
#================================= parent class -2  
class Result(SubjMarks,PractMarks): # child class  
  #print("if student pass in both = subject and practical paper then pass")  
  def total(self):  
    if self.math>=40 and self.DE>=40 and self.c>=40 and self.english>=40 and self.cpract>=20:  
      print("pass")  
    else:  
      print("fail")  
obj = Result()  
obj.total()  