Geeks={
    'address':'Toktogula 174',
    'courses':['android''backend''frontend'],
    'bag':{'errors','fails','stack'}
}

#удаления багов(1)
del Geeks['bag']
#изменения адреса на ннешний(2)
Geeks['address'] = 'Ibraimova 103,Bishkek'
#добавления телефон номера и инстаграмм аккаунт Geeks(3)
Geeks['phone'] = '996507052018'
Geeks['instagram'] = '@geeks_edu'
#расширение списков актуальных курсов и переобразование списка в set(4)
new_courses = ['mobile development','ux/ui-design','IOS-development']
Geeks['courses'].extend(new_courses)
Geeks['courses'] = set(Geeks['courses'])
#дата основания Geeks(5)
Geeks['founding_date'] = 'january 1, 2018'
#вывод количества уроков(6)
print(len(Geeks['courses']))
#вывод словоря с помощю цикла for (7)
for key, value in Geeks.items():
    print(key +':', value)