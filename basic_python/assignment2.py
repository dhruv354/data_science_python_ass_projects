def func(a, b):
    if a > b:
        return a
    else:
        return b

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))


output = func(a, func(b, c))
print(output)