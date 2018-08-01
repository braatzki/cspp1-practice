"""a for loop that sums the values 1 through end, inclusive"""
END = int(input("ENTER END: "))
SUM = 0
for N in range(1, END + 1):
    SUM += N
print(SUM)
