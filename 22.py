x = int(input("Enter number of students: "))
result = {}
for i in range(x):
    print("Enter Details of student No.", i+1)
    name = input("Name: ")
    marks = int(input("Marks: "))
    result[name] = [marks]    
print(result)  
for student in result:
    a = result.get(student)
    a = int(a)
    if a > 75:
        print(result[student][0])  