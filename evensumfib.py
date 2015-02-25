def genFibonacci(input):
    fibSeries = [1, 2]
    while (fibSeries[-1] < input):
        fibSeries.append(fibSeries[-1]+fibSeries[-2])
    fibSeries.pop(-1)
    return fibSeries

def evenSumFibonacci(input):
    fibSeries = genFibonacci(input)
    finalSum = 0
    for number in fibSeries:
        if (number%2 == 0):
            finalSum += number
    return finalSum