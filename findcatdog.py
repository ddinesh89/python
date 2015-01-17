def cat_dog(str):
    index = 0
    foundCat = 0
    foundDog = 0
    for char in str:
        if (str[index:index+3] == "cat"):
            foundCat += 1
        elif (str[index:index+3] == "dog"):
            foundDog += 1
        index += 1
    if (foundCat == foundDog):
       return True
    else:
       return False