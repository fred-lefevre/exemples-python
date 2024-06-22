nb = float(input("Nombre à diviser : "))
div = float(input("Nombre diviseur : "))
try:
    resu = nb / div
except ZeroDivisionError as e:
    print(f"Erreur : {e}")
else:
    print(f"Résultat = {resu:.2f}")

print("Bye!")
