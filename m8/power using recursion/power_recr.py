"""
Calculate exponent of a given base using recursion
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 1:
        return base
    else:
        return base*recurPower(base, exp-1)
    

def main():
    data = input()
    data = data.split()
    print(recurPower(float(data[0]),int(data[1])))   

if __name__== "__main__":
    main()