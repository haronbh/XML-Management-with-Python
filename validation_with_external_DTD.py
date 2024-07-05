from lxml import etree as ET


xml_path = 'commande_dtd.xml'
dtd_path = 'commande.dtd'

# Parser le document DTD
dtd = ET.DTD (dtd_path)

# Paser le document XML 
xml_tree = ET.parse (xml_path)


# Valider le document XML contre la DTD externe 
is_valid = dtd.validate(xml_tree)
print(is_valid)

#if is_valid:
    #print("Le fichier XML est valide par rapport à la DTD.")
#else:
    #print("Le fichier XML n'est pas valide par rapport à la DTD.")
    #for erreur in dtd.error_log.filter_from_errors():
        #print(erreur)

