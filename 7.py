x = int(input("Enter the number : "))

i = 2
while i < x:
     if  x%i == 0:
        break
    i += 1

if x == i:
    print("Number is Prime.")

else:
    print("Number is Composite.")