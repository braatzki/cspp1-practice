'''
GCD of 2 given numbers
'''

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    GCD_out = min(a, b)
    while True:
        if a%GCD_out == 0 and b%GCD_out == 0:
            break
        GCD_out -= 1

    return GCD_out

def main():
    '''
    Main funcion
    '''
    data = input()
    data = data.split()
    print(gcdIter(int(data[0]), int(data[1]))) 

if __name__ == "__main__":
    main()