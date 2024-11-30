import xml.etree.ElementTree as ET

# Path to the XML file
path_to_file: str = 'data_warehouses/task_5.xml'

# Parse the XML file
tree: ET.ElementTree = ET.parse(path_to_file)
root: ET.Element = tree.getroot()

# Update the quantity of products with specific IDs
for elm in root.findall('.//product[@id="1"]/quantity'):
    elm.text = '0'

for elm in root.findall('.//product[@id="2"]/quantity'):
    elm.text = '0'

# Write the updated tree back to the XML file
tree.write(path_to_file, encoding='utf-8')

# Print the name and quantity of each product
for product in root.findall('.//product'):
    for detail in product:
        if detail.tag in ('name', 'quantity'):
            print(f'{detail.tag}: {detail.text}')
    print('\n')
