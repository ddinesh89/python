s = "abcdefghijklmnopqrstuvwxyz"
length = len(s)
iterator = 0
maxsubstr = ""
while (iterator < length):
    whileIter = iterator;
    substr = ""
    exceed = False
    if (whileIter + 1 <= length - 1): 
        while (s[whileIter] <= s[whileIter+1]):
            substr = substr + s[whileIter]
            whileIter = whileIter + 1
            if(whileIter > length-1 or whileIter+1 > length-1):
                if (whileIter > length-1):
                    exceed = True
                break
        if (not exceed):
            substr = substr + s[whileIter]
    if (len(substr) > len(maxsubstr)):
        maxsubstr = substr
    iterator = whileIter+1
print "Longest substring in alphabetical order is: "+maxsubstr