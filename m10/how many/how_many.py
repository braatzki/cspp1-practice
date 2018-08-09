#Exercise : how many
# write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary.


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    return len(aDict)
    

def main():
    aDict={}
    s=input()
    l=s.split()
    for i in range(0,len(l),2):        
        if l[i] not in aDict:
            aDict[l[i]]=l[i+1]
        else:
            aDict[l[i].append(l[i+1])]

    print(how_many(aDict))


if __name__== "__main__":
    main()