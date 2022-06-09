x = int(input("Enter the number : "))
n = int(input("Enter the range : "))
s = 1
for i in range(1,n+1):
    a = x**i
    s = s + a

print ("Sum = ",s)