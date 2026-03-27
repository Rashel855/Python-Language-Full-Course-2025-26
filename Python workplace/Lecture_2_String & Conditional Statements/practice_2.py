# WAP to check if a number entered by the user is odd or even.

number = int(input("Enter the value of the number: "))

if (number%2==0):
    print("the number you enter is even.")
else:
    print("the number you enter is Odd.")

# WAP to find the greatest of 3 numbers entered by the user.

num1 = int(input("Enter the value of the num1: "))
num2 = int(input("Enter the value of the num2: "))
num3 = int(input("Enter the value of the num3: "))


if (num1>num2 & num1>num3):
    print("The number 1 is the greatest number", num1)
elif (num2>num1 & num2>num3):
    print("The number 2 is the greatest number", num2)
else:
    print("The number 3 is the greatest number", num3)
    
        
# WAP to check if a number is a multiple of 7 or not.

n = int(input("Enter the value of the number, n = "))

if (n % 7 == 0):
    print("The number is multiple of 7")
else:
    print("The number is not multiple of 7")

# WAP to find the greatest of 4 numbers entered by the user.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a >= b and a >= c and a >= d:
    greatest = a
elif b >= a and b >= c and b >= d:
    greatest = b
elif c >= a and c >= b and c >= d:
    greatest = c
else:
    greatest = d

print("The greatest number is:", greatest)