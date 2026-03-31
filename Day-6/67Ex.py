#method overriding

class Rbi:
    def homeLoan_ROI(self):
        print("Home Loan Rate of interest = 7.5%")#parent class
    def carLoan(self):
        print("Car Loan Rate of interest = 8%")

class Sbi(Rbi):
    def homeLoan_ROI(self):
        print("Home Loan Rate of Intrest = 6.5%")#child class

obj = Sbi()
obj.homeLoan_ROI()
obj.carLoan()


#if they ask i want to access parent class then....
#using super() method we can access parent class method in child class

class Rbi:
    def homeLoan_ROI(self):
        print("Home Loan Rate of interest parent class = 7.5%")#parent class
    def carLoan(self):
        print("Car Loan Rate of interest = 8%")

class Sbi(Rbi):
    def homeLoan_ROI(self):
        print("Home Loan Rate of Intrest child class = 6.5%")#child class
        super().homeLoan_ROI()

obj = Sbi()
obj.homeLoan_ROI()
obj.carLoan()