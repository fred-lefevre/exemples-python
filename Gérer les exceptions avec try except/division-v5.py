nb = float(input("Nombre à diviser : "))
try:
    div = float(input("Nombre diviseur : "))
    resu = nb / div
except ZeroDivisionError as e:
    print(f"Erreur : {e}")
except Exception as e:
    print(f"Erreur : {e}")    
    print(f"Type : {type(e).__name__}")    
else:
    print(f"Résultat = {resu:.2f}")
finally:
    print("Bye!")
