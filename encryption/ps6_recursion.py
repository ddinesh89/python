# 6.00x Problem Set 6
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    if len(aStr) == 1 :
        return aStr
    else : 
        return aStr[len(aStr)-1] + reverseString(aStr[0:len(aStr)-1])

#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if len(x) == 1 :
        return x in word
    else :
        return x[0] in word and x_ian(x[1:],word[word.index(x[0]):])
        

#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    if len(text) <= lineLength :
        return text
    else :
        if text[lineLength+1] == " " : 
            return text[:lineLength+1] + "\n" + insertNewlines(text[lineLength+2:], lineLength) 
        else :
            length = lineLength
            while text[length+1] != " " or length <= len(text):
                length += 1
            if length == len(text) :
                return text
            else :
                return text[:length] + "\n" + insertNewlines(text[length+2:], lineLength)
