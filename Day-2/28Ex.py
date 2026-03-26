name = "prashant" #str 
print(name)  # Output: prashant  
myname = list(name)  
print(myname)

mylist = [40, 30, 20, 10]  
mylist.reverse()  
print(mylist) 

mylist = [44, 22, 77, 0, 9, 88]  
mylist.sort()  
print(mylist) 

mylist = [44, 22, 77, 0, 9, 88]  
mylist.sort(reverse=True)  
print(mylist) 

mylist = [44, 22, 77, 0, 9, 88]  
newlist = mylist  
print(id(mylist))  # Output: same id  
print(id(newlist))