# WAP to find the sum of first n numbers. (using while)

n = int(input("Enter the value of n: "))

i = 1
sum = 0
while i<=n:
    sum +=i
    i+=1
print(sum)

# WAP to find the factorial of first n numbers. (using for)

n = int(input("Enter the value of n: "))
fact = 1
for i in range(1, n+1):
    fact*=i

print(fact)