import math

def findPrimeOrComp(number) :
    for factor in range(2,int(math.sqrt(number))) :
        if (number%factor == 0) :
            return False
    return True