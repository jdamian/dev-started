a = b = c = 300
print(a, b, c)

# object identity
n = 300
m = n
id(n)
id(m)

# reserved words
help("keywords")

# False	def	if	raise
# None	del	import	return
# True	elif	in	try
# and	else	is	while
# as	except	lambda	with
# assert	finally	nonlocal	yield
# break	for	not	
# class	from	or	
# continue	global	pass

# arithmetic operators

# + (unary)	+a	Unary Positive	a
# In other words, it doesn’t really do anything. It mostly exists for the sake of completeness, to complement Unary Negation.
# + (binary)	a + b	Addition	Sum of a and b
# - (unary)	-a	Unary Negation	Value equal to a but opposite in sign
# - (binary)	a - b	Subtraction	b subtracted from a
# *	a * b	Multiplication	Product of a and b
# /	a / b	Division	Quotient when a is divided by b.
# The result always has type float.
# %	a % b	Modulo	Remainder when a is divided by b
# //	a // b	Floor Division (also called Integer Division)	Quotient when a is divided by b, rounded to the next smallest whole number
# **	a ** b	Exponentiation	a raised to the power of b

# comparison operators

# ==	a == b	Equal to	True if the value of a is equal to the value of b
# False otherwise
# !=	a != b	Not equal to	True if a is not equal to b
# False otherwise
# <	a < b	Less than	True if a is less than b
# False otherwise
# <=	a <= b	Less than or equal to	True if a is less than or equal to b
# False otherwise
# >	a > b	Greater than	True if a is greater than b
# False otherwise
# >=	a >= b	Greater than or equal to	True if a is greater than or equal to b
# False otherwise

tolerance = 0.00001
x = 1.1 + 2.2
abs(x - 3.3) < tolerance    # true

x = 5
type(x < 10)

t = x > 10
t           # boolean
callable(x)

# not	not x	True if x is False
# False if x is True
# (Logically reverses the sense of x)
# or	x or y	True if either x or y is True
# False otherwise
# and	x and y	True if both x and y are True
# False otherwise

s = string or '<default_value>'


# bitwise operators

# &	a & b	bitwise AND	Each bit position in the result is the logical AND of the bits in the corresponding position of the operands. (1 if both are 1, otherwise 0.)
# |	a | b	bitwise OR	Each bit position in the result is the logical OR of the bits in the corresponding position of the operands. (1 if either is 1, otherwise 0.)
# ~	~a	bitwise negation	Each bit position in the result is the logical negation of the bit in the corresponding position of the operand. (1 if 0, 0 if 1.)
# ^	a ^ b	bitwise XOR (exclusive OR)	Each bit position in the result is the logical XOR of the bits in the corresponding position of the operands. (1 if the bits in the operands are different, 0 if they are the same.)
# >>	a >> n	Shift right n places	Each bit is shifted right n places.
# <<	a << n	Shift left n places	Each bit is shifted left n places.

'0b{:04b}'.format(0b1100 & 0b1010)  # '0b1000'
'0b{:04b}'.format(0b1100 | 0b1010)  # '0b1110'
'0b{:04b}'.format(0b1100 ^ 0b1010)  # '0b0110'
'0b{:04b}'.format(0b1100 >> 2)  # '0b0011'
'0b{:04b}'.format(0b0011 << 2)  #'0b1100'

# identity operators: is, is not  (same objects)
x = 1001
y = 1000 + 1

x == y # True
x is y #False