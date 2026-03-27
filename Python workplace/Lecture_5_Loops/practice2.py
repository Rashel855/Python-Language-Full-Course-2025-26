# using for & range( )
# Print numbers from 1 to 100. 

for i in range(1, 101):
    print(i)

# Print numbers from 100 to 1. 

el = 100

for i in range(100):
    print(el)
    el-=1
    
# Print the multiplication table of a number n. 

n = 4
for i in range(1, 11):
    print(n, "*", i, "=", n * i)