import math

def findPrimeOrComp(number) :
    tmpNumber = int(math.sqrt(number))
    for factor in range(2,tmpNumber+1) :
        if (number%factor == 0) :
            return False
    return True

def getPrimeFactors(input) :
    factorsList = []
    if input < 2 :
        return factorsList
    tempRange = input
    for number in range(2,int(math.sqrt(tempRange))+1) :
        if (input%number == 0) :
            if (findPrimeOrComp(number)) :
                factorsList.append(number)
            tempRange /= number
    if tempRange != 0 :
        if (findPrimeOrComp(tempRange)) :
            factorsList.append(tempRange)
    return factorsList
    
def largestPrimeFactor(input) :
    """Returns the largest PrimeFactor below the given input"""
    primeFactors = getPrimeFactors(input)
    return primeFactors[-1]