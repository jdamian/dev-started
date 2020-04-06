# x = set(<iter>)
# x = {<obj>, <obj>, ..., <obj>}

x = set(['foo', 'bar', 'baz', 'foo', 'qux'])
s = 'quux'
list(s)
set(s)

x = {'foo', 'bar', 'baz', 'foo', 'qux'}
x = {'q', 'u', 'u', 'x'}
x = {42, 'foo', 3.14159, None}
x = {42, 'foo', (1, 2, 3), 3.14159}

x = {}  # class

len(x)
'bar' in x

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
x1 | x2
x1.union(x2)
x1.intersection(x2)
x1 & x2
x1.difference(x2)
x1 - x2
x1.symmetric_difference(x2)
x1 ^ x2
x1.isdisjoint(x2)   # true when no elements in common
x1.issubset({'foo', 'bar', 'baz', 'qux', 'quux'})
x1 <= x2
x1 < x2     # x1 in x2 and are not equal
x1.issuperset({'foo', 'bar'})
x1 >= x2
x1 > x2     # proper superset


a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}
a.union(b, c, d)
a | b | c | d
a.intersection(b, c, d)
a & b & c & d
a.difference(b, c)
a - b - c
a ^ b ^ c


# Modifying a Set
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}

x1 |= x2
print(x1)
x1.update(['corge', 'garply'])

x1 &= x2
x1.intersection_update(['baz', 'qux'])

x1 -= x2
x1.difference_update(['foo', 'bar', 'qux'])

x1 ^= x2
x1.symmetric_difference_update(['qux', 'corge'])

x.add('qux')
x.remove('baz')
x.discard('baz')    # remove quietly
x.pop()
x.clear()

# frozen sets
x = frozenset(['foo', 'bar', 'baz'])
len(x)
x & {'baz', 'qux', 'quux'}
s = {'baz', 'qux', 'quux'}
x &= s  # x is a new object

x1 = frozenset(['foo'])
x2 = frozenset(['bar'])
x3 = frozenset(['baz'])
x = {x1, x2, x3}
