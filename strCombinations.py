def shiftPrint(tempStr, inputStr, results) :
    """ Recursively rotates the strings and
    returns a list of combinations """
    newStr = tempStr[1:] + tempStr[0]
    if newStr == inputStr :
        if newStr not in results :
            results.append(newStr)
    else :
        if newStr not in results :
            results.append(newStr)
        shiftPrint(newStr, inputStr, results)

def rotateStr(inputStr, iterator) :
    """ Gets an input string and integer iterator
    and rotates the first char and iterator character
    within the string and returns the string """
    tempStr = inputStr[iterator] + inputStr[1:iterator] + inputStr[0] + inputStr[iterator+1:]
    return tempStr

def allcombinations() :
    """ Gets a string from user and prints a list
    of all possible combinations of the string"""
    inputStr = raw_input("Enter the string for which you want all the combinations : ")
    iterator = 0
    results = []
    while iterator < len(inputStr)-1 :
        shiftPrint(inputStr, inputStr, results)
        iterator += 1
        inputStr = rotateStr(inputStr, iterator)
    print results

allcombinations()