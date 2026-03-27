# name = input("Enter your name here: ")
# age = int(input("Enter your age here: "))
# height = float(input("Enter your height here: "))

# print("The input name, age and height show below:\n", name, age, height)

# age = "20"
# age = int(age) # this line not in the problem i add this line for solving error purpose
# next_age = age + 1
# print(next_age)

# length = int(input("Enter the length: "))
# breadth = int(input("Enter the breadth: "))

# area = length * breadth

# print("The area of rectangle is: ", area)

# number = int (input (" Enter the number: "))

# print(number%5==0)

# x = int("10")
# y = float("5")
# print(x * y)

# str = input("Enter the string here: ")

# print("The first caracter: ", str[0], "The last character: ", str[-1])

# s = "PythonProgramming"


# print(s[:6])
# print(s[6:])

# sequece = input("Enter the secuence: ")

# print(sequece.count("a"))

# num = int (input("Enter the number: "))
# if(num>0):
#     print("POsitive")
# elif(num<0):
#     print("Negative")
# else:
#     print("Zero")

# marks = [45, 67, 89, 32, 76]
# student = []
# for i in marks:
#     if (i>60):
#         student.append(marks)
# print (len(student))

# tuple = (4,4,3,5,4,5,4,5,3,5)
# print(tuple.count(5))

# tup = (1, 2, 3, 2, 1)

# tup = list(tup)

# tup1 =tup.copy()
# tup1.reverse()
# if(tup==tup1):
#     print("paliondrome")
# else:
#     print("Not Palindrome")

# nums = []


# for i in range(3):
#     num = int(input("Enter the number that you want: "))
#     nums.append(num)

# greatest = nums[0]
# for j in nums:
#     if j>greatest:
#         greatest = j
#     else:
#         j+=1

# print("The greatest number is:", greatest)

# list1 = []

# for i in range(3):
#     list1.append(input("Enter the names: "))

# list1.sort()
# print(list1)

str = input("Enter a string: ")
list1 = []

for i in range(len(str)):
    list1.append(str[i])

list2 = list1.copy()
list2.reverse()

if(list1 == list2):
    print("The string is palindrome!")
else:
    print("The string is not palindrome")