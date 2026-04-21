import pandas as pd

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv"

df = pd.read_csv(url)

# Nettoyage des colonnes numériques
df["prix"] = pd.to_numeric(df["prix"], errors="coerce")
df["qte"] = pd.to_numeric(df["qte"], errors="coerce")

# Suppression des lignes invalides
df = df.dropna(subset=["produit", "prix", "qte"])

# Calcul du CA ligne par ligne
df["CA"] = df["prix"] * df["qte"]

# Calcul du CA moyen par produit
ca_moyen_par_produit = df.groupby("produit")["CA"].mean().reset_index()

print(ca_moyen_par_produit)