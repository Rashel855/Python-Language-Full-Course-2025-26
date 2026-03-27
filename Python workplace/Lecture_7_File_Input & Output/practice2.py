# WAF to find in which line of the file does the word “learning”occur first. 
# Print -1 if word not found. 
# From a file containing numbers separated by comma, print the count of even numbersword = "learning"

def check_for_line():
    word = "dhjskdfsk"
    data = True
    line_no = 1
    with open ("R:\Python_Learning\Python_workplace\Lecture_7\practice.txt", "r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print("The word 'learning' is found in line no: ", line_no) 
                return
            line_no+=1
    return -1

print(check_for_line())