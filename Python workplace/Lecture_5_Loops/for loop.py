# using for
# Print the elements of the following list using a loop: 
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100] 

list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

for el in list1:
    print(el)

# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100] 

list2 = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
x = 81
for el in list2:
    if el == x:
        print("The X is found which is: ",el) 
        break
    else:
        print(el)