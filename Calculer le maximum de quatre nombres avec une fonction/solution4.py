def max4(a,b,c,d):
    if a > b and a > c and a > d:
        return a
    if b > c and b > d:
        return b
    if c > d:
        return c
    return d

print(max4(3,7,5,12))
print(max4(14,15,19,8))
print(max4(25,15,19,8))
print(max4(25,55,19,8))
