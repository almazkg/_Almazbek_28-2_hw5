data = ('O!','Megacom','0705','Beeline','0550','0770','Katel','0510','Fonex','0543')

design = []

codes = []

for item in data:
    if item[0] == '0':
        codes.append(item)
    else:
        design.append(item)

operators = {}
item = 0
while len < (design):
    operators[design[item]] = set()
item += 1

item = 0

while len < (operators) != 5 :
        operators[design[item]] = {codes[item]}
item += 1

del operators['Katel']
del operators['Fonex']

operators['O!'] = {'0700','0705','0500'}
operators['Megacom'] = {'0550','0555','0999'}
operators['Beeline'] = {'0770','0220','0222'}

for key,value in operators.items():

    print(key,':', value)