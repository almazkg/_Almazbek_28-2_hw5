ten = list(range(1,10))
evens = list(filter(lambda x: x % 2 == 0,ten))
squared_evens = list(map(lambda x: x ** 2, evens))
def display_list_object(lst = ten):
    try:
        value = lst[ten]
        print(value)
    except IndexError:
        actual_index = input(f"Invalid index'{index}').Please enter the actual index:")
        display_list_object(int(actual_index),lst)
while True:
    index = input("Enter an index to display (or'exit'to quit): ")
    if index == 'exit':
        break
    try:
        display_list_object(index(ten))
    except ValueError:

