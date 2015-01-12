# sample s = "bobbsoboboboboebobobobotbo"
s = str(raw_input("Enter the input string"))
count = 0;
iterator = 0;
length = len(s)
while (iterator < length):
    if (iterator+3 <= length):
        if (s[iterator:iterator+3] == "bob"):
            count = count + 1
            iterator = iterator + 2
        else:
            iterator = iterator + 1
    else:
        break
print "Number of times bob occurs is: "+ str(count)
