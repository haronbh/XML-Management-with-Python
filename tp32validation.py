import lxml.etree as ET

# Charger le schéma XSD
schema = ET.XMLSchema(ET.parse("tp32.xsd"))

# Lecture du fichier XML
tree = ET.parse("tp32.xml")
root = tree.getroot()

# Valider le document XML par rapport au schéma XSD
is_valid = schema.validate(tree)

if is_valid:
    print("Le document est valide selon le schéma XSD.")
else:
    print("Le document n'est pas valide selon le schéma XSD.")
    print("Erreurs de validation :")
    for error in schema.error_log:
        print(error)

