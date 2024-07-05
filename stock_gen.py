import xml.etree.ElementTree as ET

# Crée l'élément racine "stock"
root = ET.Element("stock")

# Ajoute l'élément "nouveau"
nouveau = ET.SubElement(root, "nouveau")
libelle_nouveau = ET.SubElement(nouveau, "libelle")
libelle_nouveau.text = "Semoule"
prix_nouveau = ET.SubElement(nouveau, "prix")
prix_nouveau.text = "12"
prix_nouveau.set("devise", "USD")

# Ajoute les éléments "occasion"
occasion1 = ET.SubElement(root, "occasion")
libelle_occasion1 = ET.SubElement(occasion1, "libelle")
libelle_occasion1.text = "Nintendo Wii"
category_occasion1 = ET.SubElement(occasion1, "category")
category_occasion1.text = "games"
prix_occasion1 = ET.SubElement(occasion1, "prix")
prix_occasion1.text = "9000"
prix_occasion1.set("devise", "DZD")
etat_occasion1 = ET.SubElement(occasion1, "etat")
etat_occasion1.text = "Bon"

occasion2 = ET.SubElement(root, "occasion")
libelle_occasion2 = ET.SubElement(occasion2, "libelle")
libelle_occasion2.text = "Gödel, Escher, Bach: an Eternal Golden Braid"
category_occasion2 = ET.SubElement(occasion2, "category")
category_occasion2.text = "books"
prix_occasion2 = ET.SubElement(occasion2, "prix")
prix_occasion2.text = "40"
prix_occasion2.set("devise", "EUR")
etat_occasion2 = ET.SubElement(occasion2, "etat")
etat_occasion2.text = "Acceptable"

# Crée l'arbre XML
tree = ET.ElementTree(root)

# Écrit dans un fichier
tree.write("stock_gen.xml", encoding="utf-8", xml_declaration=True)

print("Fichier XML 'stock_gen.xml' créé avec succès !")