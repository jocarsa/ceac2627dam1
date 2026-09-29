from lxml import etree

xml = etree.parse("001-ticket.xml")
xsd = etree.parse("003-ticket incorrecto.xsd")

schema = etree.XMLSchema(xsd)

if schema.validate(xml):
    print("XML válido")
else:
    print("XML NO válido")
    print(schema.error_log)