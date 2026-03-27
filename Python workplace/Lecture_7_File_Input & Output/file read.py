f = open("R:\Python_Learning\Python_workplace\demo.txt", "r")

# data = f.read()

# print(data)

line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
line4 = f.readline()

print(line1)
print(line2)
print(line3)
print(line4)


f.close()