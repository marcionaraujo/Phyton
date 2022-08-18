
# Online Python - IDE, Editor, Compiler, Interpreter

def sum(a, b):
    c = a + b
    return (c)

def pro(a, b):
    c = a / b
    return (c)
    
def sumsqr(a, b):
    return (a * a + b * b)

a = float(input('Enter 1st number: '))
b = float(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')
print(f'Product of {a} and {b} is {pro(a, b)}')
print(f'The sum of squares of {a} and {b} is {sumsqr(a, b)}')

