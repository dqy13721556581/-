def isNum (word):
    try:
        words = type (eval(word))
        if words == type(I):
            return True
        elif words == type(1.0):
            return True
        elif words == (1+1j):
            return  True
    except:
        return  False
n = input()
print (isNum(n))
