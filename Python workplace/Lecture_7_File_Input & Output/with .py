with open("Sample.txt", "r") as f:
    data = f.read()
    print(data)

with open("Sample.txt", 'r+') as f:
    data = f.write("I love you very much")
    print(data)