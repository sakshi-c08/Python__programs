mydict = {  
  101: "prashant",  
  102: "ashish",  
  "103": "mohini",  
  "104": "trivani",  
  101: "ashish",  
  104: "ashish"  
}  
print(mydict)  
#only print key x=0,1
for x in mydict:  
     print(x) 

#only print values x=0
for x in mydict.values():  
     print(x) 

#printing key and values both
for x, y in mydict.items():  
    print(x," ", y)  

#if i have to add new key and value pair in my dictionary
mydict["mobile_no"] = 4646463738  
print(mydict)  



mydict = {
    101: "prashant",
    "professional": "developer",
    "empid": 1001
}
mydict.pop(101)  
print(mydict)  



mydict = {
    "name": "prashant",
    "professional": "developer",
    "empid": 1001
}
newdict = mydict.copy()  
print(newdict)  
