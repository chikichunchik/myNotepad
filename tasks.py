def task4(strng):
    strng=list(strng)
    numberOfBrackets = 0
    for i in strng:
        if i == "a":
            numberOfBrackets += 1
        if i == "z":
            numberOfBrackets -= 1
        if numberOfBrackets > 0 and (not i.isalpha() or i.isupper()):
            return False
    return True

def task36(strng):
    strng = strng.lower()
    strng = list(strng)
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    for i in range(len(strng) - 1):
        if i % 2 == 0 and strng[i] in vowels:
            return False
        if i % 2 == 1 and strng[i] not in vowels:
            return False
    return True

def task7(strng):
    strng = strng.lower()
    strng = list(strng)
    numberOfA = 0
    numberOfB = 0
    for i in strng:
        if i == 'a':
            numberOfA += 1
        if i == 'b':
            numberOfB += 1
    return True if numberOfA > numberOfB else False

def task11(strng):
    strng = strng.lower()
    strng = list(strng)
    for i in range(len(strng) - 1):
        if strng[i] == 'a' and i != len(strng) - 2:
            return strng[i + 1]
        elif i == len(strng) - 2:
            return "There are no 'a' in text or a in the end of the text"




