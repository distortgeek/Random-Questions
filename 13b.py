x = int(input("Enter the number : "))
n = int(input("Enter the range : "))
s = 1
for i in range(1,n+1):
    if i%2 == 0:
        a = x**i
        s = s + a
    else:
        b = -x**i
        s = s + b
    

print ("Sum = ",s)