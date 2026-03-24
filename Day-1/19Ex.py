#WAP to calculate gross sal from basic sal(HRA=30% ,TA=40% ,DA=20%)

basic = float(input("Enter Basic Salary"))
hra = 0.30 * basic 
ta = 0.40 * basic 
da = 0.20 * basic 

gross = basic + hra + ta + da
print("Gross Sallary=" , gross)