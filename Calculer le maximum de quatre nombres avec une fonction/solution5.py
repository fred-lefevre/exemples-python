def max4(a,b,c,d):
    resultat = a
    if b > resultat:
        resultat = b
    if c > resultat:
        resultat = c
    if d > resultat:
        resultat = d
    return resultat

print(max4(3,7,5,12))
print(max4(14,15,19,8))
print(max4(25,15,19,8))
print(max4(25,55,19,8))
