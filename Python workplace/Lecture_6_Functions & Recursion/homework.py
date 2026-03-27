# WAF take int input and return str if the number is even return EVEN or ODD

def EVEN_ODD(n):
    if (n%2==0):
        return "EVEN"
    else:
        return "ODD"
    
print(EVEN_ODD(5))