#newton-rhapson formulae for finding sqrt
inputNum = float(raw_input("Enter the input number: "))
negative = False
if (inputNum < 0):
    negative = True;
    inputNum = abs(inputNum)
epsilon = 0.001
guess = inputNum/2.0
while (abs(guess**2 - inputNum) >= epsilon):
    guess = guess - ((guess**2)-inputNum)/(2*guess)
if (abs(guess**2 - inputNum) >= epsilon):
    print "Could not find the square root of "+str(inputNum)
else:
    if (negative):
        print str(guess) +"i is the approximate square root of "+str(inputNum)
    else:
        print str(guess) +" is the approximate square root of "+str(inputNum)