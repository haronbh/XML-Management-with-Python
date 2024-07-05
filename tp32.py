import xml.etree.ElementTree as ET
import lxml.etree as ET


# Lecture du fichier XML
tree = ET.parse("tp32.xml")
root = tree.getroot()

# Récupération des informations sur les articles du stock
articles = root.findall(".//occasion") + root.findall(".//nouveau")

# Affichage des informations sur chaque article
for article in articles:
    print("Article:")
    libelle = article.find("libelle").text
    print("  Libellé:", libelle)
    
    category = article.find("category")
    if category is not None:
        print("  Catégorie:", category.text)
        
    prix = article.find("prix")
    if prix is not None:
        prix_value = prix.text
        devise = prix.attrib.get("devise", "EUR")
        print(f"  Prix: {prix_value} {devise}")
        
    etat = article.find("etat")
    if etat is not None:
        print("  État:", etat.text)
    
    print()  # Ligne vide pour séparer les articles

