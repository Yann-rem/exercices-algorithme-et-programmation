# %%

# Exercice 1
a = 10
b = 10

# Calcul des résultats
addition = a + b
soustraction = a - b

if b != 0:
    division = a / b
else:
    division = "Indéfini (division par zéro)"

multiplication = a * b

# Affichage des résultats
print(f"Addition : {a} + {b} = {addition}")
print(f"Soustraction : {a} - {b} = {soustraction}")
print(f"Division : {a} / {b} = {division}")
print(f"Multiplication : {a} * {b} = {multiplication}")

# %%

# Exercice 2


# Fonction qui renvoie le double d'un nombre
def double(x: float) -> float:
    return x * 2


# Résultat
resultat = double(2)
print(resultat)
