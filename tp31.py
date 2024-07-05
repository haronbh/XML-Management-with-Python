import xml.etree.ElementTree as ET
import lxml.etree as ET

# Lecture du fichier XML
tree = ET.parse("tp31.xml")
root = tree.getroot()

# Récupération des informations de la commande
orderid = root.attrib.get("orderid")
client = root.find("client").text
livraison = root.find("livraison")
adresse = livraison.find("adresse").text
ville = livraison.find("ville").text
pays = livraison.find("pays").text

items = root.findall("item")

# Affichage des informations de la commande
print("Commande ID:", orderid)
print("Client:", client)
print("Adresse de livraison:", adresse)
print("Ville de livraison:", ville)
print("Pays de livraison:", pays)
print("Items de la commande:")
for item in items:
    category = item.attrib.get("category")
    libelle = item.find("libelle").text
    quantite = item.find("quantite").text
    prix = item.find("prix").text
    devise = item.find("prix").attrib.get("devise", "EUR")
    print(f"  - Catégorie: {category}, Libellé: {libelle}, Quantité: {quantite}, Prix: {prix} {devise}")

