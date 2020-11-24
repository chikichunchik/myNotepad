def task4(strng):
    strng=list(strng)
    numberOfBrackets = 0
    for i in strng:
        if i == "a":
            numberOfBrackets += 1
        if i == "z":
            numberOfBrackets -= 1
        if numberOfBrackets > 0 and not i.isalpha():
            return False
    return True

