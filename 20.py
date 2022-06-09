x = int(input("Enter total number of elements in your list : "))
i = 1
list1 = []
while i <= x:
    y = int(input("Enter element : "))
    list1.append(y)
    i += 1
list1.sort()
print("Original List is:",list1)
s=len(list1)
if s%2!=0:
    s=s-1
for i in range(0,s,2):
    list1[i],list1[i+1]=list1[i+1],list1[i]
print("List after swapping :",list1)