import xml.etree.ElementTree as ET

# Crée l'élément racine
root = ET.Element("commande")
root.set("orderid", "c9964")

# Ajoute les éléments enfants
client = ET.SubElement(root, "client")
client.text = "Yamada Ayu"

livraison = ET.SubElement(root, "livraison")
adresse = ET.SubElement(livraison, "adresse")
adresse.text = "380-1299, Mahikizawa"
ville = ET.SubElement(livraison, "ville")
ville.text = "Tama-shi"
pays = ET.SubElement(livraison, "pays")
pays.text = "Japan"

item1 = ET.SubElement(root, "item")
item1.set("category", "games")
libelle1 = ET.SubElement(item1, "libelle")
libelle1.text = "Wii U"
note1 = ET.SubElement(item1, "note")
note1.text = "Édition spéciale"
quantite1 = ET.SubElement(item1, "quantite")
quantite1.text = "1"
prix1 = ET.SubElement(item1, "prix")
prix1.text = "900000"

item2 = ET.SubElement(root, "item")
item2.set("category", "food")
libelle2 = ET.SubElement(item2, "libelle")
libelle2.text = "semoule"
quantite2 = ET.SubElement(item2, "quantite")
quantite2.text = "10"
prix2 = ET.SubElement(item2, "prix")
prix2.text = "1050"
prix2.set("devise", "DZD")

# Crée l'arbre XML
tree = ET.ElementTree(root)

# Écrit dans un fichier
tree.write("commande_gen.xml", encoding="utf-8", xml_declaration=True)

print("Fichier XML 'commande_gen.xml' créé avec succès !")