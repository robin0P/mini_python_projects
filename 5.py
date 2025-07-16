# STRING PALINDROME CONTROL

isPalindrome = False

string = input("Enter a string: ")
reversed_string = string[::-1]
if(string == reversed_string):
    isPalindrome = True

if(isPalindrome):
    print("YES")
else:
    print("NO")
