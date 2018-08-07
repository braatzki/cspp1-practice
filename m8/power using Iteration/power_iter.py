"""
Iterative function to calculate exponent
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    state_var = 1
    mul_op = 1
    while state_var <= exp:
        mul_op = base*mul_op
        state_var += 1
    return mul_op

    


def main():

    data = input()
    data = data.split()
    print(iterPower(float(data[0]),int(data[1]))) 

if __name__== "__main__":
    main()