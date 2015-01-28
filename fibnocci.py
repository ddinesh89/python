def fib(n) :
    """ returns the nth fib number
        """
    if (n == 0 or n == 1) :
        return 1
    else :
        return fib(n-1) + fib(n-2)
        
def generateFib(n):
        """returns the fibonacci series
        uptil the nth element"""
        print "The fibonacci series is"
        for i in range(0,n+1):
            print str(fib(i))+" "