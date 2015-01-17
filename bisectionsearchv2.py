def setMinimumPayment(lower,upper):
    return lower + (upper-lower)/2.0

balance = int(raw_input("Enter the balance amount: "))
annualInterestRate = float(raw_input("Enter the annual interest rate(eg: 0.2 for 20%): "))
remainingBal = balance
monthlyInterestRate = annualInterestRate / 12
lowerbound = remainingBal / 12
upperbound = (remainingBal*(1+monthlyInterestRate)**12)/12.0
minimumPayment = setMinimumPayment(lowerbound,upperbound)
epsilon = 0.01
month = 1
while (True):
    while (month <= 12):
        remainingBal = remainingBal - minimumPayment;
        remainingBal = remainingBal + (monthlyInterestRate*remainingBal)
        month += 1
    if (abs(round(remainingBal,2)) <= epsilon):
        break
    if (remainingBal > 0.01):
        lowerbound = minimumPayment
        minimumPayment = setMinimumPayment(lowerbound,upperbound)
        remainingBal = balance
        month = 1
    elif (remainingBal < 0.01):
        upperbound = minimumPayment
        minimumPayment = setMinimumPayment(lowerbound,upperbound)
        remainingBal = balance
        month = 1
print "Lowest Payment: "+str(round(minimumPayment,2))