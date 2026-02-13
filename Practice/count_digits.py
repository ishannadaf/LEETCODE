n1 = 58730
cnt = 0
while n1 > 0:
    digit = n1 % 10
    cnt += 1
    n1 = n1 // 10

print("Number of digits:", cnt)

# Time Complexity: O(log10 n)
# Space Complexity: O(1)