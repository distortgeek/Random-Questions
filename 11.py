x = int(input("Enter the number of calls : "))
if 100 >= x:
    print("Telephone Bill : Rs. 100")
elif 100 < x < 150:
    a = x-100
    print("Telephone Bill : Rs.",(100+(a*1.25)))
elif 150 < x < 200:
    b = x-150
    print("Telephone Bill : Rs.",(100+(50*1.25)+(b*1.75)))
else:
    c = x-200
    print("Telephone Bill : Rs.",(100+(50*1.25)+(50*1.75)+(c*2.25)))
