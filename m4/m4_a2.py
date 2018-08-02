"""A program that prints the number of times the
string 'bob' occurs in s"""
S = str(input("Enter string: "))
I = len(S)
COUNT = 0
for N in range(I-1):
    if len(S[N:N+3]) == 3 and S[N:N+3] in 'bob':
        COUNT += 1
print('Number of times bob occurs is: ' + str(COUNT))
