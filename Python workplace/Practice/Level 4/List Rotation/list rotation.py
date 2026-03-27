# 17. List Rotation ⭐
# Rotate list right by k steps.

def rotate_right(lst, k):
    n = len(lst)
    k = k % n

    for _ in range(k):
        last = lst.pop()
        lst.insert(0, last)

    return lst


string = input("Enter the value and separating by space: ")
str_lst = string.split(" ")
lst = list(str_lst)
print(rotate_right(lst, 8))