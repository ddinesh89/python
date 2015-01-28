def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    gcd = 1
    iterator = 1
    if (a < b) :
        iterator = a
    else :
        iterator = b
    print iterator
    while iterator > 1 :
        if (a%iterator == 0 and b%iterator == 0) :
            gcd = iterator
            break
        iterator -= 1
    return gcd

def gcdRec(a, b) :
        if(b == 0):
            return a
        else :
            return gcdRec(b,a%b)