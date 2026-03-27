# Store following word meanings in a python dictionary : 
# table : “a piece of furniture”, “list of facts & figures”
# cat : “a small animal”

dictionary = {
    "table" : ("a piece of furniture", "list of facts & figures"),

    "cat" : "a small animal"
}

print(dictionary)

# You are given a list of subjects for students. Assume one classroom is required for 1
# subject. How many classrooms are needed by all students.
# ”python”, “java”, “C++”, “python”, “javascript”,
# “java”, “python”, “java”, “C++”, “C”

subject1 = {"Python", "Java", "C++", "Python", "Javascript"}
subject2 = {"Java", "Python",  "Java", "C++", "C"}

subjects = subject1.union(subject2)

print("The number of classroom needed for the students are: ",len(subjects))



# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.

dictionary = {

}

for i in range(3):
    dictionary.update({input("Enter subject name: ") : int(input("Enter the marks of subject value: "))})

print(dictionary)

# Figure out a way to store 9 & 9.0 as separate values in the set. 
# (You can take help of built-in data types) 


set = {9, str(9.0)}
print(set)