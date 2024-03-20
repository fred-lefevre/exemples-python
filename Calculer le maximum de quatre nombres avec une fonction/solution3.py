def max4(a,b,c,d):
    if a > b and a > c and a > d:
        resultat = a
    elif b > c and b > d:
        resultat = b
    elif c > d:
        resultat = c
    else:
        resultat = d
    return resultat

print(max4(3,7,5,12))
print(max4(14,15,19,8))
print(max4(25,15,19,8))
print(max4(25,55,19,8))
