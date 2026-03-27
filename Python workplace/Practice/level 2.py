# 6. Reverse a String (without slicing)
# Reverse a string using a loop.

# str = input("Enter the string: ")

# for i in range(len(str)-1, -1, -1):
#     # if str[i]==" ":
#     #     print("", end="")
#     # else:
#         print(str[i], end="")

# rev_str = ""

# for i in str:
#         rev_str = i + rev_str
# print(rev_str)

# i = len(str) - 1
# reverse_str = ""

# while i >= 0:
#     reverse_str += str[i]
#     i -= 1

# print("Reversed string:", reverse_str)


# # 8. Prime Number Check
# # Check whether a given number is prime.

# n = int(input("Enter the value of n:"))

# if n == 1:
#     print("Enter bigger number.")
# else:
#     is_prime = True
#     for i in range(2, n):
#         if n%i==0:
#             is_prime = False
#             break
#     if is_prime:
#         print(n, "is the prime number.")
#     else:
#         print(n, "is not prime number.")

# 9. Fibonacci Series
# Print first n Fibonacci numbers.

# n = int(input("Enter the number:"))
# n1 = 0
# n2 = 1
# if n<=0:
#     print("Enter a positive number....")
# elif n==1:
#     print(n1, end= " ")
# else:
#     print(n1, n2, end=" ")

#     for i in range(n-2):
#         fibo = n1 + n2
#         print(fibo, end=" ")
#         n1 = n2
#         n2 = fibo

# # 10. Remove Duplicates from List
# # Given a list, return a new list without duplicates.

# lst = [1,2,2,3,4,4]
# print(lst)
# new_list = []

# for i in lst:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

lst = ["a", "b", "a", "c", "b", "d"]

# new_list = list(dict.fromkeys(lst))

new_list = list(set(lst))

# new_list = []

# for i in lst:
#     if i not in new_list:
#         new_list.append(i)

print(new_list)