# %%

import datetime

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

# %%

# Exercice 3


# Fonction qui calcul l'aire d'un carré
def carre(x: float) -> float:
    return x * x


# Résultat
resultat = carre(3)
print(resultat)

# %%

# Exercice 4


# Fonction qui affiche « Hello prénom » où prénom est une valeur saisie par l’utilisateur
def salutation(prenom: str) -> str:
    return f"Hello {prenom}"


prenom = "Yannick"
print(prenom)
# %%

# Exercice 5


# Fonction pour calculer l'âge à partir de l'année de naissance
def calculer_age(annee_naissance: int) -> int:
    return datetime.datetime.now().year - annee_naissance


# Saisie de l'année de naissance
annee_naissance = int(input("Entrez l'année de naissance de la personne : "))

# Calcul de l'âge
age = calculer_age(annee_naissance)

# Affichage de l'âge
print(f"Une personne née en {annee_naissance} aura {age} ans cette année.")

# %%

# Exercice 6


# Fonction pour calculer le prix TTC à partir du prix HT et d'une TVA de 20%
def calculer_prix_ttc(prix_ht: float, tva: float = 0.20) -> float:
    return prix_ht * (1 + tva)


# Prix HT
prix_ht = 100

# Calcul du prix TTC
prix_ttc = calculer_prix_ttc(prix_ht)

# Affichage du prix TTC
print(f"Le prix TTC pour un prix HT de {prix_ht}€ est de {prix_ttc}€.")
# %%
