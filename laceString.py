def joinStrings(s1, s2, n) :
    if(n == 0) :
        return ""
    else :
        result = ""
        for i in range(0,n) :
            result += s1[i] + s2[i]
        return result

def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    lenS1 = len(s1)
    lenS2 = len(s2)
    resultString = ''
    if lenS1 > lenS2 :
        resultString = joinStrings(s1, s2,lenS2)
        resultString += s1[lenS2:]
    elif lenS2 > lenS1 :
        resultString = joinStrings(s1, s2, lenS1)
        resultString += s2[lenS1:]
    else :
        resultString = joinStrings(s1, s2, lenS1)
    return resultString

def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return out+s2
        if s2 == '':
            return out+s1
        else:
            return out + helpLaceStrings(s1[1:],s2[1:],(s1[0]+s2[0]))
    return helpLaceStrings(s1, s2, '')