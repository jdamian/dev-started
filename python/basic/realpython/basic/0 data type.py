# Prefix	Interpretation	Base

# 0b (zero + lowercase letter 'b')
# 0B (zero + uppercase letter 'B')	Binary	2
# 0o (zero + lowercase letter 'o')
# 0O (zero + uppercase letter 'O')	Octal	8
# 0x (zero + lowercase letter 'x')
# 0X (zero + uppercase letter 'X')	Hexadecimal	16

# int
print(0o10)
print(0x10)
print(0b10)

type(10)
type(0o10)
type(0x10)

# float 
print(4.2)
type(4.2)
print(4.0)
print(.2)
print(.4e7)
print(4.2e-4)
print(1.79e308) # max float  64-bit “double-precision” 
print(1.8e308)  # inf
print(5e-324)   # The closest a nonzero number can be to zero
print(1e-325)   # zero

#Floating point numbers are represented internally as binary (base-2) fractions. Most decimal fractions cannot be represented exactly as binary fractions, so in most cases the internal representation of a floating-point number is an approximation of the actual value. In practice, the difference between the actual value and the represented value is very small and should not usually cause significant problems.


# complex numbers
print(2+3j)
type(2+3j)


# string
print("I am a string.")
type("I am a string.")

# \a	ASCII Bell (BEL) character
# \b	ASCII Backspace (BS) character
# \f	ASCII Formfeed (FF) character
# \n	ASCII Linefeed (LF) character
# \N{<name>}	Character from Unicode database with given <name>
# \r	ASCII Carriage Return (CR) character
# \t	ASCII Horizontal Tab (TAB) character
# \uxxxx	Unicode character with 16-bit hex value xxxx
# \Uxxxxxxxx	Unicode character with 32-bit hex value xxxxxxxx
# \v	ASCII Vertical Tab (VT) character
# \ooo	Character with octal value ooo
# \xhh	Character with hex value hh

print('foo\nbar')
print(r'foo\nbar')  # raw string
print('''This string has a single (') and a double (") quote.''')

# boolean
type(true)

# built-in fuctions

# math
abs()	# Returns absolute value of a number
divmod()	# Returns quotient and remainder of integer division
max()	# Returns the largest of the given arguments or items in an iterable
min()	# Returns the smallest of the given arguments or items in an iterable
pow()	# Raises a number to a power
round()	# Rounds a floating-point value
sum()	# Sums the items of an iterable

# type conversion
ascii()	# Returns a string containing a printable representation of an object
bin()	# Converts an integer to a binary string
bool()	# Converts an argument to a Boolean value
chr()	# Returns string representation of character given by integer argument
complex()	# Returns a complex number constructed from arguments
float()	# Returns a floating-point object constructed from a number or string
hex()	# Converts an integer to a hexadecimal string
int()	# Returns an integer object constructed from a number or string
oct()	# Converts an integer to an octal string
ord()	# Returns integer representation of a character
repr()	# Returns a string containing a printable representation of an object
str()	# Returns a string version of an object
type()	# Returns the type of an object or creates a new type object

# iterables and iterators
all()	# Returns True if all elements of an iterable are true
any()	# Returns True if any elements of an iterable are true
enumerate()	# Returns a list of tuples containing indices and values from an iterable
filter()	# Filters elements from an iterable
iter()	# Returns an iterator object
len()	# Returns the length of an object
map()	# Applies a function to every item of an iterable
next()	# Retrieves the next item from an iterator
range()	# Generates a range of integer values
reversed()	# Returns a reverse iterator
slice()	# Returns a slice object
sorted()	# Returns a sorted list from an iterable
zip()	# Creates an iterator that aggregates elements from iterables

# composite data type
bytearray()	# Creates and returns an object of the bytearray class
bytes()	# Creates and returns a bytes object (similar to bytearray, but immutable)
dict()	# Creates a dict object
frozenset()	#Creates a frozenset object
list()	# Constructs a list object
object()	# Returns a new featureless object
set()	# Creates a set object
tuple()	# Creates a tuple object

# clases, attributes and inheritance
classmethod()	# Returns a class method for a function
delattr()	# Deletes an attribute from an object
getattr()	# Returns the value of a named attribute of an object
hasattr()	# Returns True if an object has a given attribute
isinstance()	# Determines whether an object is an instance of a given class
issubclass()	# Determines whether a class is a subclass of a given class
property()	# Returns a property value of a class
setattr()	# Sets the value of a named attribute of an object
super()	# Returns a proxy object that delegates method calls to a parent or sibling class

# input / output
format()	# Converts a value to a formatted representation
input()	# Reads input from the console
open()	# Opens a file and returns a file object
print()	# Prints to a text stream or the console

# variables, reference and scope
dir()	# Returns a list of names in current local scope or a list of object attributes
globals()	# Returns a dictionary representing the current global symbol table
id()	# Returns the identity of an object
locals()	# Updates and returns a dictionary representing current local symbol table
vars()	# Returns __dict__ attribute for a module, class, or object

# miscellaneous
callable()	# Returns True if object appears callable
compile()	# Compiles source into a code or AST object
eval()	# Evaluates a Python expression
exec()	# Implements dynamic execution of Python code
hash()	# Returns the hash value of an object
help()	# Invokes the built-in help system
memoryview()	# Returns a memory view object
staticmethod()	# Returns a static method for a function
__import__()	# Invoked by the import statement