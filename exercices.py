# %%

# Importation du module datetime
import datetime

# %%

# Exercice 1 : à partir de deux nombres `a` et `b`, écrire le résultat pour l’addition, la
# soustraction, la division et la multiplication.
a = 10
b = 10

# Calcul des résultats
addition = a + b
soustraction = a - b

# Vérification pour éviter la division par zéro
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

# Exercice 2 : écrire un algorithme permettant d’afficher le double d’un nombre `x`.


# Fonction qui renvoie le double d'un nombre
def double(x: float) -> float:
    return x * 2


# Résultat
resultat = double(2)

# Affichage du résultat
print(resultat)

# %%

# Exercice 3 : écrire un algorithme permettant de calculer l’aire d’un carré de côté `x`.


# Fonction qui calcul l'aire d'un carré
def carre(x: float) -> float:
    return x * x


# Résultat
resultat = carre(3)

# Affichage du résultat
print(resultat)

# %%

# Exercice 4 : écrire un algorithme qui affiche « Hello prénom » où `prenom` est une valeur saisie par l’utilisateur.


# Fonction qui affiche « Hello prénom » où `prenom` est une valeur saisie par l’utilisateur
def salutation(prenom: str) -> str:
    return f"Hello {prenom}"


# Saisie du prénom
prenom = "Yannick"

# Affichage du prénom
print(prenom)
# %%

# Exercice 5 : écrire un algorithme permettant de calculer l’âge d’une personne à partir de son
# année de naissance saisie au clavier.


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

# Exercice 6 :écrire un algorithme qui calcule le prix TTC à partir d’un prix HT et d’une TVA de 20 %
# (prestation de service en France).


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

# Exercice 7 : Calculez le volume d’un parallélépipède dont la largeur, la longueur et la hauteur seront saisies au clavier.


# Fonction pour calculer le volume d'un parallélépipède
def calculer_volume_parallelepipede(
    largeur: float, longueur: float, hauteur: float
) -> float:
    return largeur * longueur * hauteur


# Saisie des dimensions
largeur = float(input("Entrez la largeur du parallélépipède : "))
longueur = float(input("Entrez la longueur du parallélépipède : "))
hauteur = float(input("Entrez la hauteur du parallélépipède : "))

# Calcul du volume
volume = calculer_volume_parallelepipede(largeur, longueur, hauteur)

# Affichage du volume
print(f"Le volume du parallélépipède est de {volume} unités cubiques.")

# %%
