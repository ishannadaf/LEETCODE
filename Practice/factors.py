n1 = 10
#       Brute Force Method
factors = []
for i in range(1, n1 + 1):
    if n1 % i == 0:
        factors.append(i)
print("Factors of", n1, "are:", factors)

#       Brute Force Method 2
factors_v2 = []
for i in range(1, (n1 // 2) + 1):
    if n1 % i == 0:
        factors_v2.append(i)

factors_v2.append(n1)  # n1 is also a factor of itself
print("Factors of", n1, "using brute force method 2 are:", factors_v2)

#       Optimized Method
factors_optimized = []
for i in range(1, int(n1**0.5) + 1):
    if n1 % i == 0:
        factors_optimized.append(i)
        if i != n1 // i:
            factors_optimized.append(n1 // i)
factors_optimized.sort()
print("Factors of", n1, "using optimized method are:", factors_optimized)

# Time Complexity: O(n) where n is the number itself for brute force methods
# Time Complexity: O(sqrt(n)) for optimized method

# Space Complexity: O(k) where k is the number of factors found