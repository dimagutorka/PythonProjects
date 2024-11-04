# Read the file
with open('text.txt', 'r') as fr:
    a = fr.readlines()

q = []
for i in a:
    b = i.replace('\n', '')
    q.append(b)

# Custom print with double quotes
print('[' + ', '.join(f'"{item}"' for item in q) + ']')
