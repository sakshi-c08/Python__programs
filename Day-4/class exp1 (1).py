class Student:   
    roll_number = 101  
    num1 = 50  
    num2 = 100   # data member  
  
    def add(self):  #member function  
        print(self.num1+self.num2)#150  
        self.name = input("Enter name:")# name is your new type of variable  
        print(self.name)
        #function inside a clss called as method