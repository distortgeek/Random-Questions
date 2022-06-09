x = int(input("Enter the length of the series : "))

f1, f2 = 0, 1
print("Fibonacci Series:", f1, f2, end=" ")
for i in range(2, x):
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    print(f3, end=" ")

print()