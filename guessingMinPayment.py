#balance = 3926
#annualInterestRate = 0.2
remainingBal = balance
monthlyInterestRate = annualInterestRate / 12
minimumPayment = 10
month = 1
while (remainingBal > 0):
    print "Guess amt is: "+str(minimumPayment)
    while (month <= 12):
        remainingBal = remainingBal - minimumPayment;
        remainingBal = remainingBal + (monthlyInterestRate*remainingBal)
        month += 1
    if (remainingBal > 0):
        minimumPayment += 10
        remainingBal = balance
        month = 1
    else:
        print "Lowest Payment: "+str(minimumPayment)
        break
    