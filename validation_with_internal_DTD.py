from lxml import etree as ET

xml_path = 'stock_dtd.xml'
dtd_path = 'stock.dtd'

# Parser le document XML
xml_tree = ET.parse(xml_path)

# Récupérer la DTD interne 
dtd = xml_tree.docinfo.internalDTD

# Valider le document XML contre la DTD interne
is_valid = dtd.validate(xml_tree)

if is_valid:
    print("Le fichier XML est valide par rapport à la DTD.")
else:
    print("Le fichier XML n'est pas valide par rapport à la DTD.")
    for erreur in dtd.error_log.filter_from_errors():
        print(erreur)
