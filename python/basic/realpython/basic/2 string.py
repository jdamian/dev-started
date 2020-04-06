# concatenar: +
# multiples copias: *
# contiene: in

s = 'foo'
s in 'That\'s food for thought.'    # true
'z' not in 'abc'                    # true


chr()	# Converts an integer to a character
ord()	# Converts a character to an integer
len()	# Returns the length of a string
str()	# Returns a string representation of an object


ord('a')
ord('#')
chr(97)
len(s)
str(49.2)
s[0]
s[-1]

# slicing
s = 'foobar'
s[2:5]
s[:4]
s[2:]
s[2:len(s)]
s[:4] + s[4:]
s[-5:-2]
s[0:6:2]
s[::5]
s[::-5]
s[5:0:-2]

# f-string

n = 20
m = 25
prod = n * m
print(f'The product of {n} and {m} is {prod}')

# methods
s.capitalize()
s.lower()
s.swapcase()
s.title()
s.upper()
s.replace()

# find and replace
s.count()
s.startswith()
s.endswith()
s.find()
s.rfind()   # reverse
s.isalnum()
s.isalpha()
s.isdigit()
s.isidentifier()
s.islower()
s.isprintable()
s.isspace()
s.istitle()
s.isupper()

# formatting
s.center()
s.expandtabs(tabsize=8)
s.ljust()
s.lstrip()
s.replace()
s.rjust()
s.rstrip()
s.strip()
s.zfill()


# Converting Between Strings and Lists
s.join()
s.partition()
s.rpartition()
s.rsplit()
s.split()
s.splitlines()

# \n	Newline
# \r	Carriage Return
# \r\n	Carriage Return + Line Feed
# \v or \x0b	Line Tabulation
# \f or \x0c	Form Feed
# \x1c	File Separator
# \x1d	Group Separator
# \x1e	Record Separator
# \x85	Next Line (C1 Control Code)
# \u2028	Unicode Line Separator
# \u2029	Unicode Paragraph Separator

# bytes
b = b'foo bar baz'
b = b'foo\xddbar'
b = rb'foo\xddbar'
b = bytes('foo.bar', 'utf8')
b = bytes(8)
b = bytes([100, 102, 104, 106, 108])
b = b'abcde'
b'cd' in b
b'foo' not in b
b[2]
b[1:3]
len(b)
min(b)
max(b)
b = b'foo,bar,foo,baz,foo,qux'
b.count(b'foo')
b.endswith(b'qux')
b.find(b'baz')
b.split(sep=b',')
b.center(30, b'-')
hex(b[3])
list(b)
b = bytes.fromhex(' aa 68 4682cc ')
list(b)
b.hex()

ba = bytearray('foo.bar.baz', 'UTF-8')
bytearray([100, 102, 104, 106, 108])
