# 11. Second Largest Number in List
# Find the second largest number without using sort().

# lst = [100,4,3,16,74,9,0]

# largest = second_largest = -1

# for i in lst:
#     if i > largest:
#         largest = i

# for i in lst:
#     if i != largest and i > second_largest:
#         second_largest = i
    
# print(largest)
# print(second_largest)

# # 12. Word Frequency Counter
# # Given a sentence, count frequency of each word.

# # "python is fun python is easy"

# sentence = "python is fun python is easy"

# words = sentence.split(" ")

# freq = {}

# for word in words:
#     if word in freq:
#         freq[word] += 1
#     else:
#         freq[word] = 1

# print(freq)

# # 13. Palindrome Checker
# # Check if a string is a palindrome (ignore spaces and case).

# strng = input("Enter the string: ")

# strng = strng.replace(" ", "").lower()

# rev_str = ""
# for ch in strng:
#     rev_str = ch + rev_str

# if strng == rev_str:
#     print("The string '",strng, "' is Palindrome.") 
#     # use this with remove the extra space -->print(f"The string '{strng}' is palindrome.")
# else:
#     print(f"The string '{strng}' is not Palindrome.")
