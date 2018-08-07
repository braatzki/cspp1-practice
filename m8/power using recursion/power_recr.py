"""
Calculate exponent of a given base using recursion
"""

def recur_power(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    if exp == 1:
        return base
    return base*recur_power(base, exp-1)
def main():
    '''
    This is the main fucntion
    '''
    data = input()
    data = data.split()
    print(recur_power(float(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
