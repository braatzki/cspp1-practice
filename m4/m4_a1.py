# """To write a program that counts up the number of vowels
# contained in the string s"""
# S = str(input())
# COUNT = 0
# for LETTER in S:
#     if LETTER in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
#         COUNT += 1
# print("Number of vowels: " + str(COUNT))

# """To write a program that counts up the number of vowels
# contained in the string s"""
# def main():
#     """ This is the code for M4-A1"""
# STR_INP = str(input())
# CNT_INP = 0
# for i in STR_INP:
#     if i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
#         CNT_INP += 1
# print("Number of vowels: " + str(CNT_INP))

"""To write a program that counts up the number of vowels
contained in the string s"""

def main():
    """ This is the code for M4-A1"""
    str_inp = raw_input()
    cnt_inp = 0
    for i in str_inp:
        if i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
            cnt_inp += 1
    print("Number of vowels: " + str(cnt_inp))

if __name__ == "__main__":
    main()
