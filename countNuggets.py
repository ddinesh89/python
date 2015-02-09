def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    if n == 6 :
        return True
    elif n == 9 :
        return True
    elif n == 20 :
        return True
    else :
        temp = 0
        while(n >= 6) :
            temp = n-6
            if temp > 0 :
                if temp%6 == 0 or temp%9 == 0 or temp%20 == 0 :
                    return True
            temp = n-9
            if temp > 0 :
                if temp%6 == 0 or temp%9 == 0 or temp%20 == 0 :
                    return True
            temp = n-20
            if temp > 0 :
                if temp%6 == 0 or temp%9 == 0 or temp%20 == 0 :
                    return True
            n = n - 6
        return False
