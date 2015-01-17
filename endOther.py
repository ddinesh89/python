def end_other(a, b):
    """ Given two strings a,b
    return True if a is found at the end of b
    or if b is found at a (case insensitive) else
    return False"""
    lengthA = len(a)
    lengthB = len(b)
    if (lengthA < lengthB):
        diff = lengthB - lengthA
        if (b[diff:].lower() == a.lower()):
            return True
        else:
            return False
    elif (lengthB < lengthA):
        diff = lengthA - lengthB
        if (a[diff:].lower() == b.lower()):
            return True
        else:
            return False
    else:
        if (a.lower() == b.lower()):
            return True
        else:
            return False