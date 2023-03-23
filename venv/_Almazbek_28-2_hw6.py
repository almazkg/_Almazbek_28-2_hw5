def multiply_numbers(*args):
    result = 1
    for num in args:
        result *= num
    return result
print(multiply_numbers(2,3,4,5))


def mirror_string(string,hello='hello'):
        if string == string[::-1]:
           return True
        else:
           return False
print(mirror_string('hello'))

def calculator(num1,operator,num2):
        if   operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2
        elif operator == '%':
            return num1 % num2
        elif operator == '**':
            return num1 ** num2
        else:
           return "Invalid operator"

print(calculator(12,"+",14))


