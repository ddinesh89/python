def findSubStr(s):
    iterator = 0
    startIndex = 0
    index = 0
    maxLength = 1
    length = 1
    while (iterator < len(s)-1):
        if (s[iterator] <= s[iterator+1]):
            length += 1
            if (length > maxLength):
                maxLength = length
                startIndex = index
        else:
            length = 1
            index = iterator+1
        iterator += 1
    return s[startIndex:startIndex+maxLength]