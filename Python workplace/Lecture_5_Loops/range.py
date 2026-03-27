# Range functions returns a sequence of numbers, starting from 0 by default, and increments by
# 1 (by default), and stops before a specified number.
# range( start?, stop, step?) 

list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

for el in range(len(list1)):
    print(list1[el])

for el in range(5, len(list1)):
    print(list1[el])


for el in range(1, len(list1), 2):
    print(list1[el])