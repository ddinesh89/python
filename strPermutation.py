def genCombo(inputStr) :
    """ Recursively rotates the strings and
    returns a list of combinations """
    if len(inputStr) == 1 :
        return [inputStr]
    else :
        temp = inputStr[0]
        result = genCombo(inputStr[1:])
        returnResult = []
        for word in result :
            for count in range(0,len(word)+1) :
                if count == 0 :
                    if temp+word not in returnResult :
                        returnResult.append(temp+word)
                else :
                    newWord = word[0:count] + temp + word[count:]
                    if newWord not in returnResult :
                        returnResult.append(newWord)
        return returnResult