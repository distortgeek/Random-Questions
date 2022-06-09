x = int(input("Enter total number of elements in your list : "))
i = 1
list1 = []
list2 = []
list3 = []
count0 = 0 
count1 = 0
while i <= x:
    y = int(input("Enter element : "))
    list1.append(y)
    i += 1
list1.sort()
for j in list1:
 if j not in list2:
     list2.append(j)
n = int(input("Enter number to search : "))
for k in list2:
    if k == n:
        list3.append(1)
    else:
        list3.append(0) 
for l in list3:
    if l == 1:
        count1 += 1 
    else:
        count0 += 1
if count1 > 0:
    print(n,"is an element of the list.")
else:
    print(n,"is not an element of the list.")