import xml.etree.ElementTree as ET
import xmltodict
import json
tree = ET.parse('menu.xml')
root = tree.getroot()
newele = ET.Element("NightSnack")
newele.attrib = {"hours": "21-23"}
beer = ET.SubElement(newele, "item")
beer.attrib = {"price": "$10"}
beer.text = "beer"
skewers = ET.SubElement(newele, "item")
skewers.attrib = {"price": "$20"}
skewers.text = "skewers"
barbecue = ET.SubElement(newele, "item")
barbecue.attrib = {"price": "$15"}
barbecue.text = "barbeque"
root.append(newele)
tree.write('menu.xml')
with open("menu.xml", "r", encoding="utf8") as xmlfile:
    dictn = xmltodict.parse(xmlfile.read())
    with open("menu.json", "w", encoding="utf8") as thefile:
        json.dump(dictn, thefile)

"""
增加宵夜(Night snack) hours: 21-23
beer: $10
skewers: $20
barbecue: $15

轉成 json 格式存檔成 menu.json
"""
