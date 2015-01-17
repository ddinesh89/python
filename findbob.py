def findBob():
    s = raw_input("Enter the test string: ")
    index = 0
    count = 0
    for char in s:
        if (s[index:index+3] == "bob"):
            count += 1
        index += 1
    print "The count is: "+str(count)