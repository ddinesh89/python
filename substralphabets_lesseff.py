# less effective approach as it loops over every character
s = str(raw_input("Enter the input string"))
length = len(s)
iterator = 0
maxsubstr = ""
for letter in s:
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
    iterator = iterator + 1
print "Longest substring in alphabetical order is: "+maxsubstr
