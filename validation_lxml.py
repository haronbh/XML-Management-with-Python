from lxml import etree as ET

xsd_file ='stock.xsd'
xml_file ='stock.xml'


# Parser le document XML 
xml_tree = ET.parse (xml_file)

# Parser le document XSD 
xsd_schema = ET.parse (xsd_file)

# Créer une instance du document XSD 
schema = ET.XMLSchema(xsd_schema)
print('Instance crée !'); 

#Note that the argument can be also a file-like object or a string containing the schema definition. See examples 1 and 2 bellow :


# Exemple 1: 
#schema_file = open('tests/test_cases/examples/collection/collection.xsd')
#schema = xmlschema.XMLSchema(schema_file)

#Example 2 : 
#schema = xmlschema.XMLS chema("""
#<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
#<xs:element name="block" type="xs:string"/>
#</xs:schema>
#""")



#if schema.is_valid ('commande.xml') :
   # print('Validated with success !')
#else :
    #print('contains errors !')
  
schema.validate(xml_tree)

#Peut aussi être utilisée comme suit : 
#fichier_xsd = 'commande1.xsd'
#fichier_xml = 'commande.xml'
#xmlschema.validate (fichier_xml, schema=fichier_xsd)


