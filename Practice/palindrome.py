n1 = 1234
rev = 0
while n1 > 0:
    digit = n1 % 10
    rev = rev * 10 + digit
    n1 = n1 // 10
print("Reversed number:", rev)
if rev == 1234:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
    
    

# Time Complexity: O(log10 n)
# Space Complexity: O(1)