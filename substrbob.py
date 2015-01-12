# sample s = "bobbsoboboboboebobobobotbo"
s = str(raw_input("Enter the input string"))
count = 0;
iter = 0;
length = len(s)
for letter in s:
    if (letter == "b"):
        if (iter+1 <= length-1 and iter+2 <= length-1):
            if (s[iter+1] == "o" and s[iter+2] == "b"):
                count = count + 1
    iter = iter + 1
print "Number of times bob occurs is: "+ str(count)
