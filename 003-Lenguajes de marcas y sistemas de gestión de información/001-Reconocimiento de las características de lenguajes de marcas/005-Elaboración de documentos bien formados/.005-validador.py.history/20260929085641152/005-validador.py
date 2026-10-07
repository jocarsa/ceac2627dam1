from lxml import etree

xml = etree.parse("003-ticket incorrecto.xml")
xsd = etree.parse("002-plantilla ticket.xsd")

schema = etree.XMLSchema(xsd)

if schema.validate(xml):
    print("XML válido")
else:
    print("XML NO válido")
    print(schema.error_log)