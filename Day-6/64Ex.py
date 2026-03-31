#Polymorphisam
#polymorphism example 
 
class Principal:  
    def role(self):  
        print("i am managing all activity of college")  
  
class Dean:  
    def role(self):  
        print('Dean= I am decision taking person')  
          
class Hod:  
    def role(self):  
        print('Hod= I have responsibility of Teachers and Students')         
class Faculty:  
    def role(self):  
        print('Faculty= I have to complete syllabus successfully')  
# ========== class declaration completed=====================================  
def  func(obj): # called func obj =1:Dean  
    obj.role()# calling func  
campus=[Principal(),Dean(),Hod(),Faculty()]   
for obj in campus: #obj =[0:Principal(),1:Dean(),2:Hod()]  
    func(obj)   # calling fun  