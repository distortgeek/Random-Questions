def isPalindrome(x):
    return x == x[::-1]
    
x = input('Enter your string : ')
y = isPalindrome(x)
 
if y:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")