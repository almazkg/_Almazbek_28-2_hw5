data_tuple=('h',6.13,'C','e','T',True,'k','e', 3,'e',1,'g')
#create new
letters = []
numbers = []

for i in data_tuple:

    letters.append(i) if type(i) == str else numbers.append(i)

del numbers[0]
letters.append(numbers.pop(0))
numbers.insert(1,2)

numbers.sort()
letters.reverse()

letters[letters.index("g")] = "G"

numbers = [int(i) ** 2 for i in numbers]

letters = tuple(letters)
numbers = tuple(numbers)


print(letters)
print(numbers)