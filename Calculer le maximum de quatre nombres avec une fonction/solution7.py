def max2(a,b):
    if a > b:
        return a
    return b

def max4(a,b,c,d):
    return max2(max2(a,b), max2(c,d))

print(max4(3,7,5,12))
print(max4(14,15,19,8))
print(max4(25,15,19,8))
print(max4(25,55,19,8))
