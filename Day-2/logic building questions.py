for i in range(1,5):
    if i == 3:
        break
    print(i)
    #i = 1,2,3


for i in range(1,5):
    if i == 3:
        continue
    print(i)


list =[10,20,30,40,50]
for i in list: #i = 0:1,1:20,2:30,...
    print(i)


mycart=[10,20,200,300,800,60,700]
for i in mycart: #i=0:10,1:20,2:200,...
    if i>400:
        print("this is my purchased cart item")
        continue
    print(i)


#WAP to calculate the sum of list elements
list = [1,2,3,4,5,6,7,8,9,10]
sum=0 #sum=1,3,6,10,....
for x in list: #x=0:1,1:2,2:3,3:4,4:5,5:6,
    sum=sum+x
print("The Sum=",sum)



name = "prashant"
       #01234567
for i in name: #i=1,2,3,..
    print(i)


name = "prashant"
       #01234567
newname = "" #prashn
for i in name: #i=
    if i not in newname:
        newname += i
    print(newname)



name = "prashant"
newname = ""
# Step 1: build string without duplicates
for i in name:
    if i not in newname:
        newname += i
# Step 2: print in reverse pattern
for i in range(len(newname), 0, -1):
    print(newname[:i])


name = "prashant"
newname = ""
# traverse string in reverse
for i in name[::-1]:
    if i not in newname:
        newname += i
        print(newname)



rollno = [3,5,7,1,11,4,5,2]
for x in rollno: #x=0:3,...
    if x == 2 or x == 4 or x == 6 or x == 8 or x == 10:
     print("even number is found",x)
     break



#s.replace(oldstring,newstring)
#inside s,every occurance of oldstring will be replaced with newstring

s = "" 
s1=s.replace("difficult","easy")
print(s1)
s="ababababababab"
s1=s.replace("a","b")
print(s1)


#comparing a value or address.......
x=['A','B','C']
y=['A','B','C']
z=[1,2,3,4]
print(x==y)
print(x==z)
print(x != z)



#index method used to written the index position in list
val=[1,2,3,5,5,5,1,2,4,4,6,6,6]
print(val.index(1))
print(val.index(2))
print(val.index(3))
print(val.index(4))
print(val.index(5))
print(val.index(6))



n=[1,2,3,5,5,5,1,2,4,4,6,6,6]
print(n.count(1))
print(n.count(2))
print(n.count(3))
print(n.count(4))
print(n.count(5))
print(n.count(6))
print(n.count(7))



import datetime
#datetime formatting
date=datetime.datetime.now()
print("it's now:{:%d/%m/%y %H:%M:%S}".format(date))