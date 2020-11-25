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
    strng = list(strng)
    for i in range(len(strng) - 1):
        if (strng[i] == 'a' or strng[i] == 'A') and i != len(strng) - 2:
            return strng[i + 1]
        elif i == len(strng) - 2:
            return "There are no 'a' in text or a in the end of the text"

def task2(strng):
    word = 'can`t do this operation: too small text'
    if len(strng) > 71:
        word = strng[65] + strng[71] + strng[69]
    return word

def task31(strng):
    strng = list(strng)
    for i in range(len(strng)):
        if strng[i] == 'a':
            strng[i] = 'A'
    return ''.join(strng)

def task48(strng):
    ukr_alfa = "абвгґдеєжзиійїклмнопрстуфхцчшщьюя"
    ukr_alfa = list(ukr_alfa)
    word = ''
    for i in strng:
        if i in ukr_alfa:
            word += i
    return word

def task20(strng):
    strng = strng.split()
    strng = ''.join(strng)
    listOfnumbers = list("0123456789 ")
    print(strng)
    print(listOfnumbers)
    for i in strng:
        print(type(i))
        if i in listOfnumbers: strng = strng   
        else:
            return( "Введеный символ не число")
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
    word = word[:int(len(word) -2)]
    word += "."
    return word

def task62(strng):
    if(task62firstCheck(strng)): return task62firstCheck(strng) 
    strng = ('.'.join(strng.split('.')[:-1]))
    if(task62SecondCheck(strng)): return task62SecondCheck(strng) 
    strng = strng.split()
    word=""
    for i in sorted(strng):
        word = word + i + " " 
    word = word[:int(len(word) -1)]
    word += "."
    return word

def task50(strng):
    if(task50firstCheck(strng)): return task50firstCheck(strng) 
    strng = ('.'.join(strng.split('.')[:-1]))
    if(task50SecondCheck(strng)): return task50SecondCheck(strng) 
    secondsrtng = ""
    for i in sorted(strng):
        if(i != " "):
            secondsrtng = secondsrtng + i
    return "True" if(secondsrtng == strng) else "False"


def task50firstCheck(strng):
    numberOfPoints = 0
    for i in strng:
        if(i == ' ' and numberOfPoints == 0): return "у тексте есть пропуск"
        if(i == '.'): numberOfPoints += 1  
    if(numberOfPoints == 0): return "у тексте нету точки"
    elif (numberOfPoints > 1): return "у тексте больше 1 точки"
    return 0 
def task50SecondCheck(strng):
    ukr_alfa = list("ЙЦУКЕНГҐШЩЗХЇЄЖДЛОРПАВІФЯЧСМИТЬБЮ")
    for i in strng:
        if i in ukr_alfa: strng = strng   
        else:
            return( "Введены незнакомые символы")
    return 0 
def task62firstCheck(strng):
    numberOfPoints = 0
    for i in strng:
        if(i == '.'): numberOfPoints += 1  
    if(numberOfPoints == 0): return "у тексте нету точки"
    elif (numberOfPoints > 1): return "у тексте больше 1 точки"
    return 0 
def task62SecondCheck(strng):
    ukr_alfa = list("абвгґдеєжзиійїклмнопрстуфхцчшщьюя ")
    for i in strng:
        if i in ukr_alfa: strng = strng   
        else:
            return( "Введены незнакомые символы")
    return 0