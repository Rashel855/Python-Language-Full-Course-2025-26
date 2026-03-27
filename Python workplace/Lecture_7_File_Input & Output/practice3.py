count = 1
with open("R:\Python_Learning\Python_workplace\Lecture_7\practice2.txt", "r") as f:
    data = f.read()
    
    nums = data.split(",")
    for val in nums:
        if (int(val)%2==0):
            count+=1
print(count)