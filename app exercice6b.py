import pandas as pd

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv"

df = pd.read_csv(url)

# Nettoyage des colonnes numériques
df["qte"] = pd.to_numeric(df["qte"], errors="coerce")


# Calcul de l'écart type des volumes par produit
qte_ecart_type_par_produit = df.groupby("produit")["qte"].std().reset_index()

print("calcule de l'écart type des volumes par produit",qte_ecart_type_par_produit, sep="\n")

# Calculde la variance des volumes par produit
qte_variance_par_produit = df.groupby("produit")["qte"].var().reset_index()

print("calcule la variance des volumes par produit",qte_variance_par_produit, sep="\n")


