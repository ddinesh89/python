balance = int(raw_input("Enter the balance amount: "))
annualInterestRate = float(raw_input("Enter the annual interest rate(eg: 0.2 for 20%): "))
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
    