#if x < lo print lo
#if x > hi pring hi
#else print x
#without using conditional statements

def clip(lo,x,hi):
    return max(lo,min(x,hi))