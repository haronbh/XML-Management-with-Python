import lxml.etree as ET

# Charger le fichier XML
tree = ET.parse("tp31.xml")

# Charger la DTD
dtd = ET.DTD("DTD1.dtd")

# Valider le document XML par rapport à la DTD
is_valid = dtd.validate(tree)

if is_valid:
    print("Le document est valide selon la DTD.")
else:
    print("Le document n'est pas valide selon la DTD.")
    print("Erreurs de validation :")
    for error in dtd.error_log:
        print(error)

