def max2(a,b):
    if a > b:
        return a
    else:
        return b

def max4(a,b,c,d):
    resu1 = max2(a,b)
    resu2 = max2(c,d)
    resultat = max2(resu1, resu2)
    return resultat

print(max4(3,7,5,12))
print(max4(14,15,19,8))
print(max4(25,15,19,8))
print(max4(25,55,19,8))
