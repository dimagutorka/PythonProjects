import xml.etree.ElementTree as ET

path_to_file = 'data_warehouses/task_5.xml'

tree = ET.parse(path_to_file)
root = tree.getroot()

for elm in root.findall('.//product[@id="1"]/quantity'):
	elm.text = '0'

for elm in root.findall('.//product[@id="2"]/quantity'):
	elm.text = '0'


tree = ET.ElementTree(root)
tree.write(path_to_file, encoding='utf-8')


for i in root:
	for j in i:

		if j.tag == 'name' or j.tag == 'quantity':
			print(f'{j.tag}: {j.text}')
	print('\n')


