x = int(input("Enter the number of rows : "))
a = 65
for i in range(1,x+1):
    for j in range(1,i+1):
        print(chr(a),end=" ")
        a = a+1
    print()