s = input()
name = input('What is your name? ')
n = int(input('Enter a number: '))

# output
print('foo', 42, 'bar', sep='/')
print('foo', end='/')

for i in range(10):
    print(n, end=(' ' if n < 9 else '\n'))

print('Hello, my name is %s.' % 'Graham')
print('%d %s cost $%.2f' % (6, 'bananas', 1.74))


# %	Introduces the conversion specifier
# %[<flags>][<width>][.<precision>]<type>

# <flags>	Indicates one or more flags that exert finer control over formatting
# <width>	Specifies the minimum width of the formatted result
# .<precision>	Determines the length and precision of floating point or string output
# <type>	Indicates the type of conversion to be performed

# Conversion Type
# d, i, u	Decimal integer
# x, X	Hexadecimal integer
# o	Octal integer
# f, F	Floating point
# e, E	Exponential
# g, G	Floating point or Exponential
# c	Single character
# s, r, a	String
# %	Single '%' character

print('%d, %i, %u' % (42, 42, 42))
print('%d, %i, %u' % (-42, -42, -42))
print('%x, %X' % (252, 252))
print('%o' % 16)
print('%f, %F' % (3.14159, 3.14))
print('%e, %E' % (1000.0, 1000.0))

x = float('NaN')
y = float('Inf')
print('%f, %e, %F, %E' % (x, x, x, x))
print('%f, %e, %F, %E' % (y, y, y, y))

print('%g' % 3.14)
print('%g' % 0.00000003)
print('%G' % 0.00000003)

print('Get %d%% off on %s today only!' % (30, 'bananas'))

# conversion flag
#	Display of base or decimal point for integer and floating point values
# 0	Padding of values that are shorter than the specified field width
# -	Justification of values that are shorter than the specified field width
# +' ' (space)	Display of leading sign for numeric values
print('%#o' % 16)   # octal
print('%#x' % 16, '%#X' % 16)

d = {'quantity': 6, 'item': 'bananas', 'price': 1.74}
print('%(quantity)d %(item)s cost $%(price).2f' % d)
print('It will cost you $%(price).2f for %(item)s, if you buy %(quantity)d' % d)

