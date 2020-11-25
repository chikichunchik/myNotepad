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

def task2(strng):
    word = 'can`t do this operation: too small text'
    if len(strng) > 71:
        word = strng[65] + strng[71] + strng[69]
    return word

def task31(strng):
    word = ''
    for i in strng:
        if i == 'a':
            word += 'A'
        else:
            word += i
    return word

def task48(strng):
    ukr_alfa = "абвгґдеєжзиійїклмнопрстуфхцчшщьюя"
    word = ''
    for i in strng:
        is_ukr_letter = False
        for ch in ukr_alfa:
            if i == ch :
                is_ukr_letter = True
        if is_ukr_letter == True:
            word += i
    return word

def task20(strng):
    word = ''
    for i in range(int(strng)+1):
        num = i
        index = 0
        while (num > 2):
            if(int(num / 3) > 0):
                index += 1
                num = int(num / 3)
        num = i
        while (index > 0):
            if(num % (3**index) >= 0):
                word += str(int(num / (3**index)))
                num = int(num - int(num / (3**index)) * (3**index))
            else:
                word += "0" 
            index -=1
        if(index == 0):
            word += str(int(num % 3))
        word +=", "
    return word

def task62(strng):
    newstrng = strng.replace(".","")
    newstrng = newstrng.split()
    word=""
    for i in sorted(newstrng):
        word = word + " " + i
    word += "."  
    return word

def task50(strng):
    firststrng = strng.replace(".","")
    secondsrtng = ""
    for i in sorted(firststrng):  
        if(i != " "):
            secondsrtng = secondsrtng + i
    secondsrtng = secondsrtng[1:]
    firststrng = firststrng[:int(len(firststrng) -1)]
    return True if(secondsrtng == firststrng) else False