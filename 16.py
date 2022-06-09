x = int(input("Enter your number 1 : "))
y = int(input("Enter your number 2 : "))

lst1 = []
hcf = 1

if x > y:
    for i in range(1,x+1):
        if x%i == 0 and y%i == 0:
            lst1.append(i)
            hcf = hcf*i



else:
    for i in range(1,y+1):
        if x%i == 0 and y%i == 0:
            lst1.append(i)
            hcf = hcf*i

print("HCF : ",hcf)
print("Common Factors : ",lst1)


lcm = (x*y)/hcf
print("LCM : ",lcm)