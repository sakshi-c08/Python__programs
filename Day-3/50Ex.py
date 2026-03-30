# i/p=[5,0,5,3,0,1,2]
# o/p=[5,5,3,1,2,0,0]

list=[5,0,5,3,0,1,2]
for i in list:
    if i == 0:
        list.remove(i)
        list.append(i)
print(list)