import plotly.express as px
import pandas as pd

donnees = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

# Calcul CA
donnees["CA"] = donnees["prix"] * donnees["qte"]

# Agrégation par produit (IMPORTANT pour un pie chart)
ca_par_produit = (
    donnees.groupby("produit")["CA"]
    .sum()
    .reset_index()
)

figure = px.pie(donnees, values='CA', names='produit', title='CA par produit')

figure.write_html('ca-par-produit.html')

print('ca-par-produit.html généré avec succès !')
