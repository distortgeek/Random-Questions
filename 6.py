x = int(input("Enter the number 1 : "))
y = int(input("Enter the number 2 : "))
z = int(input("Enter the number 3 : "))
if x > y > z:
    print("Largest number is : ",x,"and","Smallest number is : ",z)
elif y > x > z:
    print("Largest number is : ",y,"and","Smallest number is ",z)
elif z > x > y:
    print("Largest number is : ",z,"and","Smallest number is :",y)
elif x > z > y:
    print("Largest number is : ",x,"and","Smallest number is :",y)
elif z > y > x:
    print("Largest number is : ",z,"and","Smallest number is :",x)
else:
    print("Largest number is :",y,"and","Smallest number is :",x)