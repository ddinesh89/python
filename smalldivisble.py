import math

def findPrimeOrComp(number) :
    if number < 2 :
        return False
    tmpNumber = int(math.sqrt(number))
    for factor in range(2,tmpNumber+1) :
        if (number%factor == 0) :
            return False
    return True

def findNthPrime(number) :
    count = 1
    start = 1
    result = 2
    while (count < number) :
        if findPrimeOrComp(start) :
            result = start
            count += 1
        start += 2
    return result
    
            
def getPrimeList(number) :
    primeNumbers = []
    for iterator in range(2,number+1) :
        if findPrimeOrComp(iterator) :
            primeNumbers.append(iterator)
    return primeNumbers
            
def smallDivisiblev2(input) :
    limit = int(math.sqrt(input))
    primes = getPrimeList(input)
    result = 1
    for prime in primes :
        coeff = 1
        if (prime < limit) :
            coeff = int(math.log(input)/math.log(prime))
        result = result * prime**coeff
    return result 



def smallDivisible(input) :
    notSatisfied = True
    multiplier = 1
    result = 0
    while (notSatisfied) :
        satisfied = True
        result = input * multiplier
        for number in range(2,input) :
            if (result%number != 0) :
                satisfied = False
                break
        if satisfied :
            notSatisfied = False
        else:
            multiplier += 1
    return result