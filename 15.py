n = int(input("Enter number to convert : "))
y= []
while n > 0:
    z = n % 2
    y.append(z)
    n = n // 2
y.reverse()
print("Binary is: ")
for i in y:
    print(i,end=" ")