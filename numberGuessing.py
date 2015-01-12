print "Please think of a number between 0 and 100!"
epsilon = 0.001
low = 0
high = 100
ans = (low+high)/2
done = False
while (not done):
    print ("")
    print ("Is your secret number "+str(int(ans))+"?")
    print ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly "),
    userSelection = str(raw_input())
    if (userSelection == "h"):
        high = abs(ans)
        ans = int((low + high)/2)
    elif (userSelection == "l"):
        low = abs(ans)
        ans = int((low + high)/2)
    elif (userSelection == "c"):
        done = True
    else:
        print "Sorry, I did not understand your input."
print "Game over. Your secret number was: "+ str(int(ans))