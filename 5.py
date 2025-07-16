# STRING PALINDROME CONTROL

isPalindrome = False
string = input("Enter a string: ")

reverse_string = string[::-1]
if string == reverse_string:
    isPalindrome = True

if isPalindrome:
    print("Palindrome")
else :
    print("Not Palindrome")