"""Python code that compares two variables"""

VARA = 12
VARB = 'RT'
if isinstance(VARA, str) or isinstance(VARB, str):
    print("string involved")
elif VARA > VARB:
    print("bigger")
elif VARA == VARB:
    print("equal")
else:
    print("smaller")
