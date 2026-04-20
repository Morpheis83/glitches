import csv
import urllib.request
from collections import defaultdict

# URL du CSV
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv"

# Téléchargement du fichier
response = urllib.request.urlopen(url)
lines = [l.decode('utf-8') for l in response.readlines()]

# Lecture CSV
reader = csv.DictReader(lines)

col_produit = "produit"
col_volume = "qte"

# Agrégation des volumes par produit
ventes = defaultdict(int)

for row in reader:
    try:
        produit = row[col_produit]
        volume = int(float(row[col_volume]))  # gère "10.0" ou "10"
        ventes[produit] += volume
    except (ValueError, KeyError):
        continue  # ignore lignes invalides

# Recherche max / min
max_volume = max(ventes.values())
min_volume = min(ventes.values())

plus_vendus = [p for p, v in ventes.items() if v == max_volume]
moins_vendus = [p for p, v in ventes.items() if v == min_volume]

print("Produits les plus vendus :", plus_vendus, "=>", max_volume)
print("Produits les moins vendus :", moins_vendus, "=>", min_volume)