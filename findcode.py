def count_code(str):
    """Given an input string
    the code will return the 
    number of time code occurs
    except it doesn't care what
    'd' in code is replaced with"""
    index = 0
    count = 0
    for char in str:
        if (str[index:index+2] == "co"):
            if (str[index+3:index+4] == "e"):
                count += 1
        index += 1
    return count