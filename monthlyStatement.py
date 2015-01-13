#balance, annualInterestRate, #monthlyPaymentRate
balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate / 12
month = 1
minPayment = 0
remBalance = balance
totalPaid = 0
while (month <= 12):
    print "Month: " +str(month)
    minPayment = remBalance * monthlyPaymentRate
    totalPaid += minPayment
    remBalance = remBalance - minPayment
    remBalance = remBalance + (monthlyInterestRate * remBalance)
    month += 1
    print "Minimum monthly payment: " + str(round(minPayment,2))
    print "Remaining balance: "+str(round(remBalance,2))
print "Total paid: "+str(round(totalPaid,2))
print "Remaining balance: "+str(round(remBalance,2))