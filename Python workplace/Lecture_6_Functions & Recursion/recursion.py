#prints n to 1 backwards

def recursion(n):
    if( n==0):
        return
    print(n)
    recursion(n-1)
    print("End")

recursion(5)