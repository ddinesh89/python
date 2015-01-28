def printInst(fr,to):
    print "Move disc from "+ str(fr) +" to "+ str(to)
    
def tower(n,fr,to,sp):
    """ n is number of stacks
        fr is the name of the from tower
        to is the name of the to tower
        sp is the name of the spare tower
        """
    if(n == 1) :
        printInst(fr,to)
    else :
        tower(n-1,fr,sp,to)
        tower(1,fr,to,sp)
        tower(n-1,sp,to,fr)