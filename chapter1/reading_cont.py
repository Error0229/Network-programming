import xml.etree.ElementTree as ET
tree = ET.parse('cont.xml')
root = tree.getroot()
for country in root.iter('country'):
    if country.attrib.get('name') == '新加坡':
        alter = ET.SubElement(country, 'neighbor')
        alter.attrib = {"name": "亞特蘭提斯", "direction": "南"}
    if country.attrib.get('name') == '愛爾蘭':
        sub = country.find('gdppc')
        sub.text = '88888'
tree.write('cont2.xml', encoding='utf-8')

tree2 = ET.parse('cont2.xml')
root2 = tree2.getroot()
dct = {}
for country in root2.iter('country'):
    for neighbor in country.iter('neighbor'):
        dct.setdefault(country.attrib.get('name'), list()
                       ).append(neighbor.attrib.get('name'))
        dct.setdefault(neighbor.attrib.get('name'), list()
                       ).append(country.attrib.get('name'))
for key, value in dct.items():
    for cty in value:
        print(f'{key} : {cty}')
"""
將上面資料存成 cont.xml 檔案
寫程式讀取 cont.xml
1. 加入新加坡 南邊鄰國 亞特蘭提斯，修改愛爾蘭 gdppc 值 88888，寫入 cont2.xml
2. 讀出 cont2.xml 將所有相鄰國家列出
愛爾蘭:英國
英國:愛爾蘭
"""
