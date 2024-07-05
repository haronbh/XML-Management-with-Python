import xml.etree.ElementTree as ET

# Définition de la DTD en tant que chaîne de caractères
dtd = """
<!DOCTYPE stock [
    <!ELEMENT stock (nouveau, occasion+)>
    <!ELEMENT nouveau (libelle, prix)>
    <!ELEMENT libelle (#PCDATA)>
    <!ELEMENT prix (#PCDATA)>
    <!ATTLIST prix devise CDATA #IMPLIED>
    <!ELEMENT occasion (libelle, category, prix, etat)>
    <!ELEMENT category (#PCDATA)>
    <!ELEMENT etat (#PCDATA)>
]>
"""

# Lecture du fichier XML avec la DTD spécifiée
try:
    tree = ET.parse("tp32.xml")
    root = tree.getroot()
    is_valid = True
except ET.ParseError as e:
    is_valid = False
    print("Erreur de parsing:", e)

if is_valid:
    print("Le document est valide selon la DTD.")
else:
    print("Le document n'est pas valide selon la DTD.")

