# # 1. Even or ODD

# n = int(input("Enter the value on 'n': "))

# if (n%2==0):
#     print("The number", n, "you enter is: EVEN")
# else:
#     print("The number", n, "you enter is: ODD")

# # 2. Sum of Numbers

# n = int(input("Enter a number 'n': "))
# sum = 0
# for i in range(1, n+1):
#     sum +=i
# print("The sum of numbers from '1' to ", n,"is: ",sum)

# # 3. Largest of three number

# class Largest:
#     def __init__(self, a , b, c):
#         if (a>b & a>c):
#             print(a, "is Largest number")
#         elif(b>a & b>c):
#             print(b, "is the largest number")
#         else:
#             print(c,"is the largest number")   
# c1 = Largest(2,3,5)     

# # 4. Multiplication table

# n = int(input("Enter the value on 'n': "))

# for i in range(1, 11):
#     print(n, "*", i, "=", n*i)

str = input("Enter a string: ")
count = 0
for i in str:
    if i in "aeiouAEIOU": # count = sum(1 for ch in s if ch.lower() in "aeiou")
        count +=1
print("The number of vowels in the strings is:", count)