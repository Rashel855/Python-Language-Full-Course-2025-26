# Print numbers from 1 to 100. 

i = 1
print("Print numbers from 1 to 100:")
while i<=100:
    print(i)
    i+=1


# Print numbers from 100 to 1. 

i = 100
print("Print numbers from 100 to 1:")
while i>=1:
    print(i)
    i-=1

# Print the multiplication table of a number n. 

n = int(input("Enter the number: "))
i = 1
while i<=10:
    print("The multiplication table of ", n,"*",i, " = ", n * i)
    i+=1

# Print the elements of the following list using a loop: 
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100] 

list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
i = 0
while i<=len(list)-1:
    print(list[i])
    i+=1

# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

tup = tuple([1, 4, 9, 16, 25, 36, 49, 64, 81,100])

print(type(tup))

x = 36

i = 0

while i<=len(tup)-1:
    if tup[i]== x:
        print("The index of the tup is: ", i, "and the value of tup is: ", tup[i])
        break
    else:
        print("finding")
    i+=1


i = 0

while i <= 10:
    if (i==5):
        i+=1
        continue
    print(i)
    i+=1