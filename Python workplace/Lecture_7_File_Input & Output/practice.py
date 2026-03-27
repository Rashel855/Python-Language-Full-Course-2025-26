# Create a new file “practice.txt” using python. Add the following data in it: 
# Hi everyone
# we are learning File I/O
# using Java. 
# I like programming in Java.


# WAF that replace all occurrences of “java” with “python” in above file.
# Search if the word “learning” exists in the file or not.


# with open("R:\Python_Learning\Python_workplace\Lecture_7\practice.txt", "a+") as f:
#     f.write("Hi everyone\nwe are learning File I/O\n")
#     f.write("using Java.\nI like programming in Java.")

# with open("R:\Python_Learning\Python_workplace\Lecture_7\practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("Java", "Python")

# print(new_data)

# with open("R:\Python_Learning\Python_workplace\Lecture_7\practice.txt", "w") as f:
#     f.write(new_data)


word = "learning"
with open ("R:\Python_Learning\Python_workplace\Lecture_7\practice.txt", "r") as f:
    data = f.read()
    if data.find(word) != -1:
        print("Found")
    else:
        print("Not Found")