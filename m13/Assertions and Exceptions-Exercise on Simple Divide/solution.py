'''define the simple_divide function here'''
def simple_divide(item, denom):
    '''fucntion'''
    try:
        return item/denom
    except ZeroDivisionError:
        return 0

def fancy_divide(list_of_numbers, index):
    '''fucntion'''
    denom = list_of_numbers[index]
    return [simple_divide(item, denom) for item in list_of_numbers]

def main():
    '''fucntion'''
    data = input()
    l_inp = data.split()
    l1_inp = []
    for j in l_inp:
        l1_inp.append(float(j))
    s_inp = input()
    index = int(s_inp)
    print(fancy_divide(l1_inp, index))


if __name__ == "__main__":
    main()
