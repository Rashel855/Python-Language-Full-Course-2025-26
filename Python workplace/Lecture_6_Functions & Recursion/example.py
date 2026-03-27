# WAF to print the length of a list. ( list is the parameter)

random = [1,2,3,"ewcsd",4,6,7]
def print_length (list):
    
    print(len(list))
print_length(random)

# WAF to print the elements of a list in a single line. ( list is the parameter)

def print_el_list ():
    list = [1,2,3,"ewcsd",4,6,7]
    for el in list:
        print(el, end = " ")
print_el_list()

# WAF to find the factorial of n. (n is the parameter)

def find_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact*=i
    return fact
print("The factorial is: ", find_fact(5))

# WAF to convert USD to INR.

def conv_currency(cash):
    c = cash * 75
    return c
print("dollar equal: ", conv_currency(5), " in indian currency")