"""while loop that sums the values 1 through end, inclusive"""
END = int(input("Enter END: "))
# print(END)
N = 1
SUM = 0
while N <= END:
    SUM += N
    N += 1
print(SUM)
