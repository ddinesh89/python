def findsqrt(number) :
    epsilon = 0.01
    guess = number/2.0
    while (guess*guess - number >= epsilon) :
        guess = guess - ((guess**2 - number)/(2 * guess))
    return round(guess,1)