# Practice 01: WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

movies =[] 
movies.append(input("Enter names of your 1st favorite movie: "))
movies.append(input("Enter names of your 2nd favorite movie: "))
movies.append(input("Enter names of your 3rd favorite movie: "))

print(movies)

# Practice 02: WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
    # [1, 2, 3, 2, 1]
    # [1, “abc”, “abc”, 1]

list = [1,2,3,2,1]

new_list = list.copy()

new_list.reverse()

if (list == new_list):
    print("the list is palindrome")

# Practice 03: WAP to count the number of students with the “A” grade in the following tuple.
# [”C”, “D”, “A”, “A”, “B”, “B”, “A”]
# Store the above values in a list & sort them from “A” to “D”.

tup = ("C", "D", "A", "A", "B", "B", "A")

print(tup.count("A"))

list = ["C", "D", "A", "A", "B", "B", "A"]

print(type(list))
list.sort()
print(list)