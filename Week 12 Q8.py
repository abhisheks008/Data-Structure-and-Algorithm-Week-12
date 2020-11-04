def isPalindrome(s):
    return (s == s[::-1])
 
s = input()
ans = isPalindrome(s)
 
if ans:
    print("The word {} is a palindrome.".format(s))
else:
    print("The word {} is not a palindrome.".format(s))
