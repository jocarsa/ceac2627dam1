from lxml import etree

xml = etree.parse("ticket.xml")
xsd = etree.parse("ticket.xsd")

schema = etree.XMLSchema(xsd)

if schema.validate(xml):
    print("XML válido")
else:
    print("XML NO válido")
    print(schema.error_log)