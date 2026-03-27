# Write a recursive function to calculate the sum of first n natural numbers. 

def calSumNaturalNumber(n):
     if n==0:
          return 0
     return n + calSumNaturalNumber(n-1)
print("The summation of n natural number is: ", calSumNaturalNumber(5))


# Write a recursive function to print all elements in a list.
# Hint : use list & index as parameters. 

def print_list_el(list, idx = 0):
     if idx == len(list):
          return
     print(list[idx])
     print_list_el(list, idx+1)

num = [1,2,3,4,56,6,7]
print_list_el(num)