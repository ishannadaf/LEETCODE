n1 = 153
ln = len(str(n1))
sum = 0
temp = n1
while temp > 0:
    digit = temp % 10
    sum += digit ** ln
    temp = temp // 10
if sum == n1:
    print(n1, "is an Armstrong number.")
else:
    print(n1, "is not an Armstrong number.")