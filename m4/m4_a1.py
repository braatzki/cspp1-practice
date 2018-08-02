"""To write a program that counts up the number of vowels
contained in the string s"""
S = str(input("Enter string: "))
COUNT = 0
for LETTER in S:
    if LETTER in ('a', 'e', 'i', 'o', 'u'):
        COUNT += 1
print("Number of vowels: " + str(COUNT))
