nb = float(input("Nombre à diviser : "))
div = float(input("Nombre diviseur : "))
try:
    resu = nb / div
    print(f"Résultat = {resu:.2f}")
except ZeroDivisionError as e:
    print(f"Erreur : {e}")

print("Bye!")
